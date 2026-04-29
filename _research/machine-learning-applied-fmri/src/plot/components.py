from __future__ import annotations

from nilearn.image import iter_img
from nilearn.plotting import plot_prob_atlas, plot_stat_map


def plot_component_atlas(components_img, *, title: str):
    return plot_prob_atlas(components_img, title=title)


def plot_component_maps(components_img, *, title_prefix: str, display_mode: str = "z", cut_coords: int = 1):
    displays = []
    for index, current_img in enumerate(iter_img(components_img)):
        displays.append(
            plot_stat_map(
                current_img,
                display_mode=display_mode,
                title=f"{title_prefix} {index}",
                cut_coords=cut_coords,
                colorbar=True,
            )
        )
    return displays