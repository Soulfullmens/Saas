from dataclasses import dataclass
from typing import Dict, List

@dataclass
class FilingPeriod:
    start_date: str
    end_date: str

@dataclass
class TaxFiling:
    period: FilingPeriod
    calculations: Dict
    documents: List[str]

@dataclass
class FilingResult:
    status: str
    reference_id: str