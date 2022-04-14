from Bio.Align.Applications import ClustalOmegaCommandline
from prorf.rfunction import view_sequence

import os

cline = ClustalOmegaCommandline(infile='Data/gpdata.fasta',
                                outfile='Data/algpdata.fasta', verbose=True, force=True)
os.system(str(cline))

view_sequence('Data/algpdata.fasta')
