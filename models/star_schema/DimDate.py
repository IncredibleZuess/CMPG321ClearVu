from mongoengine import Document, StringField, IntField, DateTimeField

class DimDate(Document):
    """
    Dimension table for date/time attributes.
    Contains temporal hierarchies for time-based analysis.
    Pre-populated with dates for analysis period.
    """
    # Primary Key
    date_key = StringField(required=True, primary_key=True)  # Format: YYYYMMDD
    
    # Full Date
    full_date = DateTimeField(required=True, unique=True)
    date_string = StringField(required=True)  # Format: YYYY-MM-DD
    
    # Year Attributes
    year = IntField(required=True)
    year_name = StringField(required=True)  # "2025"
    
    # Quarter Attributes
    quarter = IntField(required=True)  # 1, 2, 3, 4
    quarter_name = StringField(required=True)  # "Q1 2025"
    year_quarter = StringField(required=True)  # "2025-Q1"
    
    # Month Attributes
    month = IntField(required=True)  # 1-12
    month_name = StringField(required=True)  # "January"
    month_abbr = StringField(required=True)  # "Jan"
    year_month = StringField(required=True)  # "2025-01"
    year_month_name = StringField(required=True)  # "January 2025"
    
    # Week Attributes
    week_of_year = IntField(required=True)  # 1-53
    week_of_month = IntField(required=True)  # 1-5
    year_week = StringField(required=True)  # "2025-W01"
    
    # Day Attributes
    day_of_month = IntField(required=True)  # 1-31
    day_of_year = IntField(required=True)  # 1-366
    day_of_week = IntField(required=True)  # 1-7 (Monday=1)
    day_name = StringField(required=True)  # "Monday"
    day_abbr = StringField(required=True)  # "Mon"
    
    # Business Day Flags
    is_weekend = StringField(required=True, choices=['Y', 'N'])
    is_weekday = StringField(required=True, choices=['Y', 'N'])
    is_holiday = StringField(default='N', choices=['Y', 'N'])
    is_business_day = StringField(required=True, choices=['Y', 'N'])
    holiday_name = StringField()  # Name of holiday if applicable
    
    # Fiscal Period (if different from calendar)
    fiscal_year = IntField()
    fiscal_quarter = IntField()
    fiscal_month = IntField()
    fiscal_week = IntField()
    
    # Relative Date Indicators
    is_current_day = StringField(default='N', choices=['Y', 'N'])
    is_current_week = StringField(default='N', choices=['Y', 'N'])
    is_current_month = StringField(default='N', choices=['Y', 'N'])
    is_current_quarter = StringField(default='N', choices=['Y', 'N'])
    is_current_year = StringField(default='N', choices=['Y', 'N'])
    
    # Season (optional)
    season = StringField()  # "Winter", "Spring", "Summer", "Fall"
    
    meta = {
        'collection': 'dim_date',
        'indexes': [
            'full_date',
            'year',
            'quarter',
            'month',
            'year_month',
            'is_business_day',
            'is_weekend'
        ]
    }
