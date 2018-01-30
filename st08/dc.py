class DesignerClothers(): # родительский класс

    def __init__(self):  # конструктор
        self.named = None
        self.experience  = None
        self.quantity_clothers  = None

    def writed (self):   # запись данных
        print("Введите данные о дизайнере")
        print("------------------------------------")
        self.named = input("Имя дизайнера: ")  # имя дизайнера
        self.experience = input("Стаж работы: ")  # стаж дизайнера
        self.quantity_clothers = input("Количество созданных коллекций одежды: ")  # количесво колекций дизайнера

    def info(self):    # отображение записанных данных
        print("------------------------------------")
        print("Вы ввели")
        print("Дизайнер: " + self.named)
        print("Стаж работы: " + self.experience)
        print("Коллекции одежды (показов): " + self.quantity_clothers)
