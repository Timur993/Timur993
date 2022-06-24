import random

should_continue = True
while should_continue:
    your_choise = input('Камень/Ножницы/Бумага! R/S/P : ').lower()
    if your_choise not in ['r', 's', 'p']:
        print('Нет такого пункта, попробуй ещё')
        continue

    choise = {1: 'r', 2: 's', 3: 'p'}
    computer = choise[random.randint(1, 3)]
    print(f'Comp choise = {computer}')
    winning_combs = [('p', 'r'), ('r', 's'), ('s', 'p')]

    if your_choise == computer:
        print('Draw')
    elif (your_choise, computer) in winning_combs:
        print('You win!')
    else:
        print('You lost!')
    should_continue = input('Do you want to continue? [y/n]').lower() == 'y'




