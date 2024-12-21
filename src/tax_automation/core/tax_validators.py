import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from .transaction import Transaction
from .tax_calculation import TaxCalculation

class TaxValidators:
    def validate_transaction(self, transaction: Transaction) -> bool:
        """
        Validate transaction data before tax calculation
        """
        if transaction.amount <= 0:
            raise ValueError("Transaction amount must be positive")
            
        if not transaction.jurisdiction:
            raise ValueError("Jurisdiction is required")
            
        return True
    
    def validate_calculation(self, calculation: TaxCalculation) -> bool:
        """
        Validate tax calculation results
        """
        if calculation.amount < 0:
            raise ValueError("Tax amount cannot be negative")
            
        if not calculation.rules_applied:
            raise ValueError("No tax rules were applied")
            
        return True