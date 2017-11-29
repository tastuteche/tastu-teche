import matplotlib.pyplot as plt
from tabulate import tabulate
is_show = True


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
