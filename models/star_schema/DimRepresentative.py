from mongoengine import Document, StringField, FloatField

class DimRepresentative(Document):
    """
    Dimension table for sales representative attributes.
    Contains descriptive information about sales representatives.
    """
    # Primary Key
    representative_key = StringField(required=True, primary_key=True)
    
    # Representative Identifiers
    rep_code = StringField(required=True, unique=True)  # Original repCode from source
    
    # Representative Profile
    rep_description = StringField(required=True)
    rep_name = StringField()  # Full name if available
    rep_title = StringField()  # Job title
    
    # Commission Information
    commission_method = StringField(required=True)
    commission_percentage = FloatField(required=True)
    commission_tier = StringField()  # bronze, silver, gold, platinum
    
    # Performance Metrics (can be updated periodically)
    total_sales_ytd = FloatField(default=0.0)  # Year-to-date sales
    total_commission_ytd = FloatField(default=0.0)
    performance_rating = StringField()  # excellent, good, average, poor
    
    # Territory/Region
    territory = StringField()
    region = StringField()
    
    # Employment Status
    status = StringField(default='active', choices=['active', 'inactive', 'terminated'])
    hire_date = StringField()
    
    # Metadata for Slowly Changing Dimensions (SCD Type 2)
    effective_date = StringField()  # When this record became effective
    expiration_date = StringField()  # When this record expired (null if current)
    is_current = StringField(default='Y', choices=['Y', 'N'])
    
    meta = {
        'collection': 'dim_representative',
        'indexes': [
            'rep_code',
            'commission_method',
            'status',
            'is_current'
        ]
    }
