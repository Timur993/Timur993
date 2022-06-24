scores = []
choise = None
while choise != 0:
    print(
        """
    Рекорды 2.0
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорды
    """
    )
    choise = input("Ваш выбор:")
    print()
    if choise == "0":
        print("До свидания")
        break
    elif choise == "1":
        print("Рекорды\n")
        print("Имя\t\tРезультат")
        for entry in scores:
            name, score = entry
            print(name, "\t", score)
    elif choise == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (name, score)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("Извините в меню нет пункта", choise)
