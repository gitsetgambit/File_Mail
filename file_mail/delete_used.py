'''deleting the merged file result.txt in combined folder 
after execution'''

import os


def delete():
    os.remove("C:\\Users\hp\\Desktop\\combined files\\result.txt")
    print("deleted...")


delete()
