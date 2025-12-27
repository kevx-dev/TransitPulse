from abc import ABC,abstractmethod

from core.domains.Station import Station


class TransportAPI(ABC):

    @abstractmethod
    def get_nearby_stations(self, latitude: float, longitude: float) -> list[Station]:
        pass

