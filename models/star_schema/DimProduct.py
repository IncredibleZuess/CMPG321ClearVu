from mongoengine import Document, StringField, IntField, FloatField

class DimProduct(Document):
    """
    Dimension table for product attributes.
    Contains descriptive information about products.
    """
    # Primary Key
    product_key = StringField(required=True, primary_key=True)
    
    # Product Identifiers
    product_id = StringField(required=True, unique=True)  # Original product_id from source
    
    # Product Details
    name = StringField(required=True)
    description = StringField(required=True)
    brand = StringField(required=True)
    category = StringField(required=True)
    
    # Pricing Information
    price = FloatField(required=True)
    cost = FloatField()  # Cost price (if available)
    margin = FloatField()  # Profit margin
    
    # Inventory
    stock_level = IntField(required=True)
    stock_status = StringField()  # in_stock, low_stock, out_of_stock
    
    # Product Hierarchy (for drill-down analysis)
    product_category = StringField(required=True)
    product_subcategory = StringField()
    product_line = StringField()
    
    # Metadata for Slowly Changing Dimensions (SCD Type 2)
    effective_date = StringField()  # When this record became effective
    expiration_date = StringField()  # When this record expired (null if current)
    is_current = StringField(default='Y', choices=['Y', 'N'])
    
    meta = {
        'collection': 'dim_product',
        'indexes': [
            'product_id',
            'brand',
            'category',
            'is_current',
            'stock_status'
        ]
    }
