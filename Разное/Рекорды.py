# Рекорды
# Демонстрируем списочные методы
scores = []
choise = None
while choise != 0:
    print(
        """
    Рекорды
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорды
    3 - Удалить рекорды
    4 - Сортировать рекорды
    """
    )
    choise = input("Ваш выбор: ")
    # Выход
    if choise == "0":
        print("До Свидания")
        break
    # Показать рекорды
    elif choise == "1":
        print("Рекорды")
        for score in scores:
            print(score)
    # Добавить рекорды
    elif choise == "2":
        score = int(input("Введите новый рекорд: "))
        scores.append(score)
    # Удалить рекорды
    elif choise == "3":
        score = int(input("Какой из рекордов вы хотите удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат", score, "не содержится в списке рекордов.")
    # Сортировать рекорды
    elif choise == "4":
        scores.sort(reverse=True)
    else:
        print("Извините, в меню нет такого пункта", choise)
        input("Ваш выбор: ")
