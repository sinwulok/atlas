from __future__ import annotations

from nilearn import plotting


def find_connectome_coords(regions_img):
    return plotting.find_probabilistic_atlas_cut_coords(regions_img)


def plot_connectivity_matrix(mean_correlation, *, title: str, vmax: float = 1, vmin: float = -1):
    return plotting.plot_matrix(mean_correlation, vmax=vmax, vmin=vmin, colorbar=True, title=title)


def plot_connectome_view(mean_correlation, coords_connectome, *, title: str, edge_threshold: str = "90%"):
    return plotting.plot_connectome(mean_correlation, coords_connectome, edge_threshold=edge_threshold, title=title)


def view_connectome(mean_correlation, coords_connectome, *, title: str, edge_threshold: str = "90%"):
    return plotting.view_connectome(mean_correlation, coords_connectome, edge_threshold=edge_threshold, title=title)