from .Phone import Phone


class Smartphone(Phone):
    def __init__(self):
        super().__init__()
        self.battery = None
        self.camera_res = None

    def set_battery(self):
        self.battery = input("Set battery: ")

    def set_camera_rez(self):
        self.camera_res = input("Set camera resolution: ")

    def set_data(self):
        super().set_data()
        self.set_battery()
        self.set_camera_rez()

    def display_data(self):
        super().display_data()
        print("Battery: " + self.battery)
        print("Camera resolution: " + self.camera_res)

    def edit_data(self):
        switch = {"1": ("Vendor", self.set_vendor),
                  "2": ("Model", self.set_model),
                  "3": ("Battery", self.set_battery),
                  "4": ("Camera resolution", self.set_camera_rez),
                  "5": ("Exit", "")}
        while True:
            print("\nEdit:")
            for key in switch:
                print(key + " " + switch[key][0])
            choice = input()
            if choice in ('1','2','3','4'):
                switch[choice][1]()
            elif choice == '5':
                break
            else:
                print("\nWrong key, try again\n")
        print("\nDone!\n")





