from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    surname: str
    email: str
    id_customer: int = None
