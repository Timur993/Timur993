# Создание словаря
relatives = {"Тимур":["Игорь","Борис"],"Сергей":["Андрей","Генадий"],"Дарья":["Борис","Виктор"],"Валентина":["Владимир","Кирилл"],"Ксения":["Николай","Глеб"]}
# Приветствие, Выбор в меню
choise = None
print("Добро пожаловать, я помогу тебе вспомнить имена твоих друзей!")
while choise != 0:
    print("""Выбор опций
0 - Выйти
1 - Добавить новое значение
2 - Найти имя отца и деда по имени реб>нка
3 - Заменить существующее имя отца и деда
4 - Удалить значение
""")
    choise = input("Для выбора опции в меню, нажми соответствующую кнопку: ")
    if choise == "0":
        print("До свидания! ")
        break
    elif choise == "1":
        name = input("Введите имя которое вы хотите добавить: ")
        if name not in relatives:
            father = input("Введите имя отца: ")
            grand = input("Ведите имя деда: ")
            relatives[name] = father, grand
            print("У", name,"(а)", "отца зовут", father, "а деда зовут", grand )
        else:
            print("Такое значение уже есть в словаре")
    elif choise == "2":
        name = input("Введите имя: ")
        if name in relatives:
            father, grand = relatives[name]
            print("Твой друг :", name,"его отца зовут:", father, "а деда:", grand)
        else:
            print("Такого значения нет в словаре, вы можете его добавить")
    elif choise == "3":
        name = input("Введите имя: ")
        if name in relatives:
            relatives[name][0] = input("Введите имя отца:")
            relatives[name][1] = input("Введите имя деда:")
            print("У", name, "(а) отца зовут:", relatives[name][0], "деда зовут:", relatives[name][1])
        else:
            print("Мы не нашли такое значение в словаре.")
    elif choise == "4":
        name = input("Введите имя: ")
        if name in relatives:
            del relatives[name]
            print(name, "Удалён из словаря")
        else:
            print("Мы не нашли такое значение в словаре. ")
    else:
        print("Такой выбор кнопки отсутствует в этом меню")
