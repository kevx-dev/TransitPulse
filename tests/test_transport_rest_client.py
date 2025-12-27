from core.domains.station import Station
from infrastructure.transport_rest_client import TransportRestClient


def test_get_nearby_stations_success(mocker):
    fake_api_response = [
        {
            "name": "Hauserstraße., Berlin",
            "location":{
                "latitude": 49.567955,
                "longitude": 16.513691
            }
        },
        {
            "name": "Berliner (S), Berlin",
            "location": {
                "latitude": 49.566437,
                "longitude": 16.513511
            }
        }
    ]

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = fake_api_response

    mocker.patch('requests.get',return_value=mock_response)

    client = TransportRestClient()
    stations = client.get_nearby_stations(52.5,13.4)

    assert len(stations) == 2
    assert stations[0].name == "Hauserstraße., Berlin"
    assert stations[1].name == "Berliner (S), Berlin"
    assert isinstance(stations[0],Station)