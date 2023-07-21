import datetime
from generate_fileName import *
from printInvoice import *

# Function to generate a note/invoice for a laptop sale


def generate_sale_invoice(laptop, customer, quantity):
    laptop_name, brand, price, stock = laptop
    total_amount = int(price.strip().strip("$")) * int(quantity)
    shipping_cost = 50  # Assuming a fixed shipping cost of $50
    total_amount_with_shipping = total_amount + shipping_cost

    invoice_text = f'''
    Invoice for Laptop Sale
    -----------------------
    Laptop: {laptop_name}
    Brand: {brand}
    Customer: {customer}
    Date: {datetime.datetime.now().strftime('%Y-%m-%d')}
    Time: {datetime.datetime.now().strftime('%H:%M:%S')}
    Total Amount (excl. Shipping): ${total_amount}
    Shipping Cost: ${shipping_cost}
    Total Amount (incl. Shipping): ${total_amount_with_shipping}
    '''

    invoice_file_name = generate_file_name('sale_invoice')
    with open("Invoice/"+invoice_file_name, 'w') as file:
        file.write(invoice_text)

    chk = input("Do you want to print the Sale Invoice?(Y/N)")
    if chk.upper() == "Y":
        printInvoice(invoice_file_name)

    # Update the stock in the laptop list
    laptop[3] = str(int(stock) - int(quantity))

    return invoice_file_name
