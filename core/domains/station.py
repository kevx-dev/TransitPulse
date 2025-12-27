from dataclasses import dataclass

@dataclass
class Station:
    name: str
    latitude: float
    longitude: float
    id: str
    distance: int

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError("name must be of type str")

        if not isinstance(self.distance, int):
            raise TypeError("distance must be of type int")

        if not isinstance(self.id,str):
            raise TypeError("id must be of type int")

        if self.id.strip() == "":
            raise ValueError("id must not be empty")

        if self.name.strip() == "":
            raise ValueError("name must not be empty")
        if not -90 <= self.latitude <= 90:
            raise ValueError(f"latitude must be between -90 and 90, got {self.latitude}")
        if not -180 <= self.longitude <= 180:
            raise ValueError(f"longitude must be between -180 and 180, got {self.longitude}")

    def __str__(self):
        return f"station name: {self.name} id: {self.id} latitude: {self.latitude} longitude: {self.longitude}"