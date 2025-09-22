from mongoengine import Document, StringField, IntField,ReferenceField,ListField

class Product(Document):
    product_id = StringField(required=True, primary_key=True)
    brand = StringField(required=True)
    category = StringField(required=True)
    name = StringField(required=True)
    description = StringField(required=True)
    price = StringField(required=True)
    stock = IntField(required=True)
    supplier_id = ListField(ReferenceField('Suppliers'))