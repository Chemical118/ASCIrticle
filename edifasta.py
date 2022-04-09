from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

parse = SeqIO.parse('Data/algpdata.fasta', 'fasta')
edit_list = []
for i in parse:
    edit_list.append(SeqRecord(seq=i.seq[28:489], id=i.id, description=''))

SeqIO.write(edit_list, 'Data/ealgpdata.fasta', 'fasta')
