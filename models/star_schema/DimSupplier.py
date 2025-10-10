from mongoengine import Document, StringField, IntField

class DimSupplier(Document):
    """
    Dimension table for supplier attributes.
    Contains descriptive information about suppliers.
    """
    # Primary Key
    supplier_key = StringField(required=True, primary_key=True)
    
    # Supplier Identifiers
    supplier_id = StringField(required=True, unique=True)  # Original supplier_id from source
    
    # Supplier Profile
    name = StringField(required=True)
    supplier_description = StringField(required=True)
    
    # Contact Information
    contact_name = StringField(required=True)
    contact_email = StringField(required=True)
    phone = StringField(required=True)
    
    # Location Information
    address = StringField(required=True)
    city = StringField(required=True)
    country = StringField(required=True)
    postal_code = StringField(required=True)
    region = StringField()  # Geographic region for analysis
    
    # Supplier Metrics
    products_supplied = IntField(required=True)
    supplier_rating = StringField()  # A, B, C, D rating
    reliability_score = IntField()  # 1-100
    
    # Supplier Classification
    supplier_type = StringField()  # manufacturer, distributor, wholesaler
    supplier_tier = StringField()  # tier_1, tier_2, tier_3
    
    # Business Relationship
    partnership_status = StringField(default='active', choices=['active', 'inactive', 'suspended'])
    contract_start_date = StringField()
    contract_end_date = StringField()
    preferred_supplier = StringField(default='N', choices=['Y', 'N'])
    
    # Metadata for Slowly Changing Dimensions (SCD Type 2)
    effective_date = StringField()  # When this record became effective
    expiration_date = StringField()  # When this record expired (null if current)
    is_current = StringField(default='Y', choices=['Y', 'N'])
    
    meta = {
        'collection': 'dim_supplier',
        'indexes': [
            'supplier_id',
            'country',
            'city',
            'partnership_status',
            'is_current'
        ]
    }
