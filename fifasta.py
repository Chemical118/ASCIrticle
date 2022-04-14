from dendropy.calculate import treemeasure
from prorf.rfclass import RF
from Bio import SeqIO
from Bio.Seq import Seq
from bidict import bidict

import dendropy as de
import numpy as np

R = RF('Data/algpdata.fasta', '')
R.view_sequence()
id_list = R.get_id_list()
bdict = bidict()
sdict = dict()

for ind, val in enumerate(id_list):
    bdict[val] = ind

for i in SeqIO.parse('Data/ealgpdata.fasta', 'fasta'):
    sdict[i.id] = str(i.seq)

tree = de.Tree.get_from_path('Data/Mega/ealtreedata.nwk', 'newick')
pdm = treemeasure.PatristicDistanceMatrix(tree)

dmat = np.full((len(id_list), len(id_list)), 10.0, dtype='float64')
for i, t1 in enumerate(tree.taxon_namespace):
    for t2 in tree.taxon_namespace[i + 1:]:
        t1l = t1.label.replace(' ', '_')
        t2l = t2.label.replace(' ', '_')
        dmat[bdict[t1l]][bdict[t2l]] = float(pdm(t1, t2))
        dmat[bdict[t2l]][bdict[t1l]] = float(pdm(t1, t2))

seq_list = []
for i in SeqIO.parse('Data/ealgpdata.fasta', 'fasta'):
    str_seq = str(i.seq)
    ls = len(str_seq)
    loc_list = [i for i in range(ls) if str_seq.find("-", i) == i]
    rloc_list = sorted(list(set(range(ls)) - set(loc_list)))
    st = rloc_list[0]
    nd = rloc_list[-1] + 1
    if st != 0 or nd != ls:
        clos_tar = bdict.inverse[np.argmin(dmat[bdict[i.id]])]
        print(i.id, clos_tar)
        if st != 0:
            str_seq = sdict[clos_tar][:st] + str_seq[st:]
        if nd != ls:
            str_seq = str_seq[:nd] + sdict[clos_tar][nd:]
    seq_list.append(str_seq)

cdata_list = []
for scord, seq in zip(SeqIO.parse('Data/gpdata.fasta', 'fasta'), seq_list):
    scord.seq = Seq(seq)
    cdata_list.append(scord)

SeqIO.write(cdata_list, 'Data/cgpdata.fasta', 'fasta')
