import datetime
from read import *
from generate_fileName import *
from printInvoice import *

# Function to generate a note/invoice for a laptop order


def generate_order_invoice(laptop, distributor, quantity):
    laptop_name, brand, price, stock = laptop
    net_amount = int(price.strip().strip("$")) * int(quantity)
    vat_amount = net_amount * 0.13
    gross_amount = net_amount + vat_amount

    invoice_text = f'''
    Invoice for Laptop Order
    -----------------------
    Distributor: {distributor}
    Laptop: {laptop_name}
    Brand: {brand}
    Date: {datetime.datetime.now().strftime('%Y-%m-%d')}
    Time: {datetime.datetime.now().strftime('%H:%M:%S')}
    Net Amount: ${net_amount}
    VAT Amount (13%): ${vat_amount}
    Gross Amount: ${gross_amount}
    '''

    invoice_file_name = generate_file_name('order_invoice')
    with open("Invoice/"+invoice_file_name, 'w') as file:
        file.write(invoice_text)

    chk = input("Do you want to print the Order Invoice?(Y/N)")
    if chk.upper() == "Y":
        printInvoice(invoice_file_name)

    # Update the stock in the laptop list
    laptop[3] = str(int(stock) + int(quantity))

    return invoice_file_name
