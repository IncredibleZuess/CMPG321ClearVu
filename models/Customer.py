from mongoengine import Document, StringField, EmailField, IntField, ListField, ReferenceField
class Customer(Document):
    customer_id = StringField(required=True, primary_key=True)
    payments = ListField(ReferenceField('Payment'))
    name = StringField(required=True)
    category = StringField(required=True)
    email = EmailField(required=True)
    creditLimit = StringField(required=True)
    discount = StringField(required=True)
    normalPaymentTerms = StringField(required=True)
    regionCode = IntField(required=True)
    settleTerms = StringField(required=True)
    customerCategory = StringField(required=True)


