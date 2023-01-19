import os
import matplotlib.pyplot as plt

from synth_forc.settings import Settings

def generate_forc_loops_plot(forc_loops, output_file, dpi=None):

    settings = Settings.get_settings()

    minor_loops = forc_loops.groupby(forc_loops.Br)

    fig, ax = plt.subplots()
    ax.set_xlabel("B (T)")
    ax.set_ylabel("M (A/m)")

    first_loop = True
    fl_B = []
    fl_M = []
    for key, minor_loop in minor_loops:
        ax.plot(minor_loop.B, minor_loop.M, c="black", linewidth=0.4)
        if first_loop:
            # Extract the major loop, reverse & flip it to complete the loop's 'top'.
            fl_B = list(reversed(minor_loop.B.tolist()))
            fl_M = [-1.0 * M for M in minor_loop.M.tolist()]
            ax.plot(fl_B, fl_M, c="black", linewidth=0.4)
            first_loop = False

    extension = os.path.splitext(output_file)
    if extension[1] == ".png":
        if dpi is not None:
            dpi = dpi
        else:
            dpi = settings.dpi
        fig.savefig(output_file, dpi=dpi)
        plt.close()
    else:
        fig.savefig(output_file)
        plt.close()
