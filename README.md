# ASCIrticle Project
#### Using Random Forest in enzyme for various variables

`ggcheck.py` : crawling google or ncbi to get protein data  
`crnbi.py` : get data from NCBI
`confasta.py` : gather .fasta file to one file  
`alnfasta.py` : align protein sequencr using clustal omega  
`fifasta.py` : fill unknown data using the tree  
`edifasta.py `: edit .fasta file by erasing gap (-)   
`prorf `: packakge for Random Forest
## Description
### `prorf.rfclass`
#### `RF` : Random Forest Class
+ `get_data` : return X, Y, L (location array) you must use .xls file and make index column
  + `__process`, `__data_list` : return various data
+ `get_id_list` : return data id list
+ `get_amino_loc` : using location array (at get_data[2]), return amino acid loaction array
+ `view_alignment` : call `prorf.rfunction.view_alignment`
#### `RFI` : Iteration Random Forest Class which inherit from `RF`
+ `get_reg_value` : RF at nfeat, ntree range return MSE arraay or MSE array and min loc tuple by val_mode on/off
+ `get_reg_value_loc` : using nfeat, ntree and MSE array return min loc tuple by val_mode on/off
+ `view_reg3d` : using nfeat, ntree and MSE array draw 3d distribution
+ `get_reg_importance` : RF at one condition return feature importance and variable importance, answer plpot when val_mode is off
+ `view_importace` : using feature importance array, draw variable importance plot

### `prorf.rfunction`
+ `blo62` : BLOSUM62 matrix
+ `view_alignment` : Using [Bokeh sequence aligner visualization program](https://dmnfarrell.github.io/bioinformatics/bokeh-sequence-aligner
), make protein sequence aligner

## Example
### Normal Random Forest
> Normal RF; `RF` use comfirm FR at constant condtion or guess which amino loaction is important

```python
# Confirm RF at constant condition
from prorf.rfclass import RF
R = RF('Data/rgpdata.fasta', 'Data/rdata.xls')
R.view_sequence()

X, Y, L = R.get_data(9, 'E')  # Excel data column
feat, tree, ran_state = 5, 300, 2022
FI = R.get_reg_importance(X, Y, L, feat, tree, split_size=0.3, show_number=25, val_mode=False, data_state=ran_state, learn_state=ran_state)
# val_mode is off, so they draw prediction-tree value plot and impotance plot
```

```python
# Confirm RF at constant condition
from prorf.rfclass import RF
R = RF('Data/cgpdata.fasta', 'Data/data.xls', 28)

X, Y, L = R.get_data(12, 'D')  # Excel data column
feat, tree, ran_state = 3, 300, 2022
FI = R.get_reg_importance(X, Y, L, feat, tree, split_size=0.3, show_number=25, val_mode=False, data_state=ran_state, learn_state=ran_state)
# val_mode is off, so they draw prediction-tree value plot and impotance plot

# To get amino loaction for get_amino_loc and sorted by amino index
for loc, im in sorted(list(zip(R.get_amino_loc(L), FI)), key=lambda t: t[0]):
    print("%d location Importance : %.4f" % (loc, im))
```

```python
# To get importace of amino location
from prorf.rfclass import RF
R = RF('Data/cgpdata.fasta', 'Data/data.xls', 28)

X, Y, L = R.get_data(12, 'D')  # Excel data column
feat, tree, ran_state = 3, 300, 2022
FI = R.get_reg_importance(X, Y, L, feat, tree, split_size=0.3, val_mode=True, learn_state=ran_state)
for i in range(9):
    FI += R.get_reg_importance(X, Y, L, feat, tree, split_size=0.3, val_mode=True, learn_state=ran_state)

R.view_importance(FI, L, show_number=20)
# Don't worry they automatically normalize the data
```
### Iteration Random Forest
> Iteration RF class; `RFI` use when we want to get the best condition

Be careful about randomness, always be aware of `data_state` and `learn_state`
```python
# Not Iteration
from prorf.rfclass import RFI
R = RFI('Data/cgpdata.fasta', 'Data/data.xls', (2, 5), (50, 500, 100), 28)

X, Y, L = R.get_data(12, 'D')  # Excel data column

MinL, Z = R.get_reg_value(X, Y, split_size=0.3, val_mode=False, learn_state=1945)
# When val_mode is off, you don't need to use draw function

print(*MinL)
```

```python
# Iteration
from prorf.rfclass import RFI
R = RFI('Data/cgpdata.fasta', 'Data/data.xls', (4, 7), (50, 500, 100), 28)

X, Y, L = R.get_data(12, 'D')  # Excel data column
ran_state = 2022

Z = R.get_reg_value(X, Y, split_size=0.3, val_mode=True, learn_state=ran_state)
for i in range(9):
  Z += R.get_reg_value(X, Y, split_size=0.3, val_mode=True, learn_state=ran_state)
# total 10 times iteration
# When val_mode is on, you need to use draw and location function

R.view_reg3d(Z)
# Don't worry they automatically normalize the data
print(*R.get_reg_value_loc(Z))
# Return tuple same as MinL (val_mode off)
```
## Import module
`biopython`
`numpy`
`bohek`
`pandas`
`bidict`
`matplotlib`
`sklearn`
`selenium`
`fake_useragent`
`webdriver_manager`
`dendropy`