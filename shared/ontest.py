import asyncio


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


# while (temps[len(temps)-1]!=0) :
#	await asyncio.sleep(1)
#	temps[len(temps)-1]=temps[len(temps)-1]-1
# print("done")


async def joueur_request(reader, writer):
    mess = "Bienvenue\n"
    writer.write(mess.encode())
    data = await reader.read(256)
    nomTab = data.decode().strip('NAME ')
    for i in tableaudetable:
        if i.nom == nomTab and i.getTemps() > 0:
            i.ajouter_table(writer)
            if i.getTable()[0] == writer:
                while i.getTemps() != 0:
                    print(i.getTemps())
                    await asyncio.sleep(1)
                    i.setTemps(i.getTemps() - 1)
                for z in i.lst_table:
                    print(z)
                    

    while True:
        data = await reader.readline()

        if reader.at_eof() :
            print(f"Socket closed by user {addr}")
            data = b"quit"
        message = data.decode().strip()

        if message == "quit":
            message = f"User {addr} quit the chat."
            print(message)
            await forward(writer, "Server", message)
            users.remove(writer)
            writer.close()
            break

        if message == "MORE 1":
            message = f"utilisateur {addr} prend une carte."
            print(message)
            await forward(writer, "Server", message)
            #code à implémenté

        print(message)
        await forward(writer, addr, message)


async def server():
    # start a socket server
    serverCR = await asyncio.start_server(croupier_request, '0.0.0.0', 668)
    serverJR = await asyncio.start_server(joueur_request, '0.0.0.0', 667)

    async with serverCR:
        await serverCR.serve_forever()  # handle requests for ever
    async with serverJR:
        await serverJR.serve_forever()


if __name__ == '__main__':
    asyncio.run(server())
