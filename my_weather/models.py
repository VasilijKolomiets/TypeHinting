"""The projects model`s module."""
from pydantic import BaseModel, Field

class Latitude(BaseModel):
    """Latitude is GeoCoordinate.
    Field(..., ge=-90, le=90)
    """
    value: float = Field(..., ge=-90, le=90)

class Longitude(BaseModel):
    """Longitude is GeoCoordinate.
    Field(..., ge=-180, le=180)
    """
    value: float = Field(..., ge=-180, le=180)

class GeoLocation(BaseModel):
    """GeoLocation is the GeoCoordinates pair.
    
        latitude: Latitude
        longitude: Longitude
    """
    latitude: Latitude
    longitude: Longitude

if __name__ == '__main__':
    coords = GeoLocation(
        latitude=Latitude(value=49.8397),
        longitude=Longitude(value=24.0297)
    )
    print(coords)

    coords = GeoLocation(
        latitude=Latitude(value=-300),
        longitude=Longitude(value=200)
    )
    print(coords)
