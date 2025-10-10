# ClearVu Star Schema for Analytics

## Overview

This star schema design transforms the ClearVu operational MongoDB database into an optimized structure for analytical queries and business intelligence. The schema enables efficient analysis of sales, payments, customers, products, and supplier relationships.

## Star Schema Architecture

```
                    DimDate
                       |
                       |
DimCustomer -----> FactSalesPayment <----- DimProduct
                       |
                       |
              DimRepresentative
                       |
                  DimSupplier
```

## Schema Components

### Fact Table

#### **FactSalesPayment**
The central fact table containing quantitative measures for sales and payment transactions.

**Measures (Metrics):**
- `quantity_sold`: Number of units sold
- `unit_price`: Price per unit
- `total_sales_amount`: Total sales revenue
- `payment_amount`: Amount paid
- `discount_amount`: Discount applied
- `net_amount`: Net revenue after discounts

**Foreign Keys:**
- `customer_key` → DimCustomer
- `product_key` → DimProduct
- `representative_key` → DimRepresentative
- `date_key` → DimDate
- `supplier_key` → DimSupplier

### Dimension Tables

#### **DimCustomer**
Customer profile and segmentation attributes.

**Key Attributes:**
- Customer identification (customer_id, name, email)
- Categories and segments
- Financial details (credit_limit, discount_percentage)
- Payment terms
- Geographic region (region_code, region_name)
- SCD Type 2 fields for tracking historical changes

**Analysis Use Cases:**
- Customer segmentation analysis
- Regional performance analysis
- Credit limit and discount analysis
- Customer lifetime value calculation

#### **DimProduct**
Product catalog and inventory information.

**Key Attributes:**
- Product identification (product_id, name, description)
- Classification (brand, category, subcategory)
- Pricing (price, cost, margin)
- Stock levels and status
- Product hierarchy for drill-down
- SCD Type 2 fields

**Analysis Use Cases:**
- Product performance analysis
- Inventory management
- Brand and category analysis
- Profit margin analysis
- Stock availability tracking

#### **DimRepresentative**
Sales representative and commission details.

**Key Attributes:**
- Representative identification (rep_code, description)
- Commission structure (method, percentage, tier)
- Performance metrics (YTD sales, commission)
- Territory and region assignment
- Employment status
- SCD Type 2 fields

**Analysis Use Cases:**
- Sales rep performance analysis
- Commission calculation and forecasting
- Territory analysis
- Sales team efficiency metrics

#### **DimSupplier**
Supplier profile and relationship management.

**Key Attributes:**
- Supplier identification (supplier_id, name)
- Contact information
- Location details (address, city, country)
- Supplier metrics (products_supplied, rating)
- Classification (type, tier)
- Partnership status
- SCD Type 2 fields

**Analysis Use Cases:**
- Supplier performance evaluation
- Geographic supplier distribution
- Supplier reliability tracking
- Preferred supplier analysis

#### **DimDate**
Time dimension for temporal analysis and reporting.

**Key Attributes:**
- Complete date hierarchies (year, quarter, month, week, day)
- Day attributes (day of week, month, year)
- Business day indicators
- Fiscal period attributes
- Season classification
- Holiday tracking

**Analysis Use Cases:**
- Time-series analysis
- Seasonal trend identification
- Year-over-year comparisons
- Business day vs. weekend analysis
- Fiscal period reporting

## Key Features

### Slowly Changing Dimensions (SCD Type 2)
All dimension tables support historical tracking with:
- `effective_date`: When the record became active
- `expiration_date`: When the record expired
- `is_current`: Flag indicating current version ('Y'/'N')

This allows tracking changes over time while maintaining historical accuracy.

### Indexes
Each table includes optimized indexes for:
- Primary and foreign keys
- Frequently queried attributes
- Date ranges
- Status and category fields

## Common Analytical Queries

### 1. Sales by Product Category and Time
```python
# Aggregate sales by product category and month
pipeline = [
    {
        "$lookup": {
            "from": "dim_product",
            "localField": "product_key",
            "foreignField": "product_key",
            "as": "product"
        }
    },
    {
        "$lookup": {
            "from": "dim_date",
            "localField": "date_key",
            "foreignField": "date_key",
            "as": "date"
        }
    },
    {
        "$group": {
            "_id": {
                "category": "$product.category",
                "year_month": "$date.year_month"
            },
            "total_sales": {"$sum": "$total_sales_amount"},
            "total_quantity": {"$sum": "$quantity_sold"}
        }
    }
]
```

### 2. Representative Commission Analysis
```python
# Calculate total commissions by representative
pipeline = [
    {
        "$lookup": {
            "from": "dim_representative",
            "localField": "representative_key",
            "foreignField": "representative_key",
            "as": "rep"
        }
    },
    {
        "$group": {
            "_id": "$rep.rep_code",
            "total_sales": {"$sum": "$total_sales_amount"},
            "calculated_commission": {
                "$sum": {
                    "$multiply": ["$total_sales_amount", "$rep.commission_percentage"]
                }
            }
        }
    }
]
```

### 3. Customer Purchase Patterns
```python
# Analyze customer purchase frequency and value
pipeline = [
    {
        "$lookup": {
            "from": "dim_customer",
            "localField": "customer_key",
            "foreignField": "customer_key",
            "as": "customer"
        }
    },
    {
        "$group": {
            "_id": "$customer.customer_id",
            "purchase_count": {"$sum": 1},
            "total_spent": {"$sum": "$net_amount"},
            "avg_order_value": {"$avg": "$net_amount"}
        }
    }
]
```

### 4. Supplier Product Performance
```python
# Evaluate products by supplier
pipeline = [
    {
        "$lookup": {
            "from": "dim_supplier",
            "localField": "supplier_key",
            "foreignField": "supplier_key",
            "as": "supplier"
        }
    },
    {
        "$lookup": {
            "from": "dim_product",
            "localField": "product_key",
            "foreignField": "product_key",
            "as": "product"
        }
    },
    {
        "$group": {
            "_id": "$supplier.name",
            "total_sales": {"$sum": "$total_sales_amount"},
            "products_sold": {"$sum": "$quantity_sold"}
        }
    }
]
```

## ETL Considerations

### Loading the Star Schema from Operational Data

1. **Extract**: Pull data from operational collections (Customer, Product, Sales, Payment, etc.)
2. **Transform**: 
   - Generate dimension keys
   - Flatten nested structures
   - Apply business rules
   - Handle SCDs
   - Calculate derived metrics
3. **Load**: Insert into fact and dimension tables

### Sample ETL Workflow
```python
from models.star_schema import *
from models import Customer, Product, Sales, Payment, Representative, Suppliers
from datetime import datetime

def load_dim_customer(operational_customer):
    """Transform operational customer to dimension table"""
    dim_customer = DimCustomer(
        customer_key=f"CK_{operational_customer.customer_id}",
        customer_id=operational_customer.customer_id,
        name=operational_customer.name,
        email=operational_customer.email,
        category=operational_customer.category,
        customer_category=operational_customer.customerCategory,
        credit_limit=float(operational_customer.creditLimit),
        discount_percentage=float(operational_customer.discount),
        normal_payment_terms=operational_customer.normalPaymentTerms,
        settle_terms=operational_customer.settleTerms,
        region_code=operational_customer.regionCode,
        effective_date=datetime.now().strftime("%Y-%m-%d"),
        is_current='Y'
    )
    dim_customer.save()
    return dim_customer

def load_fact_sales_payment(sales, payment=None):
    """Transform sales and payment into fact table"""
    fact = FactSalesPayment(
        fact_id=f"F_{sales.sales_id}",
        customer_key=f"CK_{sales.customer.customer_id}",
        product_key=f"PK_{sales.product[0].product_id}",
        representative_key=f"RK_{sales.representative.repCode}",
        date_key=sales.sales_date.replace('-', ''),
        quantity_sold=sales.quantity,
        unit_price=float(sales.price),
        total_sales_amount=float(sales.price) * sales.quantity,
        payment_amount=float(payment.amount) if payment else 0,
        net_amount=float(sales.price) * sales.quantity,
        transaction_type='sale' if not payment else 'both',
        payment_status=sales.status,
        transaction_date=datetime.strptime(sales.sales_date, "%Y-%m-%d"),
        sales_id=sales.sales_id
    )
    fact.save()
    return fact
```

## Benefits of This Star Schema

1. **Query Performance**: Denormalized structure optimizes read operations
2. **Intuitive Structure**: Easy for business users to understand
3. **Flexible Analysis**: Supports various analytical perspectives
4. **Historical Tracking**: SCD Type 2 maintains data history
5. **Scalability**: Indexed fields enable fast aggregations
6. **Business Intelligence**: Ready for BI tools (Tableau, Power BI, etc.)

## Next Steps

1. Implement ETL pipeline to populate star schema from operational database
2. Create aggregated summary tables for common queries
3. Set up scheduled jobs to refresh dimensional data
4. Build visualization dashboards using BI tools
5. Implement data quality checks and validation
6. Create date dimension pre-population script
7. Set up incremental loading for fact table

## Usage Example

```python
from mongoengine import connect
from models.star_schema import FactSalesPayment, DimCustomer, DimProduct

# Connect to MongoDB
connect('clearvu_analytics')

# Query: Top 10 customers by total sales
from mongoengine.queryset.visitor import Q

top_customers = FactSalesPayment.objects.aggregate([
    {
        '$group': {
            '_id': '$customer_key',
            'total_sales': {'$sum': '$total_sales_amount'}
        }
    },
    {'$sort': {'total_sales': -1}},
    {'$limit': 10}
])

for customer in top_customers:
    print(f"Customer: {customer['_id']}, Sales: ${customer['total_sales']}")
```
