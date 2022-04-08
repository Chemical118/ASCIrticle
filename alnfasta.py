from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import SeqIO
from viewer import view_alignment

import os

cline = ClustalOmegaCommandline(infile='Data/gpdata.fasta',
                                outfile='Data/alngpdata.fasta',
                                guidetree_out='Data/Tree/gpdata.dnd', verbose=True, auto=True, force=True)

os.system(str(cline))
aln = SeqIO.parse('Data/alngpdata.fasta', 'fasta')
view_alignment(list(aln))
