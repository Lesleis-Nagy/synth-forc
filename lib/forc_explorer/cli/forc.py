import sys

import typer

from forc_explorer.synthforc_db import SynthForcDB
from forc_explorer.plotting.forc import generate_forc_plot

app = typer.Typer()


@app.command()
def draw_forc(input_data_file: str, aspect_ratio: float, size: float, output_file: str):
    r"""
    Create a drawing of a FORC diagram based on data read from `input_data_file`.
    :param input_data_file: the input data file containing direction averaged FORC data.
    :param aspect_ratio: the aspect ratio of the grain.
    :param size: the size of the grain.
    :param output_file: the output file.
    :return:
    """
    synthforc_db = SynthForcDB(input_data_file)

    forc_loops = synthforc_db.single_forc_loops_by_aspect_ratio_and_size(aspect_ratio, size)
    if forc_loops.shape[0] == 0:
        print(f"No loops found for aspect ratio {aspect_ratio} and size {size}")
        sys.exit(1)
    print(f"Generating FORC plot: {output_file}")
    generate_forc_plot(forc_loops, output_file)


def main():
    app()


if __name__ == "__main__":
    main()
