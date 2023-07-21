# Display the available laptops
def displayContent(laptops):
    print('Available Laptops:')
    for laptop in laptops:
        print(', '.join(laptop) + "\t")
