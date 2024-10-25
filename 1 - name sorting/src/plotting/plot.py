import matplotlib.pyplot as plt
from typing import Any, Self, Callable
from .plot_utils import get_colormap


class Plot:
    def __init__(self, figsize: tuple[int, int] | None = None) -> None:
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

    def set_axis(self, value: str) -> Self:
        plt.axis(value)
        return self

    def set_color(self, color: str) -> Self:
        self.color = color
        return self

    def set_colormap(self, colormap: str, length: int) -> Self:
        self.color = get_colormap(colormap, length)
        return self

    def line_graph(
        self,
        x_data: list,
        y_data: list,
    ):
        plt.plot(
            x_data,
            y_data,
            color=self.color,
        )

        # Fit everything to the window
        plt.tight_layout()

    def bar_graph(
        self,
        x_data: list,
        y_data: list,
        *,
        horizontal: bool = False,
    ):
        if horizontal:
            plt.barh(
                x_data,
                y_data,
                color=self.color,
            )
        else:
            plt.bar(
                x_data,
                y_data,
                color=self.color,
            )

        # Fit everything to the window
        plt.tight_layout()

    def annotate(
        self,
        text: str,
        xy_coords: tuple[float, float],
        text_coord_offset: tuple[int, int],
        arrow_props: dict[str, Any] | None = dict(facecolor="black", arrowstyle="->"),
    ):
        plt.annotate(
            text,
            xy=xy_coords,
            xytext=text_coord_offset,
            textcoords="offset points",
            arrowprops=arrow_props,
        )

    def imshow(self, element):
        plt.imshow(element)

    @staticmethod
    def show_all_plots():
        plt.show()
