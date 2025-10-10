"""
Star Schema Models for ClearVu Analytics Database

This package contains the star schema design for analyzing sales and payment data.

Star Schema Structure:
- Fact Table: FactSalesPayment (contains measures/metrics)
- Dimension Tables: DimCustomer, DimProduct, DimRepresentative, DimSupplier, DimDate

The star schema is optimized for:
- Sales analysis by product, customer, representative, supplier, and time
- Payment tracking and reconciliation
- Commission calculations
- Inventory and stock analysis
- Customer segmentation
- Geographic analysis
"""

from .FactSalesPayment import FactSalesPayment
from .DimCustomer import DimCustomer
from .DimProduct import DimProduct
from .DimRepresentative import DimRepresentative
from .DimSupplier import DimSupplier
from .DimDate import DimDate

__all__ = [
    'FactSalesPayment',
    'DimCustomer',
    'DimProduct',
    'DimRepresentative',
    'DimSupplier',
    'DimDate'
]
