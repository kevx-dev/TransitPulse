from dataclasses import dataclass

@dataclass
class Departure:
    longitude: float
    latitude: float
    departure_name: str
    when: str
    delay: int


    def __str__(self):
        return f"longitude: {self.longitude} latitude: {self.latitude} departure_name: {self.departure_name} when: {self.when} delay: {self.delay}"