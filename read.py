# Function to read the laptop information from the text file
def read_laptop_info():
    laptops = []
    with open('laptop.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            laptop_info = line.strip().split(',')
            for itr in range(len(laptop_info)):
                laptop_info[itr] = laptop_info[itr].strip().lower()
            laptops.append(laptop_info)
    return laptops
