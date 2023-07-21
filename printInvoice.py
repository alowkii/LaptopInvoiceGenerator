def printInvoice(fileName):
    with open("Invoice/"+fileName, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
