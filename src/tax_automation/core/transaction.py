from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum

class TransactionType(Enum):
    SALE = "sale"
    SERVICE = "service"
    DIGITAL_GOOD = "digital_good"
    PHYSICAL_GOOD = "physical_good"

@dataclass
class Transaction:
    amount: Decimal
    jurisdiction: str  # Could be state/province/country code
    type: TransactionType
    date: datetime = datetime.now()