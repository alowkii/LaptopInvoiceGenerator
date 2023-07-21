from read import *


def write_text(l_d):
    file = open('laptop.txt', 'w')
    for values in l_d.values():
        file.write(str(values[0])+","+str(values[1]) +
                   ","+str(values[2])+","+str(values[3]))
        file.write("\n")
    file.close()
