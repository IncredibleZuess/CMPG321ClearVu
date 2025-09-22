from mongoengine import Document, StringField, EmailField, ListField, ReferenceField, IntField

class Sales(Document):
    sales_id = StringField(required=True, primary_key=True)
    product = ListField(ReferenceField('Product', required=True))
    quantity = IntField(required=True)
    price = StringField(required=True)
    customer = ReferenceField('Customer', required=True)
    representative = ReferenceField('Representative', required=True)
    sales_date = StringField(required=True)
    status = StringField(required=True)