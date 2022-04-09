******************************************************************************

	        CLUSTAL X Multiple Sequence Alignment Program
                         (version 1.81, March 2000)

******************************************************************************

This README contains notes on version CHANGES and help with INSTALLATION

Clustal X provides a new window-based user interface to the Clustal W multiple
alignment program. It uses the Vibrant multi-platform user interface
development library, developed by the National Center for Biotechnology
Information (Bldg 38A, NIH 8600 Rockville Pike,Bethesda, MD 20894) as part of
their NCBI SOFTWARE DEVELOPEMENT TOOLKIT. The toolkit is available by
anonymous ftp from ncbi.nlm.nih.gov

Please e-mail bug reports/complaints/suggestions (polite if possible) to
	   Julie Thompson at julie@igbmc.u-strasbg.fr
	or Toby Gibson at gibson@embl-heidelberg.de
 
 
******************************************************************************

            POLICY ON COMMERCIAL DISTRIBUTION OF CLUSTAL W and X

Clustal W and X are freely available to the user community. However, Clustal W
is increasingly being distributed as part of commercial sequence analysis
packages. To help us safeguard future maintenance and development, commercial
distributors of Clustal X must take out a non-exclusive licence. Anyone
wishing to commercially distribute version 1.81 of Clustal X should contact the
authors unless they have previously taken out a licence. 

******************************************************************************

Changes since CLUSTAL X Version 1.8
-----------------------------------

1. ClustalX now returns error codes for some common errors when exiting. This
may be useful for people who run clustalx automatically from within a script.
Error codes are:
        1       bad command line option
        2       cannot open sequence file
        3       wrong format in sequence file
        4       sequence file contains only 1 sequence (for multiple alignments)

2. Alignments can now be saved in Nexus format, for compatibility with PAUP,
MacClade etc. For a description of the Nexus format, see:
Maddison, D. R., D. L. Swofford and W. P. Maddison.  1997.
NEXUS: an extensible file format for systematic information.
Systematic Biology 46:590-621.

3. Phylogenetic trees can also be saved in nexus format.

4. A bug causing ClustalX to crash during cut-and-paste operations has been fixed.

5. A bug on PC systems, causing an error message when writing to files with
space characters in the filename has been fixed.

6. The Quality Curve is now displayed as a bar chart, instead of a line plot.
(Thanks to Michele Clamp, michele@ebi.ac.uk, who used this format in the JalView
editor.)

7. A bug in the 'Save Profile' option, causing the default profile filename to
be lost has been fixed.

8. A ClustalX icon has been designed for MAC and PC systems.


Changes since CLUSTAL X Version 1.65b
-------------------------------------

1. Some work has been done to automatically select the optimal parameters
depending on the set of sequences to be aligned. The Gonnet series of residue
comparison matrices are now used by default. The Blosum series remains as an
option. The default gap extension penalty for proteins has been changed to 0.2
(was 0.05).The 'delay divergent sequences' option has been changed to 30%
residue identity (was 40%).

2. The default parameters used when the 'Negative matrix' option is selected
have been optimised. This option may help when the sequences to be aligned are
not superposable over their whole lengths (e.g. in the presence of N/C terminal
extensions).

3. An option has been added to save the quality scores displayed underneath the
sequence window to a text file.

4. The 'Hide Low-scoring segments' option has been moved from the Low-scoring
parameter window to the Quality menu, and has been changed to 'Show Low-scoring
segments'.

5. An option has been added to allow the user to search for a string in the
sequences.

6. An option has been added to the postscript output to print on US Letter size
paper.

7. A bug in the display of the message at the bottom of the window causing the
text to disappear when the window was resized has been fixed.

8. The font for the Help window as been changed to Courier.

9. A bug in the calculation of phylogenetic trees for 2 sequences has been
fixed.

10. A command line option has been added to turn off the sequence weighting
calculation.

11. The phylogenetic tree calculation now ignores any ambiguity codes in the
sequences.

12.  A bug in the memory access during the calculation of profiles has been
fixed. (Thanks to Haruna Cofer at SGI).

13. A bug has been fixed in the 'transition weight' option for nucleic acid
sequences. (Thanks to Chanan Rubin at Compugen).

14. An option has been added to allow the user to read in a series of residue
comparison matrices from a file.

15. The MSF output file format has been changed. The sequence weights
calculated by ClustalX are now included in the header. 

16. Two bugs in the FAST/APPROXIMATE pairwise alignments have been fixed. One
involved the alignment of new sequences to an existing profile using the fast
pairwise alignment option; the second was caused by changing the default
options for the fast pairwise alignments.

17. A bug in the alignment of a small number of sequences has been fixed.
Previously a Guide Tree was not calculated for less than 4 sequences.

18. Several bugs affecting use of secondary structure masks in Clustal X (but
not in Clustal W) have been fixed. 


Changes since Version 1.5b
--------------------------

1. The window displayed under MS Windows has previously been a fixed size. The
window can now be resized by dragging the window frame.

2. An option has been added to read in a series of comparison matrices from a
file. This option is only applicable for protein sequences. For details of
the file format, see the on-line documentation.

3. A new DNA comparison matrix has been added. This is the default scoring 
matrix used by BESTFIT for the comparison of nucleic acid sequences. X's and N's
are treated as matches to any IUB ambiguity symbol. All matches score 1.9; all
mismatches for IUB symbols score 0.
The previous system used by ClustalW, in which matches score 1.0 and mismatches
score 0 remains as an option. All matches for IUB symbols will also score 0.

4. You can now read a comparison matrix for DNA sequences from a file. The
matrix file should be in the same format as for the Blast program.

5. The 'Reset gaps before alignment' has been changed to 'Reset new gaps
before alignments'. A new option 'Reset ALL gaps before alignment' has been
added.
RESET NEW GAPS BEFORE ALIGNMENT will remove any new gaps introduced into the
sequences during multiple alignment if you wish to change the parameters and
try again.
RESET ALL GAPS BEFORE ALIGNMENT will remove all gaps in the sequences including
gaps which were read in from the sequence input file. 
 
6. The 'Realign Residue Range' option has been changed. By default, gap
opening and extension penalties are now applied to the ends of the alignment
range in order to penalise terminal gaps. If the REALIGN SEGMENT END GAP
PENALTIES option is switched off, gaps can be introduced at the ends of the
residue range at no cost.

7. The MSF output file format has been changed. The sequence weights calculated
by ClustalX are now included in the header.

8. Two bugs in the FAST/APPROXIMATE pairwise alignments have been fixed. One
involved the alignment of new sequences to an existing profile using the
fast pairwise alignment option; the second was caused by changing the default
options for the fast pairwise alignments.

9. A bug in the postscript output file has been fixed. The residue numbers
printed at the right hand side of the alignment were not always correct.

10. A bug in the alignment of a small number of sequences has been fixed.
Previously a Guide Tree was not calculated for less than 4 sequences.

11. A bug which occurred after frequent cut-and-paste operations has been
fixed.

12. A new file called clustalx.html contains an html'ised version of the
on-line help. The file can be viewed using a World Wide Web viewer, such as
Netscape.


New Features since ClustalW
---------------------------

1. A subset of sequences in an alignment may be selected and realigned to a
profile made from the unselected sequences. This may be useful when trying to
align very divergent sequences which have been badly aligned in the initial
full multiple alignment.


2. A range of the sequence alignment can be selected for realignment. A new
phylogenetic guide tree is built based only on the residue range selected.
The selected residues are then aligned, and pasted back into the full sequence
alignment. This may be useful for aligning small sections of the alignment
which have been badly aligned in the full sequence alignment, or which have a
very different guide tree structure from the tree built using the full
sequences.


3. Clustal X provides a versatile coloring scheme for the sequence alignment
display. The sequences (or profiles) are colored automatically, when they are
loaded. Sequences can be colored either by assigning a color to specific
residues, or on the basis of an alignment consensus. In the latter case,
the alignment consensus is calculated automatically, and the residues in each
column are colored according to the consensus character assigned to the column.
In this way, for example, conserved hydrophylic or hydrophobic positions can
be highlighted.


4. An 'Alignment Quality Score' is plotted below the alignment. This is an
estimate of the conservation of each column in the alignment. Highly conserved
columns will have a high quality score, less conserved positions will be
marked by a low score.


5. 'Exceptional' residues in the alignment that cause the low quality scores
described above, can be highlighted. These can be expected to occur at a
moderate frequency in all the sequences because of their steady divergence
due to the natural processes of evolution. However, clustering of highlighted
residues is a strong indication of misalignment.
Occasionally, highlighted residues may also point to regions of some biological
significance.

6. Low-scoring segments in the alignment can be highlighted. The segments are
defined as those regions which score negatively in a forward and backward
summation of the alignment profile scores. See the online help for more
details.

7. The new GCG9 MSF,RSF formats are now recognised as input formats for
clustalx.  The alignments cannot be written out in these formats however.

The code has been tested on UNIX (SGI, SUN, DIGITAL) and Macintosh. Compiled
executables are provided for these systems. If you wish to recompile the
source files, you will first need to install the NCBI toolkit on your machine.
Then, to compile the program on UNIX, edit the makefile to point to your NCBI
include and library files, and type:

     make -f makefile.sun
or   make -f makefile.sgi
or   make -f makefile.osf


To run the program, type clustalx. A window is displayed with a pull-down menu
bar which allow all functions to be selected and all alignment parameters
may be modified, if desired.


Documentation for ClustalW (clustalw.doc) is included in the directory. Online
help is also available for most options of Clustal X by selecting HELP from
the menu bar.

Help is also available on the WWW at

www-igbmc.u-strasbg.fr/BioInfo/ClustalX/
www-igbmc.u-strasbg.fr/BioInfo/ClustalW/
www.U.arizona.edu/~schluter/ClustalW/index.html


INSTALLATION    (for Unix, PC and MAC)
------------

UNIX
----

Executables are provided in the appropriate archives for Digital UNIX 4.0 on
Alphas, Sun OS 5.6, Silicon Graphics IRIX 6.2 and LINUX (libc6 must be
installed). If you wish to run on another platform, you will need to recompile
Clustal X for yourself.

The executable file clustalx should be copied to one of the directories
specified in your PATH environment variable. The files called *.par and
clustalx_help should also be copied to the same directory.

Recompiling ClustalX:

First of all, you need the NCBI Vibrant toolkit installed on your machine. If
this is not already done, you can get the toolkit by anonymous ftp to
ncbi.nlm.nih.gov.
You should then copy one of the makefiles supplied in the unix archives to
'makefile' and edit it, changing the NCBI_INC and NCBI_LIB paths for your
system.

You make the program with:
make -f makefile

This produces the executable file clustalx. You can then proceed with the 
installation as described above.


MS WINDOWS
----------

We supply an executable file (clustalx.exe) which will run under MS Windows 
(32 bit). The directory containing the executable (plus the files named *.par,
and clustalx.hlp) should be added to your path defined in the autoexec.bat
file.


Recompiling ClustalX:

First of all, you need the NCBI Vibrant toolkit installed on your machine. If
this is not already done, you can get the toolkit by anonymous ftp to
ncbi.nlm.nih.gov.

A makefile is supplied which can be used as a guide for recompiling the
ClustalX source code. You will need to edit it for your system. In 
particular the NCBI_INC and NCBI_LIB paths should point to your installation.


MAC
---

An executable program called clustalx is supplied for Power Macintoshes.
For 68K machines, you will need to recompile the code yourself. The 
program may need up to 10m of memory to run depending on the number and
length of your sequences. The memory allocation can be adjusted with the
Get Info (%I) command from the Finder if you have problems. Just double click 
the executable file name or icon and off you go (we hope). The files *.par and
clustalx_help should be stored in the same directory as the clustalx program.

Recompiling ClustalX:

First of all, you need the NCBI Vibrant toolkit installed on your machine. If
this is not already done, you can get the toolkit by anonymous ftp to
ncbi.nlm.nih.gov.

We used the Metroworks Codewarrior C compiler to compile the ClustalX files,
but another ANSI C compiler should work. You need to compile all the *.c
files supplied in the archive, then link them together with the NCBI Toolkit
libraries 'ncbi' and 'vibrant'.


                            CLUSTAL REFERENCES
                            ------------------

Details of algorithms, implementation and useful tips on usage of Clustal
programs can be found in the following publications:

Jeanmougin,F., Thompson,J.D., Gouy,M., Higgins,D.G. and Gibson,T.J. (1998)
Multiple sequence alignment with Clustal X. Trends Biochem Sci, 23, 403-5.

Thompson,J.D., Gibson,T.J., Plewniak,F., Jeanmougin,F. and Higgins,D.G. (1997)
The ClustalX windows interface: flexible strategies for multiple sequence 
alignment aided by quality analysis tools. Nucleic Acids Research, 24:4876-4882.

Higgins, D. G., Thompson, J. D. and Gibson, T. J. (1996) Using CLUSTAL for
multiple sequence alignments. Methods Enzymol., 266, 383-402.

Thompson, J.D., Higgins, D.G. and Gibson, T.J. (1994) CLUSTAL W: improving the
sensitivity of progressive multiple sequence alignment through sequence
weighting, positions-specific gap penalties and weight matrix choice.  Nucleic
Acids Research, 22:4673-4680.

Higgins,D.G., Bleasby,A.J. and Fuchs,R. (1992) CLUSTAL V: improved software for
multiple sequence alignment. CABIOS 8,189-191.

Higgins,D.G. and Sharp,P.M. (1989) Fast and sensitive multiple sequence
alignments on a microcomputer. CABIOS 5,151-153.

Higgins,D.G. and Sharp,P.M. (1988) CLUSTAL: a package for performing multiple
sequence alignment on a microcomputer. Gene 73,237-244.

