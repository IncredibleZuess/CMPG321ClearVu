from dotenv import load_dotenv
import os
from mongoengine import *
from models.Customer import Customer
from models.Payment import Payment
from models.Product import Product
from models.Representative import Representative
from models.Suppliers import Suppliers

load_dotenv()
connect(host=os.getenv("MONGODB_URI"))


new_representative = Representative(
    repCode="R001",
    repDescription="Sales Representative",
    commissionMethod="Percentage",
    commission="5%"
)
new_representative.save()

new_product = Product(
    product_id="PR001",
    brand="Acme",
    category="Gadgets",
    name="Widget",
    description="A useful widget",
    price="100",
    stock=50,
    supplier_id=[]
)
new_product.save()


# Example usage: Creating and saving a new customer
new_customer = Customer(
    customer_id="C001",
    payments=[],
    name="John Doe",
    category="Regular",
    email="john.doe@example.com",
    creditLimit="5000",
    discount="10%",
    normalPaymentTerms="30 days",
    regionCode=1,
    settleTerms="Net 30",
    customerCategory="Regular"
)

new_payment = Payment(
    payment_id="P001",
    customer_id=new_customer,
    amount=1500,
    payment_date="2024-10-01",
    payment_method="Credit Card",
    status="Completed",
    representative=new_representative,
    products=[new_product]
)
new_payment.save()

new_supplier = Suppliers(
    supplier_id="S001",
    supplier_description="Main Supplier",
    name="Best Supplies Co.",
    contact_name="Alice Smith",
    contact_email="info@bestsupplies.com",
    phone="555-1234",
    address="123 Supply St, Commerce City",
    city="Commerce City",
    country="USA",
    postal_code="80022",
    products_supplied=100
)
new_supplier.save()
new_product.supplier_id.append(new_supplier)
new_product.save()
new_customer.payments.append(new_payment)
new_customer.save()

