from abc import ABC,abstractmethod

from core.domains.station import Station


class TransportAPI(ABC):

    @abstractmethod
    def get_nearby_stations(self, latitude: float, longitude: float) -> list[Station]:
        pass

