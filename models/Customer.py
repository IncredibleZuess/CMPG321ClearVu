from mongoengine import Document, StringField, EmailField, IntField
class Customer(Document):
    customer_id = StringField(required=True, primary_key=True)
    name = StringField(required=True)
    email = EmailField(required=True)
    creditLimit = StringField(required=True)
    discount = StringField(required=True)
    normalPaymentTerms = StringField(required=True)
    regionCode = IntField(required=True)
    repCode = IntField(required=True)
    settleTerms = StringField(required=True)
    customerCategory = StringField(required=True)