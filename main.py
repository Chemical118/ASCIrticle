# To get importace of amino location
from prorf.rfclass import RF
R = RF('Data/cgpdata.fasta', 28)

X, Y, L = R.get_data(12)
feat, tree, ran_state = 3, 300, 2022
FI = R.get_reg_importance(X, Y, L, feat, tree, split_size=0.3, val_mode=True, r_state=ran_state)
for i in range(9):
    FI += R.get_reg_importance(X, Y, L, feat, tree, split_size=0.3, val_mode=True, r_state=ran_state)

R.view_importance(FI, L, show_number=20)
# Don't worry they automatically normalize the data