# ASCIrticle Project
Using Random Forest in citrate synthase activity in heart muscle

***
ggcheck.py : crawling google or ncbi to get protein data  
crnbi.py : get data from NCBI
confasta.py : gather .fasta file to one file  
alnfasta.py : align protein sequencr using clustal omega  
fifasta.py : fill unknown data using the tree  
edifasta.py : edit .fasta file by erasing gap (-)   
toolbox.py : having useful function
#### &lt;Global variable&gt;
+ 
#### &lt;Visualization&gt;
+ get_colors, view_alignment : Using [Bokeh sequence aligner visualization program](https://dmnfarrell.github.io/bioinformatics/bokeh-sequence-aligner
), make protein sequence aligner
#### &lt;Random Forest Data processing Function&gt;
+ blo62 : BLOSUM62 matrix (by BioinformaticsProject)
+ get_data : return X, Y, L (location array)
  + process, data_list : return various data (by BioinformaticsProject, Don't use these function directly, please use get_data)
+ get_id_list : return data id list
+ get_amino_loc : using location array (at get_data[2]), return amino acid loaction array
#### &lt;Iteration Random Forest Fuction&gt;
+ get_reg_value : RF at nfeat, ntree range return MSE arraay or MSE array and min loc tuple by val_mode on/off
+ get_reg_value_loc : using nfeat, ntree and MSE array return min loc tuple by val_mode on/off
+ view_reg3d : using nfeat, ntree and MSE array draw 3d distribution
#### &lt;Importance Random Forest Fuction&gt;
+ get_reg_importance : RF at one condition return feature importance and variable importance, answer plpot when val_mode is off
+ view_importace : using feature importance array, draw variable importance plot
***
## Example
### Iteration Random Forest
> Iteration RF function use when we want to get the best condition

Be careful, when you not select random state RF will be random!
```python
# Not Iteration
from toolbox import get_reg_value, get_data

nFeat, nTree = (4, 7), (50, 500, 100)
X, Y, L = get_data(12)

MinL, Z = get_reg_value(X, Y, nFeat, nTree, split_size=0.3, val_mode=False, r_state=1945)
# When val_mode is off, you don't need to use draw function

print(*MinL)
```

```python
# Iteration
from toolbox import get_reg_value, get_data, view_reg3d, get_reg_value_loc

nFeat, nTree = (4, 7), (50, 500, 100)
X, Y, L = get_data(12)
ran_state = 2022

Z = get_reg_value(X, Y, nFeat, nTree, split_size=0.3, val_mode=True, r_state=ran_state)
for i in range(9):
  Z += get_reg_value(X, Y, nFeat, nTree, split_size=0.3, val_mode=True, r_state=ran_state)
# total 10 times iteration
# When val_mode is on, you need to use draw and location function

view_reg3d(Z, nFeat, nTree)
# Don't worry they automatically normalize the data
print(*get_reg_value_loc(Z, nFeat, nTree))
# Return tuple same as MinL (val_mode off)
```
### Importance Random Forest
> Importance RF use comfirm FR at constant condtion or guess which amino loaction is important

```python
# Confirm RF at constant condition
from toolbox import get_reg_importance, get_data, get_amino_loc

X, Y, L = get_data(12)
feat, tree = 3, 300
FI = get_reg_importance(X, Y, L, feat, tree, split_size=0.3, show_number=25, val_mode=False)
# val_mode is off, so they draw prediction-tree value plot and impotance plot

# To get amino loaction for get_amino_loc and sorted by amino index
for loc, im in sorted(list(zip(get_amino_loc(L), FI)), key=lambda t: t[0]):
    print("%d location Importance : %.4f" % (loc, im))
```
```python
# To get importace of amino location
from toolbox import get_reg_importance, get_data, view_importance

X, Y, L = get_data(12)
feat, tree, ran_state = 3, 300, 2022
FI = get_reg_importance(X, Y, L, feat, tree, split_size=0.3, val_mode=True, r_state=ran_state)
for i in range(9):
    FI += get_reg_importance(X, Y, L, feat, tree, split_size=0.3, val_mode=True, r_state=ran_state)

view_importance(FI, L, show_number=20)
# Don't worry they automatically normalize the data
```
***
## Import module
+ biopython
+ numpy
+ bokek
+ pandas
+ bidict
+ matplotlib
+ sklearn
+ selenium
  + fake_useragent
  + webdriver_manager
+ dendropy