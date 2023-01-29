from fastapi.testclient import TestClient

from api.main import app

from . import mock_geojson

client = TestClient(app)


def test_calculate_properties_polygon():
    response = client.post(
        "/calculate_properties",
        json=mock_geojson.mock_polygon_feature
    )

    assert response.status_code == 200
    assert response.json() == {
        "type": "Feature",
        "properties": {
            "name": "brendan",
            "area": 12392658216.37442,
            "centroid": {
                "type": "Point",
                "coordinates": [0.5, 0.5]
            }
        },
        "geometry": mock_geojson.mock_polygon_feature['geometry'],
        "bbox": [0, 0, 1, 1]
    }


def test_calculate_properties_polygon_empty_props():
    mock_copy = dict(mock_geojson.mock_polygon_feature)
    mock_copy['properties'] = {}
    mock_polygon_feature_empty_properties = mock_copy

    response = client.post(
        "/calculate_properties",
        json=mock_polygon_feature_empty_properties
    )

    assert response.status_code == 200
    assert response.json() == {
        "type": "Feature",
        "properties": {
            "area": 12392658216.37442,
            "centroid": {
                "type": "Point",
                "coordinates": [0.5, 0.5]
            }
        },
        "geometry": mock_polygon_feature_empty_properties['geometry'],
        "bbox": [0, 0, 1, 1]
    }


def test_calculate_properties_multipolygon():
    response = client.post(
        "/calculate_properties",
        json=mock_geojson.mock_multipolygon_feature
    )
    assert response.status_code == 200
    assert response.json() == {
        "type": "Feature",
        "properties": {
            "name": "brendan",
            "area": 24789092698.54032,
            "centroid": {
                "type": "Point",
                "coordinates": [1, 1]
            }
        },
        "geometry": mock_geojson.mock_multipolygon_feature['geometry'],
        "bbox": [0, 0, 2, 2]
    }


def test_calculate_properties_invalid_geometries():
    assert client.post(
        "/calculate_properties",
        json=mock_geojson.mock_point_feature
    ).status_code == 422

    assert client.post(
        "/calculate_properties",
        json=mock_geojson.mock_multipoint_feature
    ).status_code == 422

    assert client.post(
        "/calculate_properties",
        json=mock_geojson.mock_linestring_feature
    ).status_code == 422

    assert client.post(
        "/calculate_properties",
        json=mock_geojson.mock_multilinestring_feature
    ).status_code == 422
