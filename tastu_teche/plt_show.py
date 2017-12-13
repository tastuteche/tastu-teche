import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
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


def get_colors(totalDataPoints):
    return np.random.uniform(low=0.0, high=1.0, size=(totalDataPoints, 3))


def pos_adjust(pos0, pos_scale=1):
    pos = {n: (x * pos_scale, y * pos_scale) for n, (x, y) in pos0.items()}
    return pos


def plt_G(G, pos_scale=1, width_scale=1, edge_alpha=0.2):
    #pos = nx.spring_layout(G)
    from networkx.drawing.nx_agraph import graphviz_layout
    pos0 = graphviz_layout(G, prog='neato')
    pos = pos_adjust(pos0, pos_scale)
    edge_labels = {(u, v): "%.3f" % d['weight']
                   for u, v, d in G.edges(data=True)}
    edgelist = G.edges()
    width = [G[u][v]['weight'] * width_scale for u, v in edgelist]
    nx.draw_networkx_edges(G, pos=pos, edgelist=edgelist,
                           width=width, alpha=edge_alpha)
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
    nx.draw_networkx_nodes(G, pos=pos)
    nx.draw_networkx_labels(G, pos)
