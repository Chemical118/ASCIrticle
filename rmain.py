from toolbox import get_reg_value, get_data, view_reg3d

X, Y, L = get_data(12)
nTree, nFeat = (1, 3), (50, 500, 100)

MinL, Z = get_reg_value(X, Y, nTree, nFeat, split_size=0.3, val_mode=False, r_state=1945)

view_reg3d(Z, nTree, nFeat)

print(*MinL)
