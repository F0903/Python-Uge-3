from typing import SupportsIndex
import matplotlib.pyplot as plt


def get_colormap(
    colormap: str, amount: int | SupportsIndex
) -> list[tuple[float, float, float, float]]:
    # If the amount is already a number use that, or get the length of it (it is then presumed to be an array of sorts)
    amount = amount if isinstance(amount, int) else len(amount)

    cmap = plt.get_cmap(colormap, amount)
    colors = [cmap(i) for i in range(amount)]
    return colors
