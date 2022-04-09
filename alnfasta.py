from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import SeqIO
from viewer import view_alignment

import os

# # cline = ClustalOmegaCommandline(infile='Data/gpdata.fasta',
# #                                 outfile='Data/algpdata.fasta', verbose=True, force=True)
# os.system(str(cline))

aln = SeqIO.parse('Data/algpdata.fasta', 'fasta')
view_alignment(list(aln))
