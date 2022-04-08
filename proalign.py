from Bio import AlignIO

align = AlignIO.read('Data/gpdata.aln', 'clustal')
for i in align:
    t=i
    print(i)