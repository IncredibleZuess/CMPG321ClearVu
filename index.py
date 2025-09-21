from dotenv import load_dotenv
from models.Customer import Customer
import os
from mongoengine import *

load_dotenv()
connect(host=os.getenv("MONGODB_URI"))

# Example usage: Creating and saving a new customer
new_customer = Customer(
    customer_id="C001",
    name="John Doe",
    email="john.doe@example.com",
    creditLimit="5000",
    discount="10%",
    normalPaymentTerms="30 days",
    regionCode=1,
    repCode=101,
    settleTerms="Net 30",
    customerCategory="Regular"
)
new_customer.save()
