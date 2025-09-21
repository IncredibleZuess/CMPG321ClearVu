from mongoengine import Document, StringField, EmailField, ListField, ReferenceField
class Representative(Document):
    repCode = StringField(required=True, primary_key=True)
    repDescription = StringField(required=True)
    commissionMethod = StringField(required=True)
    commission = StringField(required=True)