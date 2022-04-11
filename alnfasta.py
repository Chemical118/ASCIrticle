from Bio.Align.Applications import ClustalOmegaCommandline
from toolbox import view_alignment

import os

cline = ClustalOmegaCommandline(infile='Data/gpdata.fasta',
                                outfile='Data/algpdata.fasta', verbose=True, force=True)
os.system(str(cline))

view_alignment('Data/algpdata.fasta')
