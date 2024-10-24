from typing import Any, SupportsIndex
import matplotlib.pyplot as plt


def get_colormap(
    colormap: str, amount: int | SupportsIndex
) -> list[tuple[float, float, float, float]]:
    # If the amount is already a number use that, or get the length of it (presumed to be a list of sorts)
    amount = amount if amount is int else len(amount)
    cmap = plt.get_cmap(colormap, amount)
    colors = [cmap(i) for i in range(amount)]
    return colors


def plot_bar_graph(
    x: list,
    y: list,
    *,
    color: str | list[tuple[float, float, float, float]],
    title: str,
    xlabel: str,
    ylabel: str,
    xticks_kwargs: dict[str, Any] = {},
    horizontal: bool = False,
):
    # Create explicitly instead of using DataFrame.plot() for more control (and due to some issues)
    if horizontal:
        plt.barh(
            x,
            y,
            color=color,
        )
    else:
        plt.bar(
            x,
            y,
            color=color,
        )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Rotate labels
    plt.xticks(**xticks_kwargs)

    # Fit everything to the window
    plt.tight_layout()


def plot_line_graph(
    x: list,
    y: list,
    *,
    color: str | list[tuple[float, float, float, float]],
    title: str,
    xlabel: str,
    ylabel: str,
    xticks_kwargs: dict[str, Any],
):
    # Create explicitly instead of using DataFrame.plot() for more control (and due to some issues)
    plt.plot(
        x,
        y,
        color=color,
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Rotate labels
    plt.xticks(**xticks_kwargs)

    # Fit everything to the window
    plt.tight_layout()
