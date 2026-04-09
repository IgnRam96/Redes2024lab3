#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Depedencies:
    pandas==2.2.2
    matplotlib==3.4.8
    click==8.1.7
"""

import os
import re

import click
import matplotlib.pyplot as plt
import pandas as pd


def format_stat(stat: pd.DataFrame) -> pd.DataFrame:
    """
    Formats the given stat dataframe by splitting the 'vectime' and 'vecvalue'
    columns, exploding the resulting dataframe, and converting the values to
    float.

    Args:
        stat (pandas.DataFrame): The input dataframe containing 'vectime' and
        'vecvalue' columns.

    Returns:
        pandas.DataFrame: The formatted dataframe with 'vectime' and 'vecvalue'
            columns as float values.
    """
    stat_values = stat.loc[:, ["vectime", "vecvalue"]]
    stat_values.loc[:, ["vectime", "vecvalue"]] = stat_values[
        ["vectime", "vecvalue"]
    ].apply(lambda x: x.str.split(" "), axis=1)
    stat_values = stat_values.explode(["vectime", "vecvalue"]).reset_index(drop=True)
    stat_values = stat_values.astype("float64")
    return stat_values


@click.command(
    help="Generate graphs from all the metrics of a results file passed from omnet."
)
@click.argument(
    "results_path",
    type=click.Path(exists=True),
)
@click.argument("output_path", type=click.Path(exists=True))
def gen_metric(results_path: str, output_path: str):
    """
    Generates graphs for all the metrics of a results file passed from omnet
    to an output path.
    """

    click.echo(f"Generating graphs from {results_path} to {output_path}\n\n")
    results = pd.read_csv(results_path)
    vectors = results.loc[results.type == "vector"]

    for stat_name in vectors.name.unique():
        fig, ax = plt.subplots()
        stat = vectors.loc[vectors.name == stat_name]
        graph_title = re.sub(r"(?<=\w)([A-Z])", r" \1", stat_name).capitalize()
        click.echo(
            f"Generating graph {graph_title} with each module where available:\n"
        )

        for module in stat.module.unique():
            click.echo(f"\t- plotting {stat_name} for {module}")
            module_stat = stat.loc[stat.module == module]
            module_vector = format_stat(module_stat.loc[:, ["vectime", "vecvalue"]])
            ax.plot(
                module_vector["vectime"],
                module_vector["vecvalue"],
                label=module,
            )

        ax.set_title(graph_title)
        ax.set_xlabel("Simulation Time (ms)")
        ax.legend()
        ax.grid()

        file_path = os.path.join(output_path, f"{stat_name}.png")
        fig.savefig(file_path)
        click.echo("")


if __name__ == "__main__":
    gen_metric()
