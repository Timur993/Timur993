import random
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
jumble = ""
score = 0
tries = 1
while len(word) != 0:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print("Привет! Вот анаграмма :", jumble)
guess = input("\n\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("К сожалению вы не отгадали. ")
    guess = input("Попробуйте отгадать исходное слово: ")
    tries += 1
    if tries == 2:
        print("Вот вам подсказка, первые три буквы слова: ", correct[:2])
if guess == correct:
    if tries == 1:
        score += 10
    elif tries == 2:
        score += 8
    elif tries == 3:
        score += 6
    elif tries == 4:
        score += 2
    print("Да! Именно так! Вы отгадали! У вас ушло на это", tries, "попыток и вы заработали",
          score, "очков! Поздравляю!")
