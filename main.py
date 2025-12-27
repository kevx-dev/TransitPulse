from infrastructure.transport_rest_client import TransportRestClient
from core.config.settings import Settings


def run():
    # noinspection PyArgumentList
    settings = Settings()

    client = TransportRestClient()
    client.get_nearby_stations(latitude=settings.latitude,longitude=settings.longitude)


    pass





if __name__ == "__main__":
    run()