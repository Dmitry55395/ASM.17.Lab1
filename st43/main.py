from .Devices import Devices

def main():

    devices = Devices()

    menu = {
        "1": ("Add phone", devices.add_phone),
        "2": ("Add smartphone", devices.add_smartphone),
        "3": ("Edit device", devices.edit_device),
        "4": ("Delete device", devices.delete_device),
        "5": ("Display list", devices.display_list),
        "6": ("Read list from file", devices.read_list),
        "7": ("Write list to file", devices.write_list),
        "8": ("Clear list", devices.clear_list),
        "9": ("Exit", "")
    }

    while True:
        for key in menu:
            print(key + ":  " + menu[key][0])
        el = input()
        if el in ("1","2","3","4","5","6","7","8"):
            menu[el][1]()
        elif el == "9":
            break
        else:
            print("\nWrong key, try again\n")
