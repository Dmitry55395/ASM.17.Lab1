import pickle
from .dcsh import *

class Catalog:

    def __init__(self):
        self.designer = []     # Инициализация стека

    # 1 - Добавить дизайнера одежды
    def plus_dc(self):
        des_clo = DesignerClothers()  # экземпляр класса
        des_clo.writed()  # заполнение класса данными
        self.designer.append(des_clo)  # добавление информации в стек
        des_clo.info()  # вывод только что введенных данных
        print("Данные добавлены\n")


       # if (input("Создать еще одну запись"))

    # 2 - Добавить дизайнера одежды и обуви
    def plus_dcsh(self):
        des_clo_sh = DesignerCloSH()     # экземпляр класса потомка
        des_clo_sh.writed()              # заполнение класса потомка данными
        self.designer.append(des_clo_sh) # добавление информации в стек
        des_clo_sh.info() # вывод только что введенных данных
        print("Данные о дизайнере добавлены\n")


    # 3 - Вывести список дизайнеров на экран
    def print(self):
        # enumerate - ф-ция позволяет раскладывать список на порядковые
        # номера и соответсвующие им элементы
        print("\nСписок дизайнеров:")
        for i, dept in enumerate(self.designer):
            print("№ ", i)
            dept.console_output()
        print("------Конец списка------\n")


    # 4 - Редактировать данные о дизайнере
    def rewrite(self):
        i = int(input("\nВведите порядковый номер дизайнера в списке: "))
        if i > len(self.designer):
            print("Нет дизайнера с таким порядковым номером\n")
        else:
            print("\nВведите новые значения:")
            self.designer[i].read()
            print("Изменения сохранены\n")

    # 5 - Удалить данные
    def delete(self):
        i = int(input("\nВведите порядковый номер дизайнера в списке:  ", ))
        self.designer.pop(i)

    # 6 - Сохранить список дизайнеров в файл
    def write_file(self):
        with open('data.pkl', 'wb') as f:
            pickle.dump(self.designer, f)
        print("Файл успешно сохранен.\n")

    # 7 - Загрузить список дизайнеров из файла
    def read_file(self):
        print("\nДанные из файла:")
        with open('data.pkl', 'rb') as f:
            data_new = pickle.load(f)

        print(data_new)

    # 8 - Очистить список дизайнеров
    def clear_catalog(self):
        self.designer.clear()  # очистка объекта
        print("Список очещен.\n")



