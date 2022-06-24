import random
words = ("table", "lesson", "chair", "work", "grandfather", "grandmother",
         "coffee", "brain", "elevator", "pumpkin", "lemongrass", "orange")
word = random.choice(words)
so_far = "-" * len(word)
correct = ""
tries = 0
print("Добро пожаловать в игру угадай слово. Я загадал случайно слово "
      "из своего словаря. Тебе нужно его отгадать, а я тебе в этом помогу")
print("Длина загаданного слова - ", len(word))
while tries != 5:
    print("\nОтгаданное вами слово сейчас выглядит так: ", so_far)
    x = str(input("Введите букву : "))
    if x in word:
        print("Эта буква присутствует в слове")
        new = ""
        for i in range(len(word)):
            if x == word[i]:
                new += x
            else:
                new += so_far[i]
        so_far = new
    else:
        print("Данной буквы в слове нет.")
    tries += 1
if tries == 5:
    print("\nОтгаданное вами слово сейчас выглядит так: ", so_far)
    correct = str(input("\nВы истратили все 5 попыток. Пришло время угадать слово: "))
    if correct == word:
        print("\n\nПоздравляю, вы угадали, моё слово действительно было ", word)
    else:
        print("\n\nВы не угадали слово, не огорчайтесь")
input("\nPress Enter to exit")
