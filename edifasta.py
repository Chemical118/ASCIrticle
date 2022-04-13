from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from toolbox import view_alignment

amino_loc = 28
amino_end_loc = 488

parse = SeqIO.parse('Data/algpdata.fasta', 'fasta')
edit_list = []
for i in parse:
    edit_list.append(SeqRecord(seq=i.seq[amino_loc:amino_end_loc + 1], id=i.id, description=''))

SeqIO.write(edit_list, 'Data/ealgpdata.fasta', 'fasta')

view_alignment('Data/ealgpdata.fasta')
