from .Smartphone import Smartphone
from .Phone import Phone
import pickle
import os

class Devices:

    def __init__(self):
        self.dev_list = []
        self.data_file = 'st43/dev_list.pkl'



    def add_phone(self):
        p = Phone()
        p.set_data()
        self.dev_list.append(p)
        print("\nDone!\n")



    def add_smartphone(self):
        sp = Smartphone()
        sp.set_data()
        self.dev_list.append(sp)
        print("\nDone!\n")



    def delete_device(self):
        if len(self.dev_list) != 0:
            el = int(input("Delete element №:"))-1
            if (el >= 0) and (el < len(self.dev_list)):
                self.dev_list.pop(el)
                print("\nDone!\n")
        else:
            print("\nList is empty!\n")



    def edit_device(self):
        if len(self.dev_list) != 0:
            el = int(input("Edit element №:"))-1
            if (el >= 0) and (el < len(self.dev_list)):
                self.dev_list[el].edit_data()
            else:
                print("\nWrong key\n")
        else:
            print("\nList is empty!\n")



    def display_list(self):
        if len(self.dev_list) != 0:
            i = 1
            for el in self.dev_list:
                print("*"*10, i, "*"*10)
                el.display_data()
                print("*"*23+"\n")
                i+=1
        else:
            print("\nList is empty!\n")



    def clear_list(self):
        if len(self.dev_list) != 0:
            self.dev_list.clear()
            print("\nDone!\n")
        else:
            print("\nList is already empty!\n")



    def write_list(self):
        if len(self.dev_list) != 0:
            pickle.dump(self.dev_list, open(self.data_file, "wb"))
            print("\nDone!\n")
        else:
            print("\nList is empty!\n")



    def read_list(self):
        self.dev_list = pickle.load(open(self.data_file, "rb"))
        print("\nDone!\n")
 
