from read import *


def checkAvailability(brand, laptop, quantity):
    laptops = read_laptop_info()
    for laptop_info in laptops:
        if brand.lower() in laptop_info:
            if laptop.lower() in laptop_info:
                if int(quantity) <= int(laptop_info[3]):
                    return True

    return False
