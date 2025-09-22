from mongoengine import Document, StringField, IntField, ReferenceField, ListField

#TODO Update from initial bad data model
class Payment(Document):
    payment_id = StringField(required=True, primary_key=True)
    customer_id = ReferenceField('Customer', required=True)
    amount = IntField(required=True)
    payment_date = StringField(required=True)
    payment_method = StringField(required=True)
    status = StringField(required=True)
    representative = ReferenceField('Representative', required=True)
    products = ListField(ReferenceField('Product'))
