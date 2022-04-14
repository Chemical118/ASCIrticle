class RF:
    def __init__(self, floc, dloc, loc=0):
        self.__amino_loc = loc
        self.__fasta_loc = floc
        self.__data_loc = dloc

    def get_id_list(self):
        from Bio import SeqIO
        return list(map(lambda t: t.id, SeqIO.parse(self.__fasta_loc, 'fasta')))

    def view_sequence(self, typ='fasta', fontsize="9pt", plot_width=800):
        from prorf.rfunction import view_sequence
        view_sequence(self.__fasta_loc, self.__amino_loc, typ, fontsize, plot_width)

    def get_amino_loc(self, loca):
        import numpy as np
        return np.array(list(map(lambda t: t[0] + 1 + self.__amino_loc, loca)))

    def view_importance(self, fim, loc, show_number=20):
        import numpy as np
        import matplotlib.pyplot as plot

        amino_names = self.get_amino_loc(loc)
        feature_importance = fim / fim.max()
        sorted_idx = np.argsort(feature_importance)
        bar_pos = np.arange(sorted_idx.shape[0]) + .5
        plot.barh(bar_pos[-show_number:], feature_importance[sorted_idx][-show_number:], align='center')
        plot.yticks(bar_pos[-show_number:], amino_names[sorted_idx][-show_number:])
        plot.xlabel('Variable Importance')
        plot.ylabel('Amino acid Location')
        plot.show()

    def __data_list(self):
        """
        df_list는 아래와 같은 모습을 가진다.
        [Seq 단백질 서열, [종 이름, Reference, NCBI No., Catalase Acitivty], index],
        """
        from Bio import SeqIO
        import pandas as pd
        df = pd.read_excel(self.__data_loc)
        df_list = df.values.tolist()
        df_list = list(map(lambda te: [*te[::-1]], enumerate(df_list)))
        for ind, val in enumerate(SeqIO.parse(self.__fasta_loc, 'fasta')):
            df_list[ind].insert(0, str(val.seq))
        return df_list

    def __process(self):
        """
        process는 아래와 같이 3개의 tuple를 반환한다
        (pro, d_list, dnum_list)
        이들은 각각 아래와 같은 의미를 가진다

        pro : 순서별로 몇개의 아미노산 종류가 있는지, 그것이 어느 것에는 어떤 것이 있는지 확인 ([[["M", "K"], {각각에 대한 딕셔너리}].. ]) + 또한 대상은 중복되지 않는다 (set과
        같은 list라 생각하자) d_list : 하나의 위치에 2개 이상의 아미노산을 가지는 대상들의 번호 dnum_list : d_list에서 가장 적은 개수를 가지는 아미노산의 개수 (몇개의 대상에서
        mutaion이 일어났는지 확인)
        """
        data = self.__data_list()
        data = list(map(lambda te: te[0], data))  # 단순 단백질 서열 list로 변경
        len_data = len(data[0])  # data의 모든 길이는 같다
        pro = list()
        for q in range(len_data):
            data_set = list()
            data_dict = dict()
            for ind, val in enumerate(data):
                tar = str(val[q])
                if tar not in data_set:
                    data_dict[tar] = []
                    data_set.append(tar)
                data_dict[tar].append(ind)
            pro.append([data_set, data_dict])
        dt_list = list()
        dtnum_list = list()

        for ind, val in enumerate(pro):
            if len(val[0]) != 1:
                dt_list.append(ind)
                dtnum_list.append(
                    len(data) - max(map(lambda te: len(te), val[1].values())))  # 5/12 수정 (최소가 아닌 최대의 나머지 개수)
        return pro, dt_list, dtnum_list

    def get_data(self, ami_arr, data_loc, norm=False):
        """

        :param ami_arr: select data with have over the number of data than setting
        :type ami_arr: int
        :param data_loc: excel row alphabet
        :type data_loc: str
        :param norm: normalization the data
        :type norm: bool
        """
        from prorf.rfunction import blo62

        import numpy as np
        pros = self.__process()
        data = self.__data_list()
        pro = pros[0]

        dtot_list = list(zip(pros[1], pros[2]))  # dtot_list : [(아미노산 위치, mutation 개수).. ]
        nogap_dtot_list = \
            list(filter(lambda t: '-' not in pro[t[0]][1].keys() and 'X' not in pro[t[0]][1].keys(), dtot_list))
        # gap또는 X가 없는 위치만 표시
        nogap_dtot_list = list(filter(lambda t: t[1] > ami_arr, nogap_dtot_list))  # 12개 초과의 mutaion을 가지는 dtot_list
        test_loca_list = list(map(lambda t: [t[0]], nogap_dtot_list))  # [[아미노산의 위치, motif 서열].. ]
        # 원하는 값에 대해서 최대 최소 찾기
        tar = ord(data_loc) - ord('A')
        tar_min = min(map(lambda t: t[1][tar], data))
        tar_max = max(map(lambda t: t[1][tar], data))

        num_data = len(data)
        num_motif = len(test_loca_list)
        train_data = np.zeros((num_data, num_motif))
        train_label = np.zeros(num_data)

        for ind, val in enumerate(test_loca_list):
            len_list = list(map(lambda t: len(t), pro[val[0]][1].values()))
            test_loca_list[ind].append(pro[val[0]][0][np.argmax(len_list)])

        if norm:
            for i, sdata in enumerate(data):
                for ind, val in enumerate(test_loca_list):
                    pro_loc = val[0]
                    pro_mot = val[1]
                    train_data[i][ind] = blo62((pro_mot, sdata[0][pro_loc]))  # 0 이상으로 변환
                tar_val = sdata[1][tar]
                tar_ind = (tar_val - tar_min) / (tar_max - tar_min)
                train_label[i] = tar_ind
        else:
            for i, sdata in enumerate(data):
                for ind, val in enumerate(test_loca_list):
                    pro_loc = val[0]
                    pro_mot = val[1]
                    train_data[i][ind] = blo62((pro_mot, sdata[0][pro_loc]))  # 0 이상으로 변환
                tar_val = sdata[1][tar]
                train_label[i] = tar_val

        return train_data, train_label, test_loca_list

    def get_reg_importance(self, x, y, loc, feet, tree, split_size=0.3,
                           val_mode=False, show_number=20, data_state=None, learn_state=None):
        """
        val_mode를 킨 경우에는 get_amino_loc 함수를 이용해서 위치를 파악해야 한다
        """
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import mean_squared_error
        from sklearn.ensemble import RandomForestRegressor

        import numpy as np

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=split_size, random_state=data_state)
        regr = RandomForestRegressor(max_depth=feet, n_estimators=tree, random_state=learn_state)
        regr.fit(x_train, y_train)
        prediction = regr.predict(x_test)
        print(mean_squared_error(y_test, prediction))
        feature_importance = regr.feature_importances_

        if not val_mode:
            import matplotlib.pyplot as plot

            self.view_importance(feature_importance, loc, show_number)

            plot.scatter(np.hstack((y_train, y_test)), np.hstack((regr.predict(x_train), regr.predict(x_test))),
                         color=['orange'] * len(x_train) + ['blue'] * len(x_test))
            plot.xlabel('True Values')
            plot.ylabel('Predictions')
            plot.axis('equal')
            plot.axis('square')
            plot.xlim([0, plot.xlim()[1]])
            plot.ylim([0, plot.ylim()[1]])
            _ = plot.plot([-100, 100], [-100, 100], color='black')
            plot.show()

        return feature_importance / feature_importance.max()


class RFI(RF):
    def __init__(self, floc, dloc, nfeet, ntree, loc=0):
        super().__init__(floc, dloc, loc)
        self.__nfeat = nfeet
        self.__ntree = ntree

    def get_reg_value(self, x, y, split_size=0.3, val_mode=False, data_state=None, learn_state=None):
        """
        val_mode를 킨 경우에는 z numpy 배열을 반환하고,
        val_mode를 끈 경우네는 (min estimator, min feature), z를 반환한다.
        """
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.metrics import mean_squared_error
        from sklearn.model_selection import train_test_split

        import numpy as np

        if learn_state is None:
            print('You are using iteration RF randomly!')

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=split_size, random_state=data_state)
        n_feat_list = np.arange(*self.__nfeat)
        n_tree_list = np.arange(*self.__ntree)
        z = np.zeros((len(n_feat_list), len(n_tree_list)))
        for idx, maxFeat in enumerate(n_feat_list):
            for jdx, iTrees in enumerate(n_tree_list):
                winerfmodel = RandomForestRegressor(n_estimators=iTrees, max_depth=None,
                                                    max_features=maxFeat, oob_score=False, n_jobs=-1,
                                                    random_state=learn_state)
                winerfmodel.fit(x_train, y_train)
                # 데이터 세트에 대한 MSE 누적
                prediction = winerfmodel.predict(x_test)
                z[idx][jdx] = mean_squared_error(y_test, prediction)

        if val_mode:
            return z
        else:
            self.view_reg3d(z)
            return self.get_reg_value_loc(z), z

    def get_reg_value_loc(self, z):
        from numpy import unravel_index

        import numpy as np

        n_feat_list, n_tree_list = np.arange(*self.__nfeat), np.arange(*self.__ntree)
        arr_loc = unravel_index(z.argmin(), z.shape)
        return n_feat_list[arr_loc[0]], n_tree_list[arr_loc[1]]

    def view_reg3d(self, z):
        from matplotlib import cm
        from matplotlib.ticker import LinearLocator

        import numpy as np
        import matplotlib.pyplot as plot

        fig, ax = plot.subplots(subplot_kw={"projection": "3d"})
        n_feat_list, n_tree_list = np.meshgrid(np.arange(*self.__nfeat), np.arange(*self.__ntree))
        surf = ax.plot_surface(n_feat_list, n_tree_list, np.transpose(z), cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)
        ax.set_zlim(np.min(z), np.max(z) * 1.05)
        ax.zaxis.set_major_locator(LinearLocator(10))

        fig.colorbar(surf, shrink=0.5, aspect=5)
        plot.show()
