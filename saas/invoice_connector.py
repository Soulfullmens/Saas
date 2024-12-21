from src.tax_automation.core.tax_engine import TaxEngine
from .models import ProcessedInvoice, Invoice, LineItem, Transaction

class InvoiceConnector:
    def __init__(self, provider: str):
        self.client = self._initialize_client(provider)
        self.tax_engine = TaxEngine()
    
    async def process_invoice(self, invoice_id: str) -> ProcessedInvoice:
        """
        Fetch invoice data and calculate applicable taxes
        """
        invoice = await self.client.get_invoice(invoice_id)
        
        tax_calculations = []
        for line_item in invoice.line_items:
            tax = self.tax_engine.calculate_tax(
                Transaction(
                    amount=line_item.amount,
                    jurisdiction=invoice.jurisdiction,
                    type=line_item.type
                )
            )
            tax_calculations.append(tax)
        
        return ProcessedInvoice(
            invoice_id=invoice_id,
            tax_calculations=tax_calculations,
            total_tax=sum(tax.amount for tax in tax_calculations)
        )