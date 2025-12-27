from dataclasses import dataclass

@dataclass
class Location:
    longitude: float
    latitude: float

    def __post_init__(self):
        if not -90 <= self.latitude <= 90:
            raise ValueError(f"latitude must be between -90 and 90, got {self.latitude}")
        if not -180 <= self.longitude <= 180:
            raise ValueError(f"longitude must be between -180 and 180, got {self.longitude}")

    def __str__(self):
        return f"latitude: {self.latitude} longitude: {self.longitude}"