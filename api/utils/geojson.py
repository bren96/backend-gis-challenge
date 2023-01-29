import json

from geojson_pydantic import Feature, Point
from geojson_pydantic.types import BBox
from geopandas import GeoDataFrame


def calculate_area(feature: Feature) -> float:
    # calculate area using WGS 84 / Pseudo-Mercator
    gdf = GeoDataFrame.from_features(
        [feature.dict()],
        crs=4326
    )
    return gdf.to_crs(epsg=3857).area.iloc[0]


def calculate_bbox(feature: Feature) -> BBox:
    gdf = GeoDataFrame.from_features([feature.dict()])
    return json.loads(
        gdf.to_json(show_bbox=True)
    )['bbox']


def calculate_centroid(feature: Feature) -> Point:
    gdf = GeoDataFrame.from_features([feature.dict()])
    return json.loads(
        gdf.centroid.to_json()
    )['features'][0]['geometry']
