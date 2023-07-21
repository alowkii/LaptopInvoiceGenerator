# Function to update the laptop stock in the text file
def update_laptop_stock(laptops):
    with open('laptop.txt', 'w') as file:
        for laptop in laptops:
            file.write(', '.join(laptop) + '\n')
