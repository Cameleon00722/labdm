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


class Joueur:
    def __init__(self, name):
        self.mainJ = []

        self.name = name

        self.score = 0

    def getMainJ(self):
        return self.mainJ

    def getScore(self):
        return self.score

    def setScore(self, add):
        self.score = add

    def setMainJ(self, lst_main):
        self.mainJ = lst_main

# liste des tables de jeux , sous tab de la classe = joueur
tableaudetable = []



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

def gen_carte2(numero_carte, point, n_as, reader, writer):
    if numero_carte == 1:
        s = "2"
        writer.write(s.encode())
        point += 2
    if numero_carte == 2:
        s = "3"
        writer.write(s.encode())
        point += 3
    if numero_carte == 3:
        s = "4"
        writer.write(s.encode())
        point += 4
    if numero_carte == 4:
        s = "5"
        writer.write(s.encode())
        point += 5
    if numero_carte == 5:
        s = "6"
        writer.write(s.encode())
        point += 6
    if numero_carte == 6:
        s = "7"
        writer.write(s.encode())
        point += 7
    if numero_carte == 7:
        s = "8"
        writer.write(s.encode())
        point += 8
    if numero_carte == 8:
        s = "9"
        writer.write(s.encode())
        point += 9
    if numero_carte == 9:
        s = "10"
        writer.write(s.encode())
        point += 10
    if numero_carte == 10:
        s = "valet"
        writer.write(s.encode())
        point += 10
    if numero_carte == 11:
        s = "dame"
        writer.write(s.encode())
        point += 10
    if numero_carte == 12:
        s = "roi"
        writer.write(s.encode())
        point += 10
    if numero_carte == 13:
        s ="AS"
        writer.write(s.encode())
        n_as += 1

        if point >= 11:
            point += 1
        else:
            point += 11

    return point


def gen_carte(carte_off, point, n_as, reader, writer):
    type_carte = random.randint(1, 4)
    numero_carte = random.randint(1, 13)

    while str(type_carte) + str(numero_carte) in carte_off:
        type_carte = random.randint(1, 4)
        numero_carte = random.randint(1, 13)


    if type_carte == 1:
        s = "Coeur"
        writer.write(s.encode())

        a = gen_carte2(numero_carte, point, n_as, reader, writer)
        carte_off.append(str(type_carte) + str(numero_carte))

    elif type_carte == 2:
        s = "Carreau"
        writer.write(s.encode())

        a = gen_carte2(numero_carte, point, n_as, reader, writer)
        carte_off.append(str(type_carte) + str(numero_carte))

    elif type_carte == 3:
        s = "Pique"
        writer.write(s.encode())

        a = gen_carte2(numero_carte, point, n_as, reader, writer)
        carte_off.append(str(type_carte) + str(numero_carte))

    elif type_carte == 4:
        s = "Trèfle"
        writer.write(s.encode())

        a = gen_carte2(numero_carte, point, n_as, reader, writer)
        carte_off.append(str(type_carte) + str(numero_carte))

    return a


def croupier(carte_off, n_as):
    pts_Croupier = 0

    while pts_Croupier < 17:
        GainPts = gen_carte(carte_off, pts_Croupier, n_as)
        pts_Croupier = + GainPts

    return pts_Croupier





async def joueur_request(reader, writer):

    partie = False

    joueur = str(writer.get_extra_info('peername')[0])
    mess = "Bienvenue\n"
    writer.write(mess.encode())
    data = await reader.read(256)
    nomTab = data.decode().strip('NAME ')
    indextable = 0
    for i in tableaudetable:
        if i.nom == nomTab and i.getTemps() > 0:
            partie = True
            i.ajouter_table(joueur)
            if i.getTable()[0] != joueur :
                while i.getTemps() != 0:
                    messte = "Temps restants avant connexion : "+str(i.getTemps()) +"\n"
                    writer.write(messte.encode())
                    await asyncio.sleep(1)
            else :
                while i.getTemps() != 0:
                    messte = "Temps restants avant connexion : "+str(i.getTemps()) +"\n"
                    writer.write(messte.encode())
                    await asyncio.sleep(1)
                    i.setTemps(i.getTemps() - 1)
            mess2 = "Connexion a la table réussi!\n"
            writer.write(mess2.encode())
            mess2 = ".\n"
            writer.write(mess2.encode())
            break
        indextable+=1
    if partie == False:
        test = "END"
        writer.write(test.encode())
        writer.close()

#################### black jack ###########################""
    carte_off = []
    JBlack = Joueur(joueur)

    jouer = 1
    Nombre_As = 0

    while partie:

        data = await reader.read(256)
        if reader.at_eof() :
           print(f"Socket closed by user {joueur}")
           data = b"END"
        message = data.decode().strip()

        if message == "END":
            mess = f"User {joueur} leave the server2."
            print(mess)
            for z in tableaudetable[indextable].lst_table :
                if z == joueur :
                    tableaudetable[indextable].lst_table.remove(joueur)
            writer.write(message.encode())
            writer.close()
            break

        if message == "MORE 1":
            mess = f"utilisateur {joueur} prend une carte."
            print(mess)

            a = gen_carte(carte_off, JBlack.getScore(), Nombre_As, reader, writer)
            JBlack.setScore(a)
            s = str(JBlack.getScore())
            writer.write(s.encode())

            if JBlack.getScore() > 21:
                s = "OOUUUT"
                writer.write(s.encode())
                s = "votre somme total : " + str(JBlack.getScore())
                s = "Coeur"
                writer.write(s.encode())
                break

            if JBlack.getScore() == 21:
                s = "blakjack win"
                writer.write(s.encode())
                s = "votre somme total : " + str(JBlack.getScore())
                writer.write(s.encode())
                break

        if message == "MORE 0":
            mess = f"utilisateur {joueur} ne prend pas de carte."
            print(mess)

            val = croupier(carte_off, Nombre_As)

            s = "Votre somme total : " + str(JBlack.getScore())
            writer.write(s.encode())


            s = "le croupier à " + str(val)
            writer.write(s.encode())

            if val > JBlack.getScore() and val <= 21:
                s = "le croupier gagne"
                writer.write(s.encode())
            else:
                s = "le joueur gagne"
                writer.write(s.encode())

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
