import matplotlib.pyplot as plt
from tabulate import tabulate
is_show = False


def set_show(show):
    global is_show
    is_show = show


def plt_show(png_file):
    if is_show:
        plt.show()
    else:
        plt.savefig(png_file, dpi=200)
        plt.cla()
        plt.clf()
        plt.close()


def df_show(df, df_file, tilte):
    if is_show:
        print(tilte)
        print(df_file)
    else:
        with open(df_file, 'w') as f:
            body = tabulate(df, headers='keys', tablefmt='pipe')
            f.write('\n\n'.join([tilte, body]))


def plt_figure(size=15):
    plt.figure(figsize=(size, size))


def ax_hbar_value(ax):
    x_offset = -0.03
    y_offset = 0.02
    ax.set_title('Average Recency (days since last purchase)')
    for p in ax.patches:
        b = p.get_bbox()
        val = "{:.0f}".format(b.x1 + b.x0)
        ax.annotate(val, (b.x1 + x_offset, (b.y0 + b.y1) / 2 + y_offset))


def ax_vbar_value(ax):
    x_offset = -0.03
    y_offset = 0.02
    ax.set_title('Number of Customers (y) by number of Orders (x)')
    ax.set_ylabel('Number of Customers')
    for p in ax.patches:
        b = p.get_bbox()
        val = "{:.0f}".format(b.y1 + b.y0)
        ax.annotate(val, ((b.x0 + b.x1) / 2 + x_offset, b.y1 + y_offset))
