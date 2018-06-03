class Phone:
    def __init__(self):
        self.vendor = None
        self.model = None

    def set_vendor(self):
        self.vendor = input("Set vendor: ")

    def set_model(self):
        self.model = input("Set model: ")

    def set_data(self):
        self.set_vendor()
        self.set_model()

    def display_data(self):
        print("Vendor: " + self.vendor)
        print("Model: " + self.model)

    def edit_data(self):
        switch = {"1": ("Vendor", self.set_vendor),
                  "2": ("Model", self.set_model),
                  "3": ("Exit", "")}
        while True:
            print("\nEdit:")
            for key in switch:
                print(key + " " + switch[key][0])
            choice = input()
            if choice in ('1','2'):
                switch[choice][1]()
            elif choice == '3':
                break
            else:
                print("\nWrong key, try again\n")
        print("\nDone!\n")