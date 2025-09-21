from mongoengine import Document, StringField, IntField

class Suppliers(Document):
    supplier_id = StringField(required=True, primary_key=True)
    supplier_description = StringField(required=True)
    name = StringField(required=True)
    contact_name = StringField(required=True)
    contact_email = StringField(required=True)
    phone = StringField(required=True)
    address = StringField(required=True)
    city = StringField(required=True)
    country = StringField(required=True)
    postal_code = StringField(required=True)
    products_supplied = IntField(required=True)