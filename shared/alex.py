import random

carte_off = []


def gen_carte2(numero_carte, point, n_as):
    if numero_carte == 1:
        print("2")
        point += 2
    if numero_carte == 2:
        print("3")
        point += 3
    if numero_carte == 3:
        print("4")
        point += 4
    if numero_carte == 4:
        print("5")
        point += 5
    if numero_carte == 5:
        print("6")
        point += 6
    if numero_carte == 6:
        print("7")
        point += 7
    if numero_carte == 7:
        print("8")
        point += 8
    if numero_carte == 8:
        print("9")
        point += 9
    if numero_carte == 9:
        print("10")
        point += 10
    if numero_carte == 10:
        print("valet")
        point += 10
    if numero_carte == 11:
        print("dame")
        point += 10
    if numero_carte == 12:
        print("roi")
        point += 10
    if numero_carte == 13:
        print("as")
        n_as += 1
        if point >= 11:
            point += 1
        else:
            point += 11

    return point


def gen_carte(carte_off, point, n_as):
    type_carte = random.randint(1, 4)
    numero_carte = random.randint(1, 13)

    while str(type_carte) + str(numero_carte) in carte_off:
        #print("déjà pris : " + str(type_carte) + str(numero_carte))
        type_carte = random.randint(1, 4)
        numero_carte = random.randint(1, 13)

    if type_carte == 1:
        print("♥ ", end='')

        a = gen_carte2(numero_carte, point, n_as)
        carte_off.append(str(type_carte) + str(numero_carte))

    elif type_carte == 2:
        print("♦ ", end='')

        a = gen_carte2(numero_carte, point, n_as)
        carte_off.append(str(type_carte) + str(numero_carte))

    elif type_carte == 3:
        print("♠ ", end='')

        a = gen_carte2(numero_carte, point, n_as)
        carte_off.append(str(type_carte) + str(numero_carte))

    elif type_carte == 4:
        print("♣ ", end='')

        a = gen_carte2(numero_carte, point, n_as)
        carte_off.append(str(type_carte) + str(numero_carte))

    return a


def croupier(carte_off, n_as):
    pts = 0

    while pts < 17:
        b = gen_carte(carte_off, pts, n_as)
        pts = + b

    return pts


def blackjack(carte_off):
    point = 0
    jouer = 1
    n_as = 0

    while jouer == 1:
        jouer = int(input("1 pour prendre 0 pour passer : "))

        if jouer == 1:
            a = gen_carte(carte_off, point, n_as)
            point = + a

            if point > 21:
                print("OUUUT")
                print("votre somme total : ", point)
                break

            if point == 21:
                print("blakjack win")
                print("votre somme total : ", point)
                break


        elif jouer == 0:

            val = croupier(carte_off, n_as)

            print("votre somme total : ", point)

            print("le croupier à ", val)

            if val > point and val <= 21:
                print("le croupier gagne")
            else:
                print("le joueur gagne")

        else:
            print("erreur")
            jouer = 1

while True:
    blackjack(carte_off)
