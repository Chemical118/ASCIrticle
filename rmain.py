from toolbox import get_reg_value, get_data, view_reg3d, get_reg_value_loc

nFeat, nTree = (4, 7), (50, 500, 100)
X, Y, L = get_data(12)

Z = get_reg_value(X, Y, nFeat, nTree, split_size=0.3, val_mode=True, r_state=2022)
for i in range(4):
    Z += get_reg_value(X, Y, nFeat, nTree, split_size=0.3, val_mode=True, r_state=2022)

view_reg3d(Z, nFeat, nTree)
print(*get_reg_value_loc(Z, nFeat, nTree))
