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




async def joueur_request(reader, writer):

    partie = True

    joueur = str(writer.get_extra_info('peername')[0])
    mess = "Bienvenue\n"
    writer.write(mess.encode())
    data = await reader.read(256)
    nomTab = data.decode().strip('NAME ')
    co = 0
    indextable = 0
    for i in tableaudetable:
        if i.nom == nomTab and i.getTemps() > 0:
            co = 1
            i.ajouter_table(joueur)
            if i.getTable()[0] != joueur :
                while i.getTemps() != 0:
                    messte = "Temps restants avant connexion :"+str(i.getTemps()) +"\n"
                    writer.write(messte.encode())
                    await asyncio.sleep(1)
            else :
                while i.getTemps() != 0:
                    messte = "Temps restants avant connexion :"+str(i.getTemps()) +"\n"
                    writer.write(messte.encode())
                    await asyncio.sleep(1)
                    i.setTemps(i.getTemps() - 1)
            mess2 = "Connexion a la table réussi!\n"
            writer.write(mess2.encode())
            mess2 = ".\n"
            writer.write(mess2.encode())
            break
        indextable+=1
    if co == 0 :
        partie=False
        test = "END"
        writer.write(test.encode())
        writer.close()


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
            #await forward(writer, "Server", message)
            #code à implémenté

        if message == "MORE 0":
            mess = f"utilisateur {joueur} ne prend pas de carte."
            print(mess)
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
