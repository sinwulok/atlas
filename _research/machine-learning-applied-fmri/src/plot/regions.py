from __future__ import annotations

import numpy as np
from nilearn import image, plotting


def plot_region_atlas(regions_img, *, title: str, view_type: str = "filled_contours"):
    return plotting.plot_prob_atlas(regions_img, view_type=view_type, title=title, colorbar=True)


def plot_region_overlays(regions_img, regions_index: list[int], component_index: int, *, title: str, colors: str = "rgbcmyk"):
    component_indices = np.where(np.asarray(regions_index) == component_index)[0]
    display = plotting.plot_anat(title=title)
    for region_offset, color in zip(component_indices, colors):
        display.add_overlay(image.index_img(regions_img, int(region_offset)), cmap=plotting.cm.alpha_cmap(color))
    return display