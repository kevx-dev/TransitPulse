from core.domains.station import Station
from core.exceptions.transport_rest_client_exception import TransportRestClientException
from core.interfaces.transport_api import TransportAPI
import requests

class TransportRestClient(TransportAPI):

    def get_nearby_stations(self, latitude: float, longitude: float) -> list[Station]:
        BASE_URL = "https://v6.db.transport.rest/locations/nearby"
        params = {
            "longitude":longitude,
            "latitude":latitude,
            "results":5,
        }
        try:
            response = requests.get(url=BASE_URL,params=params)
            response.raise_for_status()

            api_data = response.json()
            stations = [Station(name=station["name"],latitude=float(station["location"]["latitude"]),longitude=float(station["location"]["longitude"])) for station in api_data if "location" in station]
            print(stations)
            return stations

        except requests.exceptions.RequestException as e:
            raise TransportRestClientException(e)