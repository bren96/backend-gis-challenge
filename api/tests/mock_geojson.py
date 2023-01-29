mock_point_feature = {
    "type": "Feature",
    "properties": {},
    "geometry": {
        "type": "Point",
            "coordinates": [0, 0]
    }
}

mock_multipoint_feature = {
    "type": "Feature",
    "properties": {},
    "geometry": {
        "type": "MultiPoint",
            "coordinates": [
                [0, 0],
                [1, 1]
            ]
    }
}

mock_linestring_feature = {
    "type": "Feature",
    "properties": {},
    "geometry": {
        "type": "LineString",
            "coordinates": [
                [0, 0],
                [1, 1]
            ]
    }
}

mock_multilinestring_feature = {
    "type": "Feature",
    "properties": {},
    "geometry": {
        "type": "MultiLineString",
            "coordinates": [
                [
                    [0, 0],
                    [1, 1]
                ],
                [
                    [1, 1],
                    [2, 2]
                ]
            ]
    }
}

mock_polygon_feature = {
    "type": "Feature",
    "properties": {
        "name": "brendan"
    },
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [0, 0],
                [0, 1],
                [1, 1],
                [1, 0],
                [0, 0]
            ]
        ]
    }
}

mock_multipolygon_feature = {
    "type": "Feature",
    "properties": {
        "name": "brendan",
    },
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
            [[
                [0, 0],
                [0, 1],
                [1, 1],
                [1, 0],
                [0, 0]
            ]],
            [[
                [1, 1],
                [1, 2],
                [2, 2],
                [2, 1],
                [1, 1]
            ]]
        ]
    },
}
