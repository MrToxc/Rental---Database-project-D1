from dataclasses import dataclass

@dataclass
class Car:
    license_plate: str
    model: str
    price_per_day: float
    is_available: bool
    id_brand: int
    id_car: int = None
