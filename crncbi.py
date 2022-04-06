from Bio import Entrez

import pandas as pd

Entrez.email = 'wowo0118@korea.ac.kr'
df = pd.read_excel('data.xls')
df_list = map(lambda t: t[0], df.values.tolist())

for i in df_list:
    handle = Entrez.esearch('protein', i + 'citrate synthase')
    t = Entrez.read(handle)
    print(t['IdList'])
    q = Entrez.efetch('protein', id=t['IdList'][0], rettypee='gb', retmode='text')
    print(q)
