from toolbox import get_reg_importance, get_data, view_importance

X, Y, L = get_data(12)
feat, tree, ran_state = 3, 300, 2022
FI = get_reg_importance(X, Y, L, feat, tree, split_size=0.3, val_mode=True, r_state=ran_state)
for i in range(9):
    FI += get_reg_importance(X, Y, L, feat, tree, split_size=0.3, val_mode=True, r_state=ran_state)

view_importance(FI, L, show_number=20)
# Don't worry they automatically normalize the data
