def get_id_list():
    # from Bio import SeqIO
    # return list(map(lambda t: t.id, SeqIO.parse('Data/gpdata.fasta', 'fasta')))
    return ['XP_042569431.1', 'AIT82982.1', 'XP_030208401.1', 'XP_045911656.1', 'XP_035512099.1', 'XP_021465825.1',
            'XP_028439414.1', 'XP_014002235.1', 'AAR20843.1', 'XP_042700069.1', 'ABI21882.1', 'XP_042307646.1',
            'XP_006218639.1', 'AAI14139.1', 'ABD77268.1', 'XP_003476017.2', 'AAA31017.1', 'ABD77263.1', 'AAL66372.1',
            'XP_004006633.1', 'XP_006741075.1', 'XP_033927480.1', 'XP_046760974.1', 'XP_032600743.1', 'XP_030324024.1',
            'XP_014813383.1', 'PKK17119.1', 'XP_040197062.1', 'XP_031465919.1', 'XP_036447919.1', 'XP_017342999.1']


def get_colors(seqs):
    """make colors for bases in sequence
    https://dmnfarrell.github.io/bioinformatics/bokeh-sequence-aligner
    Edit by Chemical118"""
    text = [i for s in list(seqs) for i in s]
    '''
    a = dict()
    for i in 'ED':
        a[i]='red'
    for i in 'PAVMLIGH':
        a[i]='orange'
    for i in 'KR':
        a[i]='blue'
    for i in 'NCTQS':
        a[i]='green'
    for i in 'FYW':
        a[i]='yellow'
    for i in '-X'
        a[i]='white'
    '''
    clrs = {'E': 'red', 'D': 'red', 'P': 'orange', 'A': 'orange', 'V': 'orange', 'H': 'orange', 'M': 'orange',
            'L': 'orange', 'I': 'orange', 'G': 'orange', 'K': 'blue', 'R': 'blue', 'N': 'green', 'C': 'green',
            'T': 'green', 'Q': 'green', 'S': 'green', 'F': 'yellow', 'Y': 'yellow', 'W': 'yellow', '-': 'white',
            'X': 'white'}
    colors = [clrs[i] for i in text]
    return colors


def view_alignment(loc, typ='fasta', fontsize="9pt", plot_width=800):
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
    # make sequence and id lists from the aln object
    aln = list(SeqIO.parse(loc, typ))
    seqs = [rec.seq for rec in aln]
    ids = [rec.id for rec in aln]
    text = [i for s in list(seqs) for i in s]
    colors = get_colors(seqs)
    n = len(seqs[0])
    s = len(seqs)
    width = .4

    x = np.arange(1, n + 1)
    y = np.arange(0, s, 1)
    # creates a 2D grid of coords from the 1D arrays
    xx, yy = np.meshgrid(x, y)
    # flattens the arrays
    gx = xx.ravel()
    gy = yy.flatten()
    # use recty for rect coords with an offset
    recty = gy + .5
    h = 1 / s
    # now we can create the ColumnDataSource with all the arrays
    source = ColumnDataSource(dict(x=gx, y=gy, recty=recty, text=text, colors=colors))
    plot_height = len(seqs) * 15 + 50
    x_range = Range1d(0, n + 1, bounds='auto')
    if n > 100:
        viewlen = 100
    else:
        viewlen = n
    # view_range is for the close up view
    view_range = (0, viewlen)
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

    # sequence text view with ability to scroll along x axis
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

    output_file('Data/View/' + loc.split('/')[-1].split('.')[0] + '.html')
    show(p)
