from .models import Transaction, TaxCalculation, TaxRule
from .tax_rules_repository import TaxRulesRepository
from .tax_rate_calculator import TaxRateCalculator
from .tax_validators import TaxValidators

class TaxEngine:
    def __init__(self):
        self.tax_rules = TaxRulesRepository()
        self.rate_calculator = TaxRateCalculator()
        self.validators = TaxValidators()
    
    def calculate_tax(self, transaction: Transaction) -> TaxCalculation:
        """
        Calculate tax for a given transaction based on jurisdiction rules
        """
        applicable_rules = self.tax_rules.get_rules(
            jurisdiction=transaction.jurisdiction,
            transaction_type=transaction.type
        )
        
        tax_amount = self.rate_calculator.compute(
            amount=transaction.amount,
            rules=applicable_rules,
            date=transaction.date
        )
        
        return TaxCalculation(
            amount=tax_amount,
            rules_applied=applicable_rules,
            jurisdiction=transaction.jurisdiction
        )