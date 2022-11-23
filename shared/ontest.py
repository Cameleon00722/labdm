import asyncio
import random



class table:
    def __init__(self, nom, temps):
        # nom de la table
        self.nom = nom

        # liste des tables existantes
        self.lst_table = []

        # timer
        self.temps = temps

    def getTable(self):
        return self.lst_table

    def getTemps(self):
        return self.temps

    def getNom(self):
        return self.nom

    def setTemps(self, var):
        self.temps = var

    def ajouter_table(self, add_table):
        self.lst_table.append(add_table)

    def affiche(self):
        print("Nom de la table =", self.nom, "liste des joueurs =", self.lst_table, "temps =", self.temps)

class Cartes:
    def __init__(self, suite, valeur, carte_valeur):
        # Suite des carte tel que coeur pique ...
        self.suite = suite

        # Représentation des cartes Roi, As ...
        self.valeur = valeur

        # Valeur des cartes
        self.carte_valeur = carte_valeur


class Joueur:
    def __init__(self, name):
        self.mainJ = []

        self.name = name

        self.score = 0

    def getMainJ(self):
        return self.mainJ

    def getScore(self):
        return self.score

    def setMainJ(self, lst_main):
        self.mainJ = lst_main

# liste des tables de jeux , sous tab de la classe = joueur
tableaudetable = []

# Affiché la carte
def print_cartes(cartes, dissimuler):
    s = ""
    for carte in cartes:
        s = s + "\t ________________"
    if dissimuler:
        s += "\t ________________"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|                |"
    print(s)

    s = ""
    for carte in cartes:
        if carte.valeur == '10':
            s = s + "\t|  {}            |".format(carte.valeur)
        else:
            s = s + "\t|  {}             |".format(carte.valeur)
    if dissimuler:
        s += "\t|                |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|      * *       |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|    *     *     |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|       {}        |".format(carte.suite)
    if dissimuler:
        s += "\t|          *     |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|         *      |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|        *       |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|                |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimuler:
        s += "\t|                |"
    print(s)

    s = ""
    for carte in cartes:
        if carte.valeur == '10':
            s = s + "\t|            {}  |".format(carte.valeur)
        else:
            s = s + "\t|            {}   |".format(carte.valeur)
    if dissimuler:
        s += "\t|        *       |"
    print(s)

    s = ""
    for carte in cartes:
        s = s + "\t|________________|"
    if dissimuler:
        s += "\t|________________|"
    print(s)

    print()


# Game blackjack
def blackjack(deck):
    # Cartes du joueur et dealeur

    joueur = Joueur("test")

    joueur_cartes = joueur.getMainJ()
    dealer_cards = []

    # Score du joueur et dealer
    joueur_score = joueur.getScore()
    dealer_score = 0

    while len(joueur_cartes) < 2:

        joueur_carte = random.choice(deck)
        joueur_cartes.append(joueur_carte)
        deck.remove(joueur_carte)

        joueur_score += joueur_carte.carte_valeur

        if len(joueur_cartes) == 2:
            if joueur_cartes[0].carte_valeur == 11 and joueur_cartes[1].carte_valeur == 11:
                joueur_cartes[0].carte_valeur = 1
                joueur_score -= 10

        print("CARTES JOUEUR: ")
        print_cartes(joueur_cartes, False)
        print("SCORE JOUEUR = ", joueur_score)

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        # Update score
        dealer_score += dealer_card.carte_valeur

        print("CARTES CROUPIER: ")
        if len(dealer_cards) == 1:
            print_cartes(dealer_cards, False)
            print("CROUPIER SCORE = ", dealer_score)
        else:
            print_cartes(dealer_cards[:-1], True)
            print("CROUPIER SCORE = ", dealer_score - dealer_cards[-1].carte_valeur)

        if len(dealer_cards) == 2:
            if dealer_cards[0].carte_valeur == 11 and dealer_cards[1].carte_valeur == 11:
                dealer_cards[1].carte_valeur = 1
                dealer_score -= 10

    # Joueur a le blackjack
    if joueur_score == 21:
        print("Le joueur remporte")
        quit()

    # Print dealer et joueur cartes
    print("CARTES CROUPIER: ")
    print_cartes(dealer_cards[:-1], True)
    print("CROUPIER SCORE = ", dealer_score - dealer_cards[-1].carte_valeur)

    print()

    print("CARTES JOUEUR: ")
    print_cartes(joueur_cartes, False)
    print("SCORE JOUEUR = ", joueur_score)

    while joueur_score < 21:
        choice = input("Entrez P pour Prendre ou R pour Rester : ")

        if choice.upper() != 'P' and choice.upper() != 'R':
            print("erreur input merci de recommencer")

        # Le joueur prend
        if choice.upper() == 'P':

            joueur_carte = random.choice(deck)
            joueur_cartes.append(joueur_carte)
            deck.remove(joueur_carte)

            # Update joueur score
            joueur_score += joueur_carte.carte_valeur

            c = 0
            while joueur_score > 21 and c < len(joueur_cartes):
                if joueur_cartes[c].carte_valeur == 11:
                    joueur_cartes[c].carte_valeur = 1
                    joueur_score -= 10
                    c += 1
                else:
                    c += 1

            # Print joueur et dealer cartes
            print("CARTES CROUPIER: ")
            print_cartes(dealer_cards[:-1], True)
            print("CROUPIER SCORE = ", dealer_score - dealer_cards[-1].carte_valeur)

            print()

            print("CARTES JOUEUR: ")
            print_cartes(joueur_cartes, False)
            print("SCORE JOUEUR = ", joueur_score)

        # Si joueur reste
        if choice.upper() == 'R':
            break

    # Print joueur et delaer cartes
    print("CARTES JOUEUR: ")
    print_cartes(joueur_cartes, False)
    print("SCORE JOUEUR = ", joueur_score)

    print()
    print("LE CROUPIER REVELE LES CARTES....")

    print("CARTES CROUPIER: ")
    print_cartes(dealer_cards, False)
    print("CROUPIER SCORE = ", dealer_score)

    # Check si le joueur a le blackjack
    if joueur_score == 21:
        print("LE JOUEUR A LE BLACKJACK")
        quit()

    # Check si le joueur depasse
    if joueur_score > 21:
        print("LE JOUEUR A DEPASSER!!! PERDU!!!")
        quit()

    while dealer_score < 17:

        print("LE CROUPIER DECIDE DE PRENDRE.....")

        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        dealer_score += dealer_card.carte_valeur

        # Update score
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].carte_valeur == 11:
                dealer_cards[c].carte_valeur = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1

        # print joueur et dealer cartes
        print("CARTES JOUEUR: ")
        print_cartes(joueur_cartes, False)
        print("SCORE JOUEUR = ", joueur_score)

        print()

        print("CARTES CROUPIER: ")
        print_cartes(dealer_cards, False)
        print("CROUPIER SCORE = ", dealer_score)

    # Dealer depasse
    if dealer_score > 21:
        print("LE CROUPIER A DEPASSER!!! VOUS AVEZ GAGNE!!!")
        quit()

        # Le dealer a le blackjack
    if dealer_score == 21:
        print("LE CROUPIER A LE BLACKJACK!!! LE JOUEUR A PERDUE")
        quit()

    # Match nul
    if dealer_score == joueur_score:
        print("MATCH NUL!!!!")

    # Joueur Wins
    elif joueur_score > dealer_score:
        print("LE JOUEUR A GAGNE!!!")

        # Dealer Wins
    else:
        print("LE CROUPIER A GAGNE!!!")

async def croupier_request(reader, writer):
    mess = "Bienvenue\n"
    writer.write(mess.encode())
    data = await reader.read(256)
    nomTab = data.decode().strip('NAME ')

    mess2 = "La nom de la table à été enregistrer \n"
    writer.write(mess2.encode())
    data = await reader.read(256)
    tempsStr = data.decode().strip('TIME ')
    tempsDef = int(tempsStr)
    writer.close()

    tab = table(nomTab, tempsDef)
    # tab.affiche()

    tableaudetable.append(tab)

    for i in tableaudetable:
        i.affiche()


# while (temps[len(temps)-1]!=0) :
#	await asyncio.sleep(1)
#	temps[len(temps)-1]=temps[len(temps)-1]-1
# print("done")


async def joueur_request(reader, writer):
    joueur = str(writer.get_extra_info('peername')[0])
    mess = "Bienvenue\n"
    writer.write(mess.encode())
    data = await reader.read(256)
    nomTab = data.decode().strip('NAME ')
    for i in tableaudetable:
        if i.nom == nomTab and i.getTemps() > 0:
            i.ajouter_table(joueur)
            if i.getTable()[0] == joueur :
                while i.getTemps() != 0:
                    print(i.getTemps())
                    await asyncio.sleep(1)
                    i.setTemps(i.getTemps() - 1)
            mess2 = "Connexion a la table réussi!\n"
            writer.write(mess2.encode())
            mess2 = ".\n"
            writer.write(mess2.encode())


    suites = ["♠", "♥", "♣", "♦"]

    # Valeur des suites
    suites_valeur = {"♠": "\u2664", "♥": "\u2661", "♣": "\u2667", "♦": "\u2662"}

    # Types de cartes
    cartes = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Valeur des cartes
    cartes_valeurs = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                      "Q": 10, "K": 10}

    # Le deck des cartes
    deck = []

    # Boucle pour tout type de suites
    for suite in suites:

        # Boucle pour tous les types de cartes dans une suite
        for carte in cartes:
            # Ajouter la carte au deck
            deck.append(Cartes(suites_valeur[suite], carte, cartes_valeurs[carte]))

    blackjack(deck)
    
    while True:
        data = await reader.read(256)
        message = data.decode()

        if reader.at_eof() :
           print(f"Socket closed by user {joueur}")
           data = b"quit"
           message = data.decode().strip()
        if message == "quit":
            message = f"User {joueur} leave the server."
            print(message)
            #await forward(writer, "Server", message)
            #users.remove(writer)
            writer.close()
            break

        if message == "MORE 1":
            message = f"utilisateur {joueur} prend une carte."
            print(message)
            #await forward(writer, "Server", message)
            #code à implémenté

        if message == "MORE 0":
            message = f"utilisateur {joueur} ne prend pas de carte."
            print(message)
            #await forward(writer, "Server", message)
            #code à implémenté

        print(message)
        #await forward(writer, addr, message)



async def server():
    # start a socket server
    serverCR = await asyncio.start_server(croupier_request, '0.0.0.0', 668)
    serverJR = await asyncio.start_server(joueur_request, '0.0.0.0', 667)

    async with serverCR:
        await serverCR.serve_forever()
    async with serverJR:
        await serverJR.serve_forever()


if __name__ == '__main__':
    asyncio.run(server())
