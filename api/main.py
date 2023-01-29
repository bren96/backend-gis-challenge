from typing import Dict

from fastapi import FastAPI
from geojson_pydantic import Feature, MultiPolygon, Polygon

from utils.geojson import calculate_area, calculate_bbox, calculate_centroid

app = FastAPI()

FeatureModel = Feature[Polygon | MultiPolygon, Dict]


@app.post('/calculate_properties')
async def calculate_properties(feature: FeatureModel):
    response_feature = feature.dict(exclude_none=True)

    if response_feature['properties'] is None:
        response_feature['properties'] = {}

    response_feature['properties']['area'] = calculate_area(feature)
    response_feature['properties']['centroid'] = calculate_centroid(feature)
    response_feature['bbox'] = calculate_bbox(feature)

    return response_feature
