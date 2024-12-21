from dataclasses import dataclass
from decimal import Decimal
from typing import List

@dataclass
class TaxRule:
    rate: Decimal
    jurisdiction: str
    rule_id: str
    description: str

@dataclass
class TaxCalculation:
    amount: Decimal
    rules_applied: List[TaxRule]
    jurisdiction: str