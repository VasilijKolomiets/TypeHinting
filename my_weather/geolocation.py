"""Module for current geolocation defining"""

import geocoder

from models import GeoLocation, Latitude, Longitude


def location() -> GeoLocation | None:
    """Determine current device geolocation.
    Args:
        None
    Returns:
        `GeoLocation` object
    """
    latlng = geocoder.ip("me").latlng
    if latlng:
        return GeoLocation(
            latitude=Latitude(value=latlng[0]),
            longitude=Longitude(value=latlng[1]),
        )


if __name__ == "__main__":
    print(location())
