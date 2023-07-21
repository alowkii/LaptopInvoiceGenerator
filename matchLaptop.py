from read import *


def matchLaptop(laptop_brand, laptop_name):
    laptops = read_laptop_info()
    print(laptops)
    for itr in range(len(laptops)):
        if laptop_brand.lower() in laptops[itr]:
            if laptop_name.lower() in laptops[itr]:
                return itr
