from toolbox import get_reg_importance, get_data

X, Y, L = get_data(12)
get_reg_importance(X, Y, L, 3, 300)
