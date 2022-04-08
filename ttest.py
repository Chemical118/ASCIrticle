from viewer import view_alignment
from Bio import SeqIO

aln = SeqIO.parse('Data/alngpdata.fasta', 'fasta')
view_alignment(list(aln))