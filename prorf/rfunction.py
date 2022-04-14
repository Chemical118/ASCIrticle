def blo62(pair):
    """
    순서에 상관없이 matrix를 이용하도록 간단한 in을 이용해서 사용하는 함수
    pair은 2개의 tuple로 넣어주어야 한다
    """
    matrix = {('W', 'F'): 1, ('F', 'W'): 1, ('L', 'R'): -2, ('R', 'L'): -2, ('S', 'P'): -1, ('P', 'S'): -1, ('V', 'T'): 0, ('T', 'V'): 0, ('Q', 'Q'): 5, ('N', 'A'): -2, ('A', 'N'): -2, ('Z', 'Y'): -2, ('Y', 'Z'): -2, ('W', 'R'): -3, ('R', 'W'): -3, ('Q', 'A'): -1, ('A', 'Q'): -1, ('S', 'D'): 0, ('D', 'S'): 0, ('H', 'H'): 8, ('S', 'H'): -1, ('H', 'S'): -1, ('H', 'D'): -1, ('D', 'H'): -1, ('L', 'N'): -3, ('N', 'L'): -3, ('W', 'A'): -3, ('A', 'W'): -3, ('Y', 'M'): -1, ('M', 'Y'): -1, ('G', 'R'): -2, ('R', 'G'): -2, ('Y', 'I'): -1, ('I', 'Y'): -1, ('Y', 'E'): -2, ('E', 'Y'): -2, ('B', 'Y'): -3, ('Y', 'B'): -3, ('Y', 'A'): -2, ('A', 'Y'): -2, ('V', 'D'): -3, ('D', 'V'): -3, ('B', 'S'): 0, ('S', 'B'): 0, ('Y', 'Y'): 7, ('G', 'N'): 0, ('N', 'G'): 0, ('E', 'C'): -4, ('C', 'E'): -4, ('Y', 'Q'): -1, ('Q', 'Y'): -1, ('Z', 'Z'): 4, ('V', 'A'): 0, ('A', 'V'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('R', 'M'): -1, ('V', 'E'): -2, ('E', 'V'): -2, ('T', 'N'): 0, ('N', 'T'): 0, ('P', 'P'): 7, ('V', 'I'): 3, ('I', 'V'): 3, ('V', 'S'): -2, ('S', 'V'): -2, ('Z', 'P'): -1, ('P', 'Z'): -1, ('V', 'M'): 1, ('M', 'V'): 1, ('T', 'F'): -2, ('F', 'T'): -2, ('V', 'Q'): -2, ('Q', 'V'): -2, ('K', 'K'): 5, ('P', 'D'): -1, ('D', 'P'): -1, ('I', 'H'): -3, ('H', 'I'): -3, ('I', 'D'): -3, ('D', 'I'): -3, ('T', 'R'): -1, ('R', 'T'): -1, ('P', 'L'): -3, ('L', 'P'): -3, ('K', 'G'): -2, ('G', 'K'): -2, ('M', 'N'): -2, ('N', 'M'): -2, ('P', 'H'): -2, ('H', 'P'): -2, ('F', 'Q'): -3, ('Q', 'F'): -3, ('Z', 'G'): -2, ('G', 'Z'): -2, ('X', 'L'): -1, ('L', 'X'): -1, ('T', 'M'): -1, ('M', 'T'): -1, ('Z', 'C'): -3, ('C', 'Z'): -3, ('X', 'H'): -1, ('H', 'X'): -1, ('D', 'R'): -2, ('R', 'D'): -2, ('B', 'W'): -4, ('W', 'B'): -4, ('X', 'D'): -1, ('D', 'X'): -1, ('Z', 'K'): 1, ('K', 'Z'): 1, ('F', 'A'): -2, ('A', 'F'): -2, ('Z', 'W'): -3, ('W', 'Z'): -3, ('F', 'E'): -3, ('E', 'F'): -3, ('D', 'N'): 1, ('N', 'D'): 1, ('B', 'K'): 0, ('K', 'B'): 0, ('X', 'X'): -1, ('F', 'I'): 0, ('I', 'F'): 0, ('B', 'G'): -1, ('G', 'B'): -1, ('X', 'T'): 0, ('T', 'X'): 0, ('F', 'M'): 0, ('M', 'F'): 0, ('B', 'C'): -3, ('C', 'B'): -3, ('Z', 'I'): -3, ('I', 'Z'): -3, ('Z', 'V'): -2, ('V', 'Z'): -2, ('S', 'S'): 4, ('L', 'Q'): -2, ('Q', 'L'): -2, ('W', 'E'): -3, ('E', 'W'): -3, ('Q', 'R'): 1, ('R', 'Q'): 1, ('N', 'N'): 6, ('W', 'M'): -1, ('M', 'W'): -1, ('Q', 'C'): -3, ('C', 'Q'): -3, ('W', 'I'): -3, ('I', 'W'): -3, ('S', 'C'): -1, ('C', 'S'): -1, ('L', 'A'): -1, ('A', 'L'): -1, ('S', 'G'): 0, ('G', 'S'): 0, ('L', 'E'): -3, ('E', 'L'): -3, ('W', 'Q'): -2, ('Q', 'W'): -2, ('H', 'G'): -2, ('G', 'H'): -2, ('S', 'K'): 0, ('K', 'S'): 0, ('Q', 'N'): 0, ('N', 'Q'): 0, ('N', 'R'): 0, ('R', 'N'): 0, ('H', 'C'): -3, ('C', 'H'): -3, ('Y', 'N'): -2, ('N', 'Y'): -2, ('G', 'Q'): -2, ('Q', 'G'): -2, ('Y', 'F'): 3, ('F', 'Y'): 3, ('C', 'A'): 0, ('A', 'C'): 0, ('V', 'L'): 1, ('L', 'V'): 1, ('G', 'E'): -2, ('E', 'G'): -2, ('G', 'A'): 0, ('A', 'G'): 0, ('K', 'R'): 2, ('R', 'K'): 2, ('E', 'D'): 2, ('D', 'E'): 2, ('Y', 'R'): -2, ('R', 'Y'): -2, ('M', 'Q'): 0, ('Q', 'M'): 0, ('T', 'I'): -1, ('I', 'T'): -1, ('C', 'D'): -3, ('D', 'C'): -3, ('V', 'F'): -1, ('F', 'V'): -1, ('T', 'A'): 0, ('A', 'T'): 0, ('T', 'P'): -1, ('P', 'T'): -1, ('B', 'P'): -2, ('P', 'B'): -2, ('T', 'E'): -1, ('E', 'T'): -1, ('V', 'N'): -3, ('N', 'V'): -3, ('P', 'G'): -2, ('G', 'P'): -2, ('M', 'A'): -1, ('A', 'M'): -1, ('K', 'H'): -1, ('H', 'K'): -1, ('V', 'R'): -3, ('R', 'V'): -3, ('P', 'C'): -3, ('C', 'P'): -3, ('M', 'E'): -2, ('E', 'M'): -2, ('K', 'L'): -2, ('L', 'K'): -2, ('V', 'V'): 4, ('M', 'I'): 1, ('I', 'M'): 1, ('T', 'Q'): -1, ('Q', 'T'): -1, ('I', 'G'): -4, ('G', 'I'): -4, ('P', 'K'): -1, ('K', 'P'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('D', 'K'): -1, ('I', 'C'): -1, ('C', 'I'): -1, ('Z', 'D'): 1, ('D', 'Z'): 1, ('F', 'R'): -3, ('R', 'F'): -3, ('X', 'K'): -1, ('K', 'X'): -1, ('Q', 'D'): 0, ('D', 'Q'): 0, ('X', 'G'): -1, ('G', 'X'): -1, ('Z', 'L'): -3, ('L', 'Z'): -3, ('X', 'C'): -2, ('C', 'X'): -2, ('Z', 'H'): 0, ('H', 'Z'): 0, ('B', 'L'): -4, ('L', 'B'): -4, ('B', 'H'): 0, ('H', 'B'): 0, ('F', 'F'): 6, ('X', 'W'): -2, ('W', 'X'): -2, ('B', 'D'): 4, ('D', 'B'): 4, ('D', 'A'): -2, ('A', 'D'): -2, ('S', 'L'): -2, ('L', 'S'): -2, ('X', 'S'): 0, ('S', 'X'): 0, ('F', 'N'): -3, ('N', 'F'): -3, ('S', 'R'): -1, ('R', 'S'): -1, ('W', 'D'): -4, ('D', 'W'): -4, ('V', 'Y'): -1, ('Y', 'V'): -1, ('W', 'L'): -2, ('L', 'W'): -2, ('H', 'R'): 0, ('R', 'H'): 0, ('W', 'H'): -2, ('H', 'W'): -2, ('H', 'N'): 1, ('N', 'H'): 1, ('W', 'T'): -2, ('T', 'W'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('F', 'S'): -2, ('W', 'P'): -4, ('P', 'W'): -4, ('L', 'D'): -4, ('D', 'L'): -4, ('B', 'I'): -3, ('I', 'B'): -3, ('L', 'H'): -3, ('H', 'L'): -3, ('S', 'N'): 1, ('N', 'S'): 1, ('B', 'T'): -1, ('T', 'B'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('K', 'Y'): -2, ('E', 'Q'): 2, ('Q', 'E'): 2, ('Y', 'G'): -3, ('G', 'Y'): -3, ('Z', 'S'): 0, ('S', 'Z'): 0, ('Y', 'C'): -2, ('C', 'Y'): -2, ('G', 'D'): -1, ('D', 'G'): -1, ('B', 'V'): -3, ('V', 'B'): -3, ('E', 'A'): -1, ('A', 'E'): -1, ('Y', 'W'): 2, ('W', 'Y'): 2, ('E', 'E'): 5, ('Y', 'S'): -2, ('S', 'Y'): -2, ('C', 'N'): -3, ('N', 'C'): -3, ('V', 'C'): -1, ('C', 'V'): -1, ('T', 'H'): -2, ('H', 'T'): -2, ('P', 'R'): -2, ('R', 'P'): -2, ('V', 'G'): -3, ('G', 'V'): -3, ('T', 'L'): -1, ('L', 'T'): -1, ('V', 'K'): -2, ('K', 'V'): -2, ('K', 'Q'): 1, ('Q', 'K'): 1, ('R', 'A'): -1, ('A', 'R'): -1, ('I', 'R'): -3, ('R', 'I'): -3, ('T', 'D'): -1, ('D', 'T'): -1, ('P', 'F'): -4, ('F', 'P'): -4, ('I', 'N'): -3, ('N', 'I'): -3, ('K', 'I'): -3, ('I', 'K'): -3, ('M', 'D'): -3, ('D', 'M'): -3, ('V', 'W'): -3, ('W', 'V'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('H', 'M'): -2, ('P', 'N'): -2, ('N', 'P'): -2, ('K', 'A'): -1, ('A', 'K'): -1, ('M', 'L'): 2, ('L', 'M'): 2, ('K', 'E'): 1, ('E', 'K'): 1, ('Z', 'E'): 4, ('E', 'Z'): 4, ('X', 'N'): -1, ('N', 'X'): -1, ('Z', 'A'): -1, ('A', 'Z'): -1, ('Z', 'M'): -1, ('M', 'Z'): -1, ('X', 'F'): -1, ('F', 'X'): -1, ('K', 'C'): -3, ('C', 'K'): -3, ('B', 'Q'): 0, ('Q', 'B'): 0, ('X', 'B'): -1, ('B', 'X'): -1, ('B', 'M'): -3, ('M', 'B'): -3, ('F', 'C'): -2, ('C', 'F'): -2, ('Z', 'Q'): 3, ('Q', 'Z'): 3, ('X', 'Z'): -1, ('Z', 'X'): -1, ('F', 'G'): -3, ('G', 'F'): -3, ('B', 'E'): 1, ('E', 'B'): 1, ('X', 'V'): -1, ('V', 'X'): -1, ('F', 'K'): -3, ('K', 'F'): -3, ('B', 'A'): -2, ('A', 'B'): -2, ('X', 'R'): -1, ('R', 'X'): -1, ('D', 'D'): 6, ('W', 'G'): -2, ('G', 'W'): -2, ('Z', 'F'): -3, ('F', 'Z'): -3, ('S', 'Q'): 0, ('Q', 'S'): 0, ('W', 'C'): -2, ('C', 'W'): -2, ('W', 'K'): -3, ('K', 'W'): -3, ('H', 'Q'): 0, ('Q', 'H'): 0, ('L', 'C'): -1, ('C', 'L'): -1, ('W', 'N'): -4, ('N', 'W'): -4, ('S', 'A'): 1, ('A', 'S'): 1, ('L', 'G'): -4, ('G', 'L'): -4, ('W', 'S'): -3, ('S', 'W'): -3, ('S', 'E'): 0, ('E', 'S'): 0, ('H', 'E'): 0, ('E', 'H'): 0, ('S', 'I'): -2, ('I', 'S'): -2, ('H', 'A'): -2, ('A', 'H'): -2, ('S', 'M'): -1, ('M', 'S'): -1, ('Y', 'L'): -1, ('L', 'Y'): -1, ('Y', 'H'): 2, ('H', 'Y'): 2, ('Y', 'D'): -3, ('D', 'Y'): -3, ('E', 'R'): 0, ('R', 'E'): 0, ('X', 'P'): -2, ('P', 'X'): -2, ('G', 'G'): 6, ('G', 'C'): -3, ('C', 'G'): -3, ('E', 'N'): 0, ('N', 'E'): 0, ('Y', 'T'): -2, ('T', 'Y'): -2, ('Y', 'P'): -3, ('P', 'Y'): -3, ('T', 'K'): -1, ('K', 'T'): -1, ('A', 'A'): 4, ('P', 'Q'): -1, ('Q', 'P'): -1, ('T', 'C'): -1, ('C', 'T'): -1, ('V', 'H'): -3, ('H', 'V'): -3, ('T', 'G'): -2, ('G', 'T'): -2, ('I', 'Q'): -3, ('Q', 'I'): -3, ('Z', 'T'): -1, ('T', 'Z'): -1, ('C', 'R'): -3, ('R', 'C'): -3, ('V', 'P'): -2, ('P', 'V'): -2, ('P', 'E'): -1, ('E', 'P'): -1, ('M', 'C'): -1, ('C', 'M'): -1, ('K', 'N'): 0, ('N', 'K'): 0, ('I', 'I'): 4, ('P', 'A'): -1, ('A', 'P'): -1, ('M', 'G'): -3, ('G', 'M'): -3, ('T', 'S'): 1, ('S', 'T'): 1, ('I', 'E'): -3, ('E', 'I'): -3, ('P', 'M'): -2, ('M', 'P'): -2, ('M', 'K'): -1, ('K', 'M'): -1, ('I', 'A'): -1, ('A', 'I'): -1, ('P', 'I'): -3, ('I', 'P'): -3, ('R', 'R'): 5, ('X', 'M'): -1, ('M', 'X'): -1, ('L', 'I'): 2, ('I', 'L'): 2, ('X', 'I'): -1, ('I', 'X'): -1, ('Z', 'B'): 1, ('B', 'Z'): 1, ('X', 'E'): -1, ('E', 'X'): -1, ('Z', 'N'): 0, ('N', 'Z'): 0, ('X', 'A'): 0, ('A', 'X'): 0, ('B', 'R'): -1, ('R', 'B'): -1, ('B', 'N'): 3, ('N', 'B'): 3, ('F', 'D'): -3, ('D', 'F'): -3, ('X', 'Y'): -1, ('Y', 'X'): -1, ('Z', 'R'): 0, ('R', 'Z'): 0, ('F', 'H'): -1, ('H', 'F'): -1, ('B', 'F'): -3, ('F', 'B'): -3, ('F', 'L'): 0, ('L', 'F'): 0, ('X', 'Q'): -1, ('Q', 'X'): -1, ('B', 'B'): 4}
    return matrix[pair]


def view_sequence(floc, loc=0, typ='fasta', fontsize="9pt", plot_width=800):
    """Bokeh sequence alignment view
    https://dmnfarrell.github.io/bioinformatics/bokeh-sequence-aligner
    Edit by Chemical118"""
    from bokeh.plotting import figure, output_file, show
    from bokeh.models import ColumnDataSource, Range1d
    from bokeh.models.glyphs import Text, Rect
    from bokeh.layouts import gridplot
    from bokeh.core.properties import value
    from Bio import SeqIO

    import numpy as np

    clrs = {'E': 'red', 'D': 'red', 'P': 'orange', 'A': 'orange', 'V': 'orange', 'H': 'orange', 'M': 'orange',
            'L': 'orange', 'I': 'orange', 'G': 'orange', 'K': 'blue', 'R': 'blue', 'N': 'green', 'C': 'green',
            'T': 'green', 'Q': 'green', 'S': 'green', 'F': 'yellow', 'Y': 'yellow', 'W': 'yellow', '-': 'white',
            'X': 'white'}

    # make sequence and id lists from the aln object
    aln = list(SeqIO.parse(floc, typ))
    seqs = [rec.seq for rec in aln]
    ids = [rec.id for rec in aln]
    text = [it for s in list(seqs) for it in s]
    colors = [clrs[it] for it in text]
    n = len(seqs[0])
    s = len(seqs)
    # var = .4
    x = np.arange(1 + loc, n + 1 + loc)
    y = np.arange(0, s, 1)
    # creates a 2D grid of coords from the 1D arrays
    xx, yy = np.meshgrid(x, y)
    # flattens the arrays
    gx = xx.ravel()
    gy = yy.flatten()
    # use recty for rect coords with an offset
    recty = gy + .5
    # var = 1 / s
    # now we can create the ColumnDataSource with all the arrays
    source = ColumnDataSource(dict(x=gx, y=gy, recty=recty, text=text, colors=colors))
    plot_height = len(seqs) * 15 + 50
    x_range = Range1d(loc, n + loc + 1, bounds='auto')
    if n > 100:
        viewlen = 100
    else:
        viewlen = n
    # view_range is for the close up view
    view_range = (0 + loc, viewlen + loc)
    tools = "xpan, xwheel_zoom, reset, save"

    # entire sequence view (no text, with zoom)
    p = figure(title=None, plot_width=plot_width, plot_height=50,
               x_range=x_range, y_range=(0, s), tools=tools,
               min_border=0, toolbar_location='below')
    rects = Rect(x="x", y="recty", width=1, height=1, fill_color="colors",
                 line_color=None, fill_alpha=0.6)
    p.add_glyph(source, rects)
    p.yaxis.visible = False
    p.grid.visible = False

    # sequence text view with ability to scroll along x-axis
    p1 = figure(title=None, plot_width=plot_width, plot_height=plot_height,
                x_range=view_range, y_range=ids, tools="xpan,reset",
                min_border=0, toolbar_location='below')  # , lod_factor=1)
    glyph = Text(x="x", y="y", text="text", text_align='center', text_color="black",
                 text_font=value("arial"), text_font_size=fontsize)
    rects = Rect(x="x", y="recty", width=1, height=1, fill_color="colors",
                 line_color=None, fill_alpha=0.4)
    p1.add_glyph(source, glyph)
    p1.add_glyph(source, rects)

    p1.grid.visible = False
    p1.xaxis.major_label_text_font_style = "bold"
    p1.yaxis.minor_tick_line_width = 0
    p1.yaxis.major_tick_line_width = 0

    p = gridplot([[p], [p1]], toolbar_location='below')

    output_file('Data/View/' + floc.split('/')[-1].split('.')[0] + '.html')
    show(p)
