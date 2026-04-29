from __future__ import annotations

from nilearn.regions import RegionExtractor

from src.types import RegionExtractionResult


def extract_regions(
    components_img,
    *,
    threshold: float = 0.5,
    thresholding_strategy: str = "ratio_n_voxels",
    extractor: str = "local_regions",
    standardize: bool = True,
    min_region_size: int = 1350,
    source_components: int = 20,
) -> RegionExtractionResult:
    region_extractor = RegionExtractor(
        components_img,
        threshold=threshold,
        thresholding_strategy=thresholding_strategy,
        extractor=extractor,
        standardize=standardize,
        min_region_size=min_region_size,
    )
    region_extractor.fit()
    regions_img = region_extractor.regions_img_
    n_regions = regions_img.shape[-1]
    title = (
        f"{n_regions} regions are extracted from {source_components} components.\n"
        "Each separate color of region indicates extracted region"
    )
    return RegionExtractionResult(
        extractor=region_extractor,
        regions_img=regions_img,
        regions_index=list(region_extractor.index_),
        n_regions=n_regions,
        title=title,
    )