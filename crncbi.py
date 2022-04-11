from Bio import Entrez

import pandas as pd

Entrez.email = 'socialhomework209@gmail.com'
df = pd.read_excel('Data/data.xls')  # ['Spcies', 'Reference', 'NCBI No.']
df_list = df.values.tolist()

# asdas
for ind, val in enumerate(df_list):
    print(ind)
    handle = Entrez.efetch(db='protein', id=val[2], rettype='fasta', retmode='text')
    with open('Pdata/' + str(ind) + '.fasta', 'w') as f:
        f.write(handle.read())
    handle = Entrez.efetch(db='protein', id=val[2], rettype='gb', retmode='text')
    with open('Pdata/genprpt/' + str(ind) + '.gp', 'w') as f:
        f.write(handle.read())
as