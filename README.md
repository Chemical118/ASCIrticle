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
+ get_colors, view_alignment : Using [Bokeh sequence aligner visualization program](https://dmnfarrell.github.io/bioinformatics/bokeh-sequence-aligner
), make protein sequence aligner
+ get_id_list : return data id list

***
## Import module
+ Biopython
+ numpy
+ bokek
+ pandas
+ bidict
+ selenium
  + fake_useragent
  + webdriver_manager
+ dendropy