import random
print("\t This is the age of the computer")
print("\n The computer should impress us... the Man")

# User chooses the number
the_number = int(input("Human Choose a number between 0 and 100 "))
tries = 1
computer = random.randint(0, 100)
# User choose again loop
while the_number > 100:
    the_number = int(input("I thought Humans are smarter than that... \nRetype the number... "))
    if the_number <= 100:
        print("Good")

# Guessing Loop
while computer != the_number:
    if computer > the_number:
        print(computer, "lower... Mr. Computer")
    else:
        print(computer, "higher... Mr. Computer")
    computer = int(random.randint(0, 100))
    tries += 1

print("Computer Congratulations... You beat the human! The Number was ", the_number)
print("It only took a computer such as yourself", tries, "tries to guess it right...          pathetic")
input("\nPress the enter key to exit.")
