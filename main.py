from read import *
from update import *
from displayContent import *
from generate_fileName import *
from generate_saleInvoice import *
from generate_orderInvoice import *
from saleInput import *
from orderInput import *
from checkAvailability import *
from matchLaptop import *

# Main program logic


def main():
    laptops = read_laptop_info()

    displayContent(laptops)

    while True:
        chk = input("Do you want to sell a laptop?(Y/N)")
        if chk.upper() != 'Y':
            break
        # Input a laptop sale
        laptop_brand, laptop_name, customer_name, quantity_to_sell = saleInput()

        if checkAvailability(laptop_brand, laptop_name, quantity_to_sell):
            laptop_to_sell = laptops[matchLaptop(laptop_brand, laptop_name)]
            sale_invoice_file = generate_sale_invoice(
                laptop_to_sell, customer_name, quantity_to_sell)
            print(f'Sale Invoice Generated: {sale_invoice_file}')
        else:
            print("Not Available!")

        # Update the laptop stock in the text file
        update_laptop_stock(laptops)

    while True:
        chk = input("Do you want to order a laptop?(Y/N)")
        if chk.upper() != 'Y':
            break

        # Input a laptop order
        laptop_brand, laptop_name, distributor_name, quantity_to_order = orderInput()
        laptop_to_sell = laptops[matchLaptop(laptop_brand, laptop_name)]
        order_invoice_file = generate_order_invoice(
            laptop_to_sell, distributor_name, quantity_to_order)
        print(f'Order Invoice Generated: {order_invoice_file}')

        # Update the laptop stock in the text file
        update_laptop_stock(laptops)


# Run the main program
if __name__ == '__main__':
    main()
