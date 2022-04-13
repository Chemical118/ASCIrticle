def blo62(pair):
    """
    순서에 상관없이 matrix를 이용하도록 간단한 in을 이용해서 사용하는 함수
    pair은 2개의 tuple로 넣어주어야 한다
    """
    matrix = {
        ("W", "F"): 1, ("L", "R"): -2, ("S", "P"): -1, ("V", "T"): 0,
        ("Q", "Q"): 5, ("N", "A"): -2, ("Z", "Y"): -2, ("W", "R"): -3,
        ("Q", "A"): -1, ("S", "D"): 0, ("H", "H"): 8, ("S", "H"): -1,
        ("H", "D"): -1, ("L", "N"): -3, ("W", "A"): -3, ("Y", "M"): -1,
        ("G", "R"): -2, ("Y", "I"): -1, ("Y", "E"): -2, ("B", "Y"): -3,
        ("Y", "A"): -2, ("V", "D"): -3, ("B", "S"): 0, ("Y", "Y"): 7,
        ("G", "N"): 0, ("E", "C"): -4, ("Y", "Q"): -1, ("Z", "Z"): 4,
        ("V", "A"): 0, ("C", "C"): 9, ("M", "R"): -1, ("V", "E"): -2,
        ("T", "N"): 0, ("P", "P"): 7, ("V", "I"): 3, ("V", "S"): -2,
        ("Z", "P"): -1, ("V", "M"): 1, ("T", "F"): -2, ("V", "Q"): -2,
        ("K", "K"): 5, ("P", "D"): -1, ("I", "H"): -3, ("I", "D"): -3,
        ("T", "R"): -1, ("P", "L"): -3, ("K", "G"): -2, ("M", "N"): -2,
        ("P", "H"): -2, ("F", "Q"): -3, ("Z", "G"): -2, ("X", "L"): -1,
        ("T", "M"): -1, ("Z", "C"): -3, ("X", "H"): -1, ("D", "R"): -2,
        ("B", "W"): -4, ("X", "D"): -1, ("Z", "K"): 1, ("F", "A"): -2,
        ("Z", "W"): -3, ("F", "E"): -3, ("D", "N"): 1, ("B", "K"): 0,
        ("X", "X"): -1, ("F", "I"): 0, ("B", "G"): -1, ("X", "T"): 0,
        ("F", "M"): 0, ("B", "C"): -3, ("Z", "I"): -3, ("Z", "V"): -2,
        ("S", "S"): 4, ("L", "Q"): -2, ("W", "E"): -3, ("Q", "R"): 1,
        ("N", "N"): 6, ("W", "M"): -1, ("Q", "C"): -3, ("W", "I"): -3,
        ("S", "C"): -1, ("L", "A"): -1, ("S", "G"): 0, ("L", "E"): -3,
        ("W", "Q"): -2, ("H", "G"): -2, ("S", "K"): 0, ("Q", "N"): 0,
        ("N", "R"): 0, ("H", "C"): -3, ("Y", "N"): -2, ("G", "Q"): -2,
        ("Y", "F"): 3, ("C", "A"): 0, ("V", "L"): 1, ("G", "E"): -2,
        ("G", "A"): 0, ("K", "R"): 2, ("E", "D"): 2, ("Y", "R"): -2,
        ("M", "Q"): 0, ("T", "I"): -1, ("C", "D"): -3, ("V", "F"): -1,
        ("T", "A"): 0, ("T", "P"): -1, ("B", "P"): -2, ("T", "E"): -1,
        ("V", "N"): -3, ("P", "G"): -2, ("M", "A"): -1, ("K", "H"): -1,
        ("V", "R"): -3, ("P", "C"): -3, ("M", "E"): -2, ("K", "L"): -2,
        ("V", "V"): 4, ("M", "I"): 1, ("T", "Q"): -1, ("I", "G"): -4,
        ("P", "K"): -1, ("M", "M"): 5, ("K", "D"): -1, ("I", "C"): -1,
        ("Z", "D"): 1, ("F", "R"): -3, ("X", "K"): -1, ("Q", "D"): 0,
        ("X", "G"): -1, ("Z", "L"): -3, ("X", "C"): -2, ("Z", "H"): 0,
        ("B", "L"): -4, ("B", "H"): 0, ("F", "F"): 6, ("X", "W"): -2,
        ("B", "D"): 4, ("D", "A"): -2, ("S", "L"): -2, ("X", "S"): 0,
        ("F", "N"): -3, ("S", "R"): -1, ("W", "D"): -4, ("V", "Y"): -1,
        ("W", "L"): -2, ("H", "R"): 0, ("W", "H"): -2, ("H", "N"): 1,
        ("W", "T"): -2, ("T", "T"): 5, ("S", "F"): -2, ("W", "P"): -4,
        ("L", "D"): -4, ("B", "I"): -3, ("L", "H"): -3, ("S", "N"): 1,
        ("B", "T"): -1, ("L", "L"): 4, ("Y", "K"): -2, ("E", "Q"): 2,
        ("Y", "G"): -3, ("Z", "S"): 0, ("Y", "C"): -2, ("G", "D"): -1,
        ("B", "V"): -3, ("E", "A"): -1, ("Y", "W"): 2, ("E", "E"): 5,
        ("Y", "S"): -2, ("C", "N"): -3, ("V", "C"): -1, ("T", "H"): -2,
        ("P", "R"): -2, ("V", "G"): -3, ("T", "L"): -1, ("V", "K"): -2,
        ("K", "Q"): 1, ("R", "A"): -1, ("I", "R"): -3, ("T", "D"): -1,
        ("P", "F"): -4, ("I", "N"): -3, ("K", "I"): -3, ("M", "D"): -3,
        ("V", "W"): -3, ("W", "W"): 11, ("M", "H"): -2, ("P", "N"): -2,
        ("K", "A"): -1, ("M", "L"): 2, ("K", "E"): 1, ("Z", "E"): 4,
        ("X", "N"): -1, ("Z", "A"): -1, ("Z", "M"): -1, ("X", "F"): -1,
        ("K", "C"): -3, ("B", "Q"): 0, ("X", "B"): -1, ("B", "M"): -3,
        ("F", "C"): -2, ("Z", "Q"): 3, ("X", "Z"): -1, ("F", "G"): -3,
        ("B", "E"): 1, ("X", "V"): -1, ("F", "K"): -3, ("B", "A"): -2,
        ("X", "R"): -1, ("D", "D"): 6, ("W", "G"): -2, ("Z", "F"): -3,
        ("S", "Q"): 0, ("W", "C"): -2, ("W", "K"): -3, ("H", "Q"): 0,
        ("L", "C"): -1, ("W", "N"): -4, ("S", "A"): 1, ("L", "G"): -4,
        ("W", "S"): -3, ("S", "E"): 0, ("H", "E"): 0, ("S", "I"): -2,
        ("H", "A"): -2, ("S", "M"): -1, ("Y", "L"): -1, ("Y", "H"): 2,
        ("Y", "D"): -3, ("E", "R"): 0, ("X", "P"): -2, ("G", "G"): 6,
        ("G", "C"): -3, ("E", "N"): 0, ("Y", "T"): -2, ("Y", "P"): -3,
        ("T", "K"): -1, ("A", "A"): 4, ("P", "Q"): -1, ("T", "C"): -1,
        ("V", "H"): -3, ("T", "G"): -2, ("I", "Q"): -3, ("Z", "T"): -1,
        ("C", "R"): -3, ("V", "P"): -2, ("P", "E"): -1, ("M", "C"): -1,
        ("K", "N"): 0, ("I", "I"): 4, ("P", "A"): -1, ("M", "G"): -3,
        ("T", "S"): 1, ("I", "E"): -3, ("P", "M"): -2, ("M", "K"): -1,
        ("I", "A"): -1, ("P", "I"): -3, ("R", "R"): 5, ("X", "M"): -1,
        ("L", "I"): 2, ("X", "I"): -1, ("Z", "B"): 1, ("X", "E"): -1,
        ("Z", "N"): 0, ("X", "A"): 0, ("B", "R"): -1, ("B", "N"): 3,
        ("F", "D"): -3, ("X", "Y"): -1, ("Z", "R"): 0, ("F", "H"): -1,
        ("B", "F"): -3, ("F", "L"): 0, ("X", "Q"): -1, ("B", "B"): 4
    }
    if pair in matrix:
        return matrix[pair]
    else:
        return matrix[pair[::-1]]


class RF:
    def __init__(self, dloc, loc=0):
        self.amino_loc = loc
        self.data_loc = dloc

    def get_id_list(self):
        from Bio import SeqIO
        return list(map(lambda t: t.id, SeqIO.parse(self.data_loc, 'fasta')))

    def __get_colors(self, seqs):
        """make colors for bases in sequence
        https://dmnfarrell.github.io/bioinformatics/bokeh-sequence-aligner
        Edit by Chemical118"""
        text = [it for s in list(seqs) for it in s]
        '''
        a = dict()
        for i in 'ED':
            a[i]='red'
        for i in 'PAVMLIGH':
            a[i]='orange'
        for i in 'KR':
            a[i]='blue'
        for i in 'NCTQS':
            a[i]='green'
        for i in 'FYW':
            a[i]='yellow'
        for i in '-X'
            a[i]='white'
        '''
        clrs = {'E': 'red', 'D': 'red', 'P': 'orange', 'A': 'orange', 'V': 'orange', 'H': 'orange', 'M': 'orange',
                'L': 'orange', 'I': 'orange', 'G': 'orange', 'K': 'blue', 'R': 'blue', 'N': 'green', 'C': 'green',
                'T': 'green', 'Q': 'green', 'S': 'green', 'F': 'yellow', 'Y': 'yellow', 'W': 'yellow', '-': 'white',
                'X': 'white'}
        colors = [clrs[it] for it in text]
        return colors

    def get_amino_loc(self, loca):
        import numpy as np
        return np.array(list(map(lambda t: t[0] + 1 + self.amino_loc, loca)))

    def view_alignment(self, loc, typ='fasta', fontsize="9pt", plot_width=800):
        """Bokeh sequence alignment view
        https://dmnfarrell.github.io/bioinformatics/bokeh-sequence-aligner
        Edit by Chemical118"""
        from bokeh.plotting import figure, output_file, show
        from bokeh.models import ColumnDataSource, Range1d
        from bokeh.models.glyphs import Text, Rect
        from bokeh.layouts import gridplot
        from bokeh.core.properties import value
        from Bio import SeqIO

        import numpy as np
        # make sequence and id lists from the aln object
        aln = list(SeqIO.parse(loc, typ))
        seqs = [rec.seq for rec in aln]
        ids = [rec.id for rec in aln]
        text = [it for s in list(seqs) for it in s]
        colors = self.__get_colors(seqs)
        n = len(seqs[0])
        s = len(seqs)
        # var = .4

        x = np.arange(1, n + 1)
        y = np.arange(0, s, 1)
        # creates a 2D grid of coords from the 1D arrays
        xx, yy = np.meshgrid(x, y)
        # flattens the arrays
        gx = xx.ravel()
        gy = yy.flatten()
        # use recty for rect coords with an offset
        recty = gy + .5
        # var = 1 / s
        # now we can create the ColumnDataSource with all the arrays
        source = ColumnDataSource(dict(x=gx, y=gy, recty=recty, text=text, colors=colors))
        plot_height = len(seqs) * 15 + 50
        x_range = Range1d(0, n + 1, bounds='auto')
        if n > 100:
            viewlen = 100
        else:
            viewlen = n
        # view_range is for the close up view
        view_range = (0, viewlen)
        tools = "xpan, xwheel_zoom, reset, save"

        # entire sequence view (no text, with zoom)
        p = figure(title=None, plot_width=plot_width, plot_height=50,
                   x_range=x_range, y_range=(0, s), tools=tools,
                   min_border=0, toolbar_location='below')
        rects = Rect(x="x", y="recty", width=1, height=1, fill_color="colors",
                     line_color=None, fill_alpha=0.6)
        p.add_glyph(source, rects)
        p.yaxis.visible = False
        p.grid.visible = False

        # sequence text view with ability to scroll along x-axis
        p1 = figure(title=None, plot_width=plot_width, plot_height=plot_height,
                    x_range=view_range, y_range=ids, tools="xpan,reset",
                    min_border=0, toolbar_location='below')  # , lod_factor=1)
        glyph = Text(x="x", y="y", text="text", text_align='center', text_color="black",
                     text_font=value("arial"), text_font_size=fontsize)
        rects = Rect(x="x", y="recty", width=1, height=1, fill_color="colors",
                     line_color=None, fill_alpha=0.4)
        p1.add_glyph(source, glyph)
        p1.add_glyph(source, rects)

        p1.grid.visible = False
        p1.xaxis.major_label_text_font_style = "bold"
        p1.yaxis.minor_tick_line_width = 0
        p1.yaxis.major_tick_line_width = 0

        p = gridplot([[p], [p1]], toolbar_location='below')

        output_file('Data/View/' + loc.split('/')[-1].split('.')[0] + '.html')
        show(p)

    def view_reg3d(self, z, nfeat, ntree):
        from matplotlib import cm
        from matplotlib.ticker import LinearLocator

        import numpy as np
        import matplotlib.pyplot as plot

        fig, ax = plot.subplots(subplot_kw={"projection": "3d"})
        n_feat_list, n_tree_list = np.meshgrid(np.arange(*nfeat), np.arange(*ntree))
        surf = ax.plot_surface(n_feat_list, n_tree_list, np.transpose(z), cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)
        ax.set_zlim(np.min(z), np.max(z) * 1.05)
        ax.zaxis.set_major_locator(LinearLocator(10))

        fig.colorbar(surf, shrink=0.5, aspect=5)
        plot.show()

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
        df = pd.read_excel('Data/data.xls')
        df_list = df.values.tolist()
        df_list = list(map(lambda te: [*te[::-1]], enumerate(df_list)))
        for ind, val in enumerate(SeqIO.parse(self.data_loc, 'fasta')):
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

    def get_data(self, ami_arr=12, norm=False):
        from random import shuffle

        import numpy as np
        pros = self.__process()
        data = self.__data_list()
        pro = pros[0]

        dtot_list = list(zip(pros[1], pros[2]))  # dtot_list : [(아미노산 위치, mutation 개수).. ]
        nogap_dtot_list = \
            list(filter(lambda t: '-' not in pro[t[0]][1].keys() and 'X' not in pro[t[0]][1].keys(), dtot_list))
        # gap또는 X가 없는 위치만 표시
        nogap_dtot_list = list(filter(lambda t: t[1] > ami_arr, nogap_dtot_list))  # 12개 이상의 mutaion을 가지는 dtot_list
        test_loca_list = list(map(lambda t: [t[0]], nogap_dtot_list))  # [[아미노산의 위치, motif 서열].. ]
        # 원하는 값에 대해서 최대 최소 찾기
        tar = 3
        data.sort(key=lambda t: -t[1][tar])
        # data = data[1:]
        shuffle(data)
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
                train_label[i] = tar_val / 100

        return train_data, train_label, test_loca_list

    def get_reg_value(self, x, y, nfeat, ntree, split_size=0.3, val_mode=False, r_state=None):
        """
        val_mode를 킨 경우에는 z numpy 배열을 반환하고,
        val_mode를 끈 경우네는 (min estimator, min feature), z를 반환한다.
        """
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.metrics import mean_squared_error
        from sklearn.model_selection import train_test_split

        import numpy as np

        if r_state is None:
            print('You are using iteration RF randomly!')

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=split_size)
        n_feat_list = np.arange(*nfeat)
        n_tree_list = np.arange(*ntree)
        z = np.zeros((len(n_feat_list), len(n_tree_list)))
        for idx, maxFeat in enumerate(n_feat_list):
            for jdx, iTrees in enumerate(n_tree_list):
                depth = None
                winerfmodel = RandomForestRegressor(n_estimators=iTrees, max_depth=depth,
                                                    max_features=maxFeat, oob_score=False, n_jobs=-1,
                                                    random_state=r_state)
                winerfmodel.fit(x_train, y_train)
                # 데이터 세트에 대한 MSE 누적
                prediction = winerfmodel.predict(x_test)
                z[idx][jdx] = mean_squared_error(y_test, prediction)

        if val_mode:
            return z
        else:
            self.view_reg3d(z, nfeat, ntree)
            return self.get_reg_value_loc(z, nfeat, ntree), z

    def get_reg_value_loc(self, z, nfeat, ntree):
        from numpy import unravel_index

        import numpy as np

        n_feat_list, n_tree_list = np.arange(*nfeat), np.arange(*ntree)
        arr_loc = unravel_index(z.argmin(), z.shape)
        return n_feat_list[arr_loc[0]], n_tree_list[arr_loc[1]]

    def get_reg_importance(self, x, y, loc, feet, tree, split_size=0.3, val_mode=False, show_number=20, r_state=None):
        """
        val_mode를 킨 경우에는 get_amino_loc 함수를 이용해서 위치를 파악해야 한다
        """
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import mean_squared_error
        from sklearn.ensemble import RandomForestRegressor

        import numpy as np

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=split_size)
        regr = RandomForestRegressor(max_depth=feet, n_estimators=tree, random_state=r_state)
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
