from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional

@dataclass
class LineItem:
    amount: Decimal
    type: str

@dataclass
class Invoice:
    jurisdiction: str
    line_items: List[LineItem]

@dataclass
class Transaction:
    amount: Decimal
    jurisdiction: str
    type: str

@dataclass
class ProcessedInvoice:
    invoice_id: str
    tax_calculations: List['TaxCalculation']  # Forward reference
    total_tax: Decimal

@dataclass
class TaxCalculation:
    amount: Decimal