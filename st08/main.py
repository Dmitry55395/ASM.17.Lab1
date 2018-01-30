from .catalog import Catalog

cat = Catalog() # экземпляр класса

user_menu = {"1": ("Добавить дизайнера одежды", cat.plus_dc),
        "2": ("Добавить дизайнера одежды и обуви",  cat.plus_dcsh),
        "3": ("Вывести список дизайнеров на экран", cat.print),
        "4": ("Редактировать данные о дизайнере", cat.rewrite),
        "5": ("Удалить данные из списка", cat.delete),
        "6": ("Сохранить список дизайнеров в файл", cat.write_file),
        "7": ("Загрузить список дизайнеров из файла", cat.read_file),
        "8": ("Очистить список дизайнеров", cat.clear_catalog),
        "9": ("Выход", None)}


def main():
    print('===================================================')
    print('               КАРТОТЕКА ДИЗАЙНЕРОВ                ')
    print('===================================================')
    while True:
        for key in sorted(user_menu.keys()):
            print(key + ":" + user_menu[key][0])
        print('===================================================')

        ans = input("Выберете пункт меню: ")
        if int(ans) == 9:
            break
        elif int(ans) > 9:
            print("Такого пункта нет в меню.\n")
            print("")
        else:
            user_menu[ans][1]()




if __name__ == "__main__":
    main()

