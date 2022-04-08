from Bio import SeqIO

conb_list = []
for i in range(31):
    conb_list.append(SeqIO.read('Pdata/' + str(i) + '.fasta', 'fasta'))

SeqIO.write(conb_list, 'Data/gpdata.fasta', 'fasta')
