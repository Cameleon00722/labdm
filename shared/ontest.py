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




# Game blackjack
def blackjack(deck, reader, writer):
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

        Cj1 = "CARTES JOUEUR: \n"
        writer.write(Cj1.encode())
        #print("CARTES JOUEUR: ")
        #print_cartes(joueur_cartes, False, reader, writer)

        Cj2 = "SCORE JOUEUR = " + str(joueur_score) + " \n"
        writer.write(Cj2.encode())


        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        # Update score
        dealer_score += dealer_card.carte_valeur

        print("CARTES CROUPIER: ")
        if len(dealer_cards) == 1:
            s = "CROUPIER SCORE = " + str(dealer_score) + "\n "
            writer.write(s.encode())
        else:
            s = "CROUPIER SCORE = " + str(dealer_score - dealer_cards[-1].carte_valeur) + "\n "
            writer.write(s.encode())

        if len(dealer_cards) == 2:
            if dealer_cards[0].carte_valeur == 11 and dealer_cards[1].carte_valeur == 11:
                dealer_cards[1].carte_valeur = 1
                dealer_score -= 10

    # Joueur a le blackjack
    if joueur_score == 21:
        s = "Le joueur remporte \n"
        writer.write(s.encode())
        quit()

    # Print dealer et joueur cartes
    s = "CARTES CROUPIER: \n"
    writer.write(s.encode())


    s = "CROUPIER SCORE = " + str( dealer_score - dealer_cards[-1].carte_valeur) + "\n "
    writer.write(s.encode())
    s = " "
    writer.write(s.encode())

    s = "CARTES JOUEUR: \n"
    writer.write(s.encode())

    s = "SCORE JOUEUR = " + str(joueur_score) + " \n"
    writer.write(s.encode())

    while joueur_score < 21:

        # Le joueur prend

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
        s = "CARTES CROUPIER: \n"
        writer.write(s.encode())
        s = "CROUPIER SCORE = "+ str(dealer_score - dealer_cards[-1].carte_valeur) +"\n"
        writer.write(s.encode())


        s = " "
        writer.write(s.encode())

        s = "CARTES JOUEUR: \n"
        writer.write(s.encode())
        s = "SCORE JOUEUR = "+ str(joueur_score) + "\n"
        writer.write(s.encode())



    # Print joueur et delaer cartes
    s = "CARTES JOUEUR: \n"
    writer.write(s.encode())
    s = "SCORE JOUEUR = " + str(joueur_score) + "\n"
    writer.write(s.encode())

    s = " "
    writer.write(s.encode())

    s = "LE CROUPIER REVELE LES CARTES....\n"
    writer.write(s.encode())

    s = "CARTES CROUPIER: \n"
    s = "CROUPIER SCORE = "+ str(dealer_score)+ "\n"
    writer.write(s.encode())


    # Check si le joueur a le blackjack
    if joueur_score == 21:
        s = "Blackjack pour le joueur \n"
        writer.write(s.encode())
        quit()

    # Check si le joueur depasse
    if joueur_score > 21:
        s = " perdu \n"
        writer.write(s.encode())
        quit()

    while dealer_score < 17:


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
        s = "CARTES JOUEUR: \n"

        s = "SCORE JOUEUR = "+ str(joueur_score) + "\n"
        writer.write(s.encode())

        s = " "
        writer.write(s.encode())

        s = "CARTES CROUPIER: \n"
        writer.write(s.encode())

        s = "CROUPIER SCORE = " + str(dealer_score) + "\n"
        writer.write(s.encode())
        print("CROUPIER SCORE = ", dealer_score)

    # Dealer depasse
    if dealer_score > 21:
        s = "LE CROUPIER A DEPASSER!!! VOUS AVEZ GAGNE!!!\n"
        writer.write(s.encode())
        quit()

        # Le dealer a le blackjack
    if dealer_score == 21:
        s = "LE CROUPIER A LE BLACKJACK!!! LE JOUEUR A PERDUE\n"
        writer.write(s.encode())
        quit()

    # Match nul
    if dealer_score == joueur_score:
        s = "MATCH NUL!!!!\n"
        writer.write(s.encode())

    # Joueur Wins
    elif joueur_score > dealer_score:
        s = "LE JOUEUR A GAGNE!!!\n"
        writer.write(s.encode())

        # Dealer Wins
    else:
        s = "LE CROUPIER A GAGNE!!!\n"
        writer.write(s.encode())

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

    blackjack(deck, reader, writer)

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
