from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import numpy as np

import matplotlib.pyplot as plot
from matplotlib import cm
from matplotlib.ticker import LinearLocator

from toolbox import process, data_list, blo62
from random import shuffle

pros = process()
data = data_list()
pro = pros[0]

dtot_list = list(zip(pros[1], pros[2]))  # dtot_list : [(아미노산 위치, mutation 개수).. ]
nogap_dtot_list = list(filter(lambda t: '-' not in pro[t[0]][1].keys(), dtot_list))  # gap이 없는 위치만 표시
nogap_dtot_list = list(filter(lambda t: t[1] > 12, nogap_dtot_list))  # 12개 이상의 mutaion을 가지는 dtot_list
test_loca_list = list(map(lambda t: [t[0]], nogap_dtot_list))  # [[아미노산의 위치, motif 서열].. ]
# 원하는 값에 대해서 최대 최소 찾기
tar = 3
# check
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

print(len(test_loca_list))
for i, sdata in enumerate(data):
    for ind, val in enumerate(test_loca_list):
        pro_loc = val[0]
        pro_mot = val[1]
        train_data[i][ind] = blo62((pro_mot, sdata[0][pro_loc]))  # 0 이상으로 변환
    tar_val = sdata[1][tar]
    # tar_ind = (tar_val - tar_min) / (tar_max - tar_min)
    train_label[i] = tar_val / 100

X = train_data
Y = train_label
wineNames = np.array(list(map(lambda t: t[0] + 1, test_loca_list)))
xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size=0.3)
print(len(xTrain), len(xTest))
mseOos = []
nFeatList = np.arange(1, 6)
nTreeList = np.arange(50, 500, 10)
Z = np.zeros((len(nTreeList), len(nFeatList)))
for idx, maxFeat in enumerate(nFeatList):
    for jdx, iTrees in enumerate(nTreeList):
        depth = None
        # maxFeat = 5 #조정해볼 것
        wineRFModel = ensemble.RandomForestRegressor(n_estimators=iTrees,
                                                     max_depth=depth, max_features=maxFeat,
                                                     oob_score=False, n_jobs=-1)
        wineRFModel.fit(xTrain, yTrain)
        # 데이터 세트에 대한 MSE 누적
        prediction = wineRFModel.predict(xTest)
        Z[jdx][idx] = mean_squared_error(yTest, prediction)

fig, ax = plot.subplots(subplot_kw={"projection": "3d"})
nFeatList, nTreeList = np.meshgrid(nFeatList, nTreeList)
surf = ax.plot_surface(nFeatList, nTreeList, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(np.min(Z), np.max(Z) * 1.05)
ax.zaxis.set_major_locator(LinearLocator(10))

fig.colorbar(surf, shrink=0.5, aspect=5)
plot.show()

regr = RandomForestRegressor(max_depth=4,
                             n_estimators=300)
regr.fit(xTrain, yTrain)
prediction = regr.predict(xTest)
print(mean_squared_error(yTest, prediction))
featureImportance = regr.feature_importances_

# 가장 높은 중요도 기준으로 스케일링
featureImportance = featureImportance / featureImportance.max()
sorted_idx = np.argsort(featureImportance)
barPos = np.arange(sorted_idx.shape[0]) + .5
plot.barh(barPos, featureImportance[sorted_idx], align='center')
plot.yticks(barPos, wineNames[sorted_idx])
plot.xlabel('Variable Importance')
print()
plot.show()

plot.scatter(Y, regr.predict(X))
plot.xlabel('True Values')
plot.ylabel('Predictions')
plot.axis('equal')
plot.axis('square')
plot.xlim([0, plot.xlim()[1]])
plot.ylim([0, plot.ylim()[1]])
_ = plot.plot([-100, 100], [-100, 100])
plot.show()
