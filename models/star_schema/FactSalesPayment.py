from mongoengine import Document, StringField, IntField, FloatField, DateTimeField, ReferenceField

class FactSalesPayment(Document):
    """
    Fact table combining sales and payment transactions.
    Contains measures (quantitative data) and foreign keys to dimension tables.
    """
    # Primary Key
    fact_id = StringField(required=True, primary_key=True)
    
    # Foreign Keys to Dimension Tables
    customer_key = ReferenceField('DimCustomer', required=True)
    product_key = ReferenceField('DimProduct', required=True)
    representative_key = ReferenceField('DimRepresentative', required=True)
    date_key = ReferenceField('DimDate', required=True)
    supplier_key = ReferenceField('DimSupplier')
    
    # Measures (Metrics for Analysis)
    quantity_sold = IntField(required=True, default=0)
    unit_price = FloatField(required=True)
    total_sales_amount = FloatField(required=True)
    payment_amount = FloatField(required=True)
    discount_amount = FloatField(default=0.0)
    net_amount = FloatField(required=True)  # total_sales_amount - discount_amount
    
    # Transaction Details
    transaction_type = StringField(required=True, choices=['sale', 'payment', 'both'])
    payment_method = StringField()  # cash, credit_card, bank_transfer, etc.
    payment_status = StringField(required=True, choices=['pending', 'completed', 'failed', 'cancelled'])
    
    # Temporal Fields (also linked to DimDate)
    transaction_date = DateTimeField(required=True)
    payment_date = DateTimeField()
    
    # Additional Context
    sales_id = StringField()  # Reference to original sales transaction
    payment_id = StringField()  # Reference to original payment transaction
    
    meta = {
        'collection': 'fact_sales_payment',
        'indexes': [
            'customer_key',
            'product_key',
            'representative_key',
            'date_key',
            'transaction_date',
            'payment_status'
        ]
    }
