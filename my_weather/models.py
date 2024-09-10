"""The projects model`s module."""

class Latitude:
    """Latitude is GeoCoordinate.
    Field(..., ge=-90, le=90)
    """
    pass


class Longitude:
    """Longitude is GeoCoordinate.
    Field(..., ge=-180, le=180)
    """
    pass


class GeoLocation:
    """GeoLocation is the GeoCoordinates pair.

        latitude: Latitude
        longitude: Longitude
    """
    latitude: Latitude
    longitude: Longitude

if __name__ == '__main__':
    pass
