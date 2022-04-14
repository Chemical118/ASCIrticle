# Confirm RF at constant condition
from prorf.rfclass import RF
R = RF('Data/rgpdata.fasta', 'Data/rdata.xls')
R.view_sequence()

X, Y, L = R.get_data(9, 'E')  # Excel data column
feat, tree, ran_state = 5, 300, 2022
FI = R.get_reg_importance(X, Y, L, feat, tree, show_number=25, val_mode=False, data_state=ran_state, learn_state=ran_state)
# val_mode is off, so they draw prediction-tree value plot and impotance plot

# To get amino loaction for get_amino_loc and sorted by amino index
for loc, im in sorted(list(zip(R.get_amino_loc(L), FI)), key=lambda t: t[0]):
    print("%d location Importance : %.4f" % (loc, im))
