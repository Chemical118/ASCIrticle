from toolbox import get_reg_value, get_data, view_reg3d

X, Y, L = get_data(12)
nFeet = (1, 3)
nTree = (50, 500, 100)
Z = get_reg_value(X, Y, nFeet, nTree, val=True)
view_reg3d(Z, nFeet, nTree)
