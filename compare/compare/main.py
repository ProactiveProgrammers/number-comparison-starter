"""Perform number comparison to find the largest odd number."""

from typing import Tuple

import typer

from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()


def get_minimum(first: int, second: int, third: int) -> int:
    """Determine the smallest of the three provided values."""
    # TODO: write a function that will return the smallest of
    # the three provided int input values called:
    # --> first
    # --> second
    # --> third
    # if first is the smallest, return it
    # if second is the smallest, return it
    # if third is the smallest, return it


def get_largest_odd(first: int, second: int, third: int) -> Tuple[int, bool]:
    """Determine the largest odd number among the provided values."""
    # TODO: Call the get_minimum function to determine the smallest number
    answer = get_minimum(first, second, third)
    # TODO: implement a function that will identify the largest odd number
    # among the provided three input values called first, second, and third
    # TODO: if none of the numbers are odd, then return the smallest of
    # the three values
    # TODO: keep track of whether or not the returned value is due to the
    # fact that it is returning:
    # ---> the largest odd number among the function's inputs OR
    # ---> the smallest non-odd number among the functions inputs
    # TODO: make sure that the function returns two values in the
    # form (answer, found_odd), fitting the function's signature
    return (0, False)

@cli.command()
def compare(
    first: int = typer.Option(...),
    second: int = typer.Option(...),
    third: int = typer.Option(...),
) -> None:
    """Perform number comparison to find the largest odd number."""
    # TODO: create a console for rich text output
    console = Console()
    # TODO: create program output that exactly matches the expected
    # output on the ProactiveProgrammers web site! You can search
    # for the name of this project which is called "Comparing Numbers"
