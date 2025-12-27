from core.domains.departure import Departure
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
            stations = [Station(name=station["name"],latitude=float(station["location"]["latitude"]),longitude=float(station["location"]["longitude"]),id=station["id"],distance=station["distance"]) for station in api_data if "location" in station]
            return stations

        except requests.exceptions.RequestException as e:
            raise TransportRestClientException(e)

    def get_departures(self, stop_id: int) -> list[Departure]:
        BASE_URL = f"https://v6.db.transport.rest/stops/{stop_id}/departures"
        params = {
            "language":"de",
            "duration":20
        }

        try:
            response = requests.get(url=BASE_URL,params=params)
            response.raise_for_status()
            api_data = response.json()


            departure_data = [Departure(
                longitude=departure["stop"]["location"]["longitude"],
                latitude=departure["stop"]["location"]["latitude"],
                departure_name=departure["direction"],
                when=departure["when"],
                delay=departure["delay"]
            ) for departure in api_data["departures"]]

            return departure_data

        except requests.exceptions.RequestException as e:
            raise  TransportRestClientException(e)

