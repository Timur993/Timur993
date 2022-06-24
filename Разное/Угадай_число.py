import random




def instructions():
    """Правила игры"""
    print("Добро пожаловать в игру ’Отгадай число’!")
    print("\nЯ загадал натуральное число от 1 до 100, твоя задача отгадать это число, за фиксированное количество попыток\n")

def ask_number(question,low,high):
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response


def ask_level(question,low,high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def number():
    number = random.randint(1,100)
    return number


def move(level):
    move = None
    while move not in number:
        move = ask_number("Предложите число от 1 до 99: ",1,100)
        if move > number():
            print("Не угадал, бери ниже! ")
        else:
            print("Не угадал, бери выше! ")
        level += 1
        return move


def level():
    level = ask_level("Сколько права на ошибку. от 3 до 9: ",3,9)
    return level


def main():
    instructions()
    level()
    move(level)


main()

input("\n\nHaжмитe Enter. чтобы выйти.")
