import pytest

from core.domains.station import Station


def test_station_with_valid_data():
    name = "Berlin HBF"
    lat = 52.520008
    lon = 13.404954

    station = Station(
        name=name,
        latitude=lat,
        longitude=lon
    )

    assert station.name == "Berlin HBF"
    assert station.longitude == 13.404954
    assert station.latitude == 52.520008


def test_station_with_invalid_latitude_raises_error():
    name = "Test"
    lat = 91
    lon = 13.4

    with pytest.raises(ValueError):
        Station(name=name,latitude=lat,longitude=lon)

def test_station_with_invalid_longitude_raises_error():
    name = "Test"
    lat = 91
    lon = 500

    with pytest.raises(ValueError):
        Station(name=name,longitude=lon,latitude=lat)

def test_station_with_empty_name_raises_error():
    name = ""
    lat = 52.5
    lon = 13.4

    with pytest.raises(ValueError):
        Station(name=name,longitude=lon,latitude=lat)


def test_station_str_output():
    name = "Test"
    lat = 52
    lon = 13

    station = Station(name=name,latitude=lat,longitude=lon)
    expected = f"station name: {name} latitude: {lat} longitude: {lon}"

    assert str(station) == expected
