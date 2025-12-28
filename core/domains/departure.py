from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Departure:
    longitude: float
    latitude: float
    departure_name: str
    when: str
    delay: Optional[int] = None

    @property
    def formatted_time(self) -> str:
        date = datetime.fromisoformat(self.when)
        return datetime.strftime(date, "%H:%M")

    @property
    def delay_display(self) -> str:
        if self.delay is None:
            return "❎"
        elif self.delay == 0:
            return "✅"
        else:
            return f"+{self.delay}min"

    def __str__(self):
        return f"longitude: {self.longitude} latitude: {self.latitude} departure_name: {self.departure_name} when: {self.when} delay: {self.delay}"

    def __post_init__(self):
        if not isinstance(self.longitude, float) or not isinstance(self.latitude, float):
            raise TypeError("longitude and latitude must be of type float")

        if not isinstance(self.departure_name, str):
            raise TypeError("departure_name must be of type string")

        if not isinstance(self.when, str):
            raise TypeError("when must be of type string")

        if self.delay is not None and not isinstance(self.delay, int):
            raise TypeError("delay must be of type int or None")

        if not self.departure_name.strip():
            raise ValueError("departure name must not be empty")

        if not self.when.strip():
            raise ValueError("when name must not be empty")

        if not (-180 <= self.longitude <= 180):
            raise ValueError("longitude must be between -180 and 180")

        if not (-90 <= self.latitude <= 90):
            raise ValueError("latitude must be between -90 and 90")
