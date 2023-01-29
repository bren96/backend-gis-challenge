from geojson_pydantic import Feature

from utils.geojson import calculate_area, calculate_bbox, calculate_centroid
from .mock_geojson import mock_multipolygon_feature, mock_polygon_feature


def test_calculate_area_polygon():
    assert calculate_area(
        Feature(**mock_polygon_feature)
    ) == 12392658216.37442


def test_calculate_area_multipolygon():
    assert calculate_area(
        Feature(**mock_multipolygon_feature)
    ) == 24789092698.54032


def test_calculate_centroid_polygon():
    assert calculate_centroid(Feature(**mock_polygon_feature)) == {
        "type": "Point",
        "coordinates": [0.5, 0.5]
    }


def test_calculate_centroid_multipolygon():
    assert calculate_centroid(Feature(**mock_multipolygon_feature)) == {
        "type": "Point",
        "coordinates": [1, 1]
    }


def test_calculate_bbox_polygon():
    assert calculate_bbox(Feature(**mock_polygon_feature)) == [0, 0, 1, 1]


def test_calculate_bbox_multipolygon():
    assert calculate_bbox(Feature(**mock_multipolygon_feature)) == [0, 0, 2, 2]
