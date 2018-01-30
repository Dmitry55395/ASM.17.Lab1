from .dc import *


class DesignerCloSH(DesignerClothers):  # класс потомок

    def __init__(self):  # конструктор
        super().__init__() #обращение к родительску классу
        self.quantity_shoes = None
        self.university = None

    def writed(self): # запись данных
        super().writed()
        print("Введите данные о дизайнере")
        self.quantity_shoes = input("Количество созданных коллекций обуви: ")
        self.university = input("Университет: ")


    def info(self):  # отображение записанных данных
        print("Вы ввели")
        print("------------------------------------")
        super().info()   #данные  из родительского класса
        print("Коллекции обуви (показы): " + self.quantity_shoes)
        print("Высшее образование получено в: " + self.university)


