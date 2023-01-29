# Solution

Basic Python REST API using:

- Fast API
- GeoPandas
- geojson-pydantic
- pytest

## Setup

```
cd api

pip install -r requirements.txt
```

## To Run

In api directory:

```
uvicorn main:app
```

Endpoint documentation: http://127.0.0.1:8000/docs#/default/calculate_properties_calculate_properties_post

## To Test

In api directory:

```
pytest
```
