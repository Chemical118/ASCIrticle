from Bio import SeqIO

import pandas as pd

df = pd.read_excel('Data/data.xls')  # ['Spcies', 'Reference', 'NCBI No.']
df_list = df.values.tolist()

conb_list = []
for i in range(len(df_list)):
    conb_list.append(SeqIO.read('Pdata/' + str(i) + '.fasta', 'fasta'))

SeqIO.write(conb_list, 'Data/gpdata.fasta', 'fasta')
