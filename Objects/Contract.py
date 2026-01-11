from datetime import datetime, timedelta
from dataclasses import dataclass, field

@dataclass
class Contract:
    total_price: float
    id_customer: int = None
    date_from: datetime = field(
        default_factory=lambda: datetime.now().replace(microsecond=0)
    )
    date_to: datetime = field(
        default_factory=lambda: (datetime.now() + timedelta(days=1)).replace(microsecond=0)
    )
    id_contract: int = None
