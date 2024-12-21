from decimal import Decimal
from typing import List
from datetime import datetime
from .models import TaxRule

class TaxRateCalculator:
    def compute(self, amount: Decimal, rules: List[TaxRule], date: datetime) -> Decimal:
        """
        Compute the tax amount based on the given rules
        """
        total_tax = Decimal("0")
        
        for rule in rules:
            # Apply each tax rule sequentially
            # Some jurisdictions might have multiple layers of taxation
            tax_amount = amount * rule.rate
            total_tax += tax_amount
            
        return total_tax.quantize(Decimal("0.01"))  # Round to 2 decimal places