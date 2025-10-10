from mongoengine import Document, StringField, EmailField, IntField, FloatField

class DimCustomer(Document):
    """
    Dimension table for customer attributes.
    Contains descriptive information about customers.
    """
    # Primary Key
    customer_key = StringField(required=True, primary_key=True)
    
    # Customer Identifiers
    customer_id = StringField(required=True, unique=True)  # Original customer_id from source
    
    # Customer Profile
    name = StringField(required=True)
    email = EmailField(required=True)
    category = StringField(required=True)
    customer_category = StringField(required=True)
    
    # Financial Information
    credit_limit = FloatField(required=True)
    discount_percentage = FloatField(required=True)
    
    # Payment Terms
    normal_payment_terms = StringField(required=True)
    settle_terms = StringField(required=True)
    
    # Geographic Information
    region_code = IntField(required=True)
    region_name = StringField()  # Derived from region_code
    
    # Metadata for Slowly Changing Dimensions (SCD Type 2)
    effective_date = StringField()  # When this record became effective
    expiration_date = StringField()  # When this record expired (null if current)
    is_current = StringField(default='Y', choices=['Y', 'N'])
    
    meta = {
        'collection': 'dim_customer',
        'indexes': [
            'customer_id',
            'category',
            'region_code',
            'is_current'
        ]
    }
