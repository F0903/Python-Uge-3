import pandas as pd
import matplotlib.pyplot as plt
from typing import Any, Self, Callable
from plot_utils import get_colormap


class Plot:
    def __init__(self, data: pd.DataFrame, figsize: tuple[int, int]) -> None:
        self.data = data
        self.fig = plt.figure(figsize=figsize)
        self.color = None

    def set_title(self, title: str) -> Self:
        plt.title(title)
        self.fig.canvas.manager.set_window_title(title)
        return self

    def set_xlabel(self, xlabel: str) -> Self:
        plt.xlabel(xlabel)
        return self

    def set_ylabel(self, ylabel: str) -> Self:
        plt.ylabel(ylabel)
        return self

    def set_xticks_kwargs(self, xticks_kwargs: dict[str, Any]) -> Self:
        plt.xticks(**xticks_kwargs)
        return self

    # Too many options to wrap, just let consumer modify through a lambda lol
    def set_advanced_axes_options(self, fn: Callable[[plt.Axes], None]) -> Self:
        axes = self.fig.gca()
        fn(axes)
        return self

    def set_color(self, color: str) -> Self:
        self.color = color
        return self

    def set_colormap(self, colormap: str) -> Self:
        self.color = get_colormap(colormap, len(self.data))
        return self

    def line_graph(
        self,
        x_column: str,
        y_column: str,
    ):
        # Create explicitly instead of using DataFrame.plot() for more control (and due to some issues)
        plt.plot(
            self.data[x_column],
            self.data[y_column],
            color=self.color,
        )

        # Fit everything to the window
        plt.tight_layout()

    def bar_graph(
        self,
        x_column: str,
        y_column: str,
        *,
        horizontal: bool = False,
    ):
        # Create explicitly instead of using DataFrame.plot() for more control (and due to some issues)
        if horizontal:
            plt.barh(
                self.data[x_column],
                self.data[y_column],
                color=self.color,
            )
        else:
            plt.bar(
                self.data[x_column],
                self.data[y_column],
                color=self.color,
            )

        # Fit everything to the window
        plt.tight_layout()

    def annotate(
        self,
        text: str,
        x_data: str,
        y_data: str,
        x_data_index: int,
        y_data_index: int,
        text_coord_offset: tuple[int, int],
        arrow_props: dict[str, Any] | None = dict(facecolor="black", arrowstyle="->"),
    ):
        plt.annotate(
            text,
            xy=(
                self.data[x_data].iloc[x_data_index],
                self.data[y_data].iloc[y_data_index],
            ),
            xytext=text_coord_offset,
            textcoords="offset points",
            arrowprops=arrow_props,
        )

    @staticmethod
    def show_all_plots():
        plt.show()
