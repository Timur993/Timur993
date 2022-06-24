import turtle as tur


def stars():
    """Function draws star with 5 tops
    return: star with 5 tops"""
    for moves in range(5):
        tur.forward(50)
        tur.right(180-180/5)


stars()


def stars2():
    """Function draws star with 11 tops
    return: star with 11 tops"""
    for moves in range(11):
        tur.forward(50)
        tur.right(180-180/11)


stars2()


def stars3(n):
    """Function draws star with n tops
    return: star with n tops"""
    for moves in range(n):
        tur.forward(50)
        tur.right(180-180/n)


stars3(int(input('Number of star vertices: ')))