# rezo

***Serveur Blackjack***

Le but de ce DM est d'écrire un serveur pour un jeu simplifié de blackjack en suivant un protocole fourni. Un lab est proposé contenant une machine server sur lequel lancer votre application, ainsi que 6 machines pc1 à pc6 sur lesquelles vous pourrez faire tourner des clients. Deux applications clientes sont fournies ("shared/croupier.py") et ("shared/joueur.py").

Vous devrez programmer ce serveur en python en utilisant l'API asyncio vue en TP.

1. Le lab et le serveur

 La machine server du lab doit héberger le serveur, qui sera lancé au démarrage (commande à décommenter dans "server.startup"). Le code du serveur est contenu dans un fichier "serverblackjack.py" placé dans le répertoire "shared" du lab. Au lancement, le serveur se positionne en écoute sur les ports 667 et 668. Un croupier ("shared/croupier.py"), exécuté depuis une des 6 autres machines, se connecte au serveur et l'échange permet au croupier de donner au serveur les paramètres de la table de jeu que le serveur va ensuite créer. La connexion se termine une fois les paramètres transmis. Un joueur ("shared/joueur.py"), exécuté depuis une des 6 autres machines, se connecte au serveur, rejoint une table et joue.

 Le serveur doit pouvoir gérer un nombre arbitraire de tables en attente de joueurs ou en cours de jeu, et un nombre arbitraire de joueurs par table.

2. Le jeu

 On joue avec un paquet de 52 cartes classiques : 4 couleurs, 13 cartes par couleur (cf https://fr.wikipedia.org/wiki/Jeu_de_cartes_fran%C3%A7ais).
 Lorsqu'un joueur se connecte au serveur, il donne un nom de table auquel il souhaite se connecter. Cette table doit avoir été créée par un croupier auparavant. S'il est le premier joueur à cette table, une attente débute pendant un temps passé en paramètre lors de la création de la table. Pendant ce temps, d'autres joueurs peuvent se connecter à la même table. Une fois ce délai passé, il ne sera plus possible de rejoindre la table.
 Le serveur prend alors un jeu de 52 cartes, qu'il mélange puis donne une carte à chaque joueur, prend une carte et recommence l'opération, de sorte que chaque joueur a 2 cartes ainsi que le donneur. Le but du jeu est de constituer un ensemble de cartes dont la valeur totale est la plus grande possible tout en restant inférieure ou égale à 21. Seule la première carte du donneur est connue des joueurs. Partant de ses 2 cartes, chaque joueur peut choisir de continuer à prendre des cartes une par une et de s'arrêter lorsqu'il le souhaite. S'il dépasse 21, il a perdu, s'il s'arrête avant, le donneur doit retourner sa seconde carte puis à son tour prendre des cartes une par une et s'arrêter lorsqu'il le souhaite. Si le donneur non plus n'a pas dépassé 21, le joueur gagne s'il a un meilleur total que le donneur, fait match nul en cas d'égalité et perd sinon. Dans une table à plusieurs joueurs, tous les joueurs jouent avant que le donneur ne retourne sa seconde carte et complète éventuellement sa main.
  La stratégie du donneur est fixée : il s'arrête s'il a 17 ou plus et prend une carte sinon.
  Les valeurs des cartes ne dépendent pas de la couleur :
 - les as valent 1 ou 11, on choisit la valeur la plus favorable;
 - les dix, valets, dames ou rois valent 10;
 - les autres cartes valent leur chiffre, par exemple le sept de pique vaut 7.

Une fois la partie démarrée sur une table, pour chaque joueur successivement :
 - le serveur envoie au joueur la liste de ses cartes, ainsi que la première carte du donneur;
 - le serveur demande au joueur s'il souhaite une carte supplémentaire;
 - le joueur demande une carte ou s'arrête;
 - on répète ces 3 opérations jusqu'à ce que le joueur décide de s'arrêter.
Quand tous les joueurs ont joué, le donneur joue à son tour en prenant des cartes tant qu'il n'a pas atteint 17, puis il informe les joueurs du résultat.

3. Le protocole

On implémente un protocole textuel avec des messages de trois types :
1) "COMMAND" où "COMMAND" est une commande parmi {END, .};
2) "COMMAND value" où "COMMAND" est une commande parmi {NAME, TIME, MORE} et "value" est un paramètre (éventuellement vide) transmis sous forme de chaîne de caractères;
3) une chaîne de caractères quelconque.
Dans le cas du 3ème type, la syntaxe est libre. En revanche, dans le second cas, "value" est un paramètre de la commande envoyée par le client. Sauf précision dans le corps du sujet, les messages envoyés consistent en une unique ligne terminée par un "\n".

 3.1 Le croupier comme client
  Lorsqu'un croupier se connecte sur le port 668 du serveur, le serveur envoie un message de bienvenue. Le croupier répond avec la commande NAME suivie du nom de la table que le croupier veut créer. Le serveur confirme la réception et attend ensuite le délai (en secondes) que le croupier veut fixer entre la connexion d'un premier joueur et le début de la partie. Le croupier répond avec la commande TIME suivie du délai.
  Le rôle du croupier s'arrête ici.

 3.2 Le joueur comme client
  Lorsqu'un joueur se connecte sur le port 667 du serveur, le serveur envoie un message de bienvenue. Le joueur répond avec la commande NAME suivie du nom de la table que le joueur veut rejoindre. Si aucune table ouverte ne correspond, le serveur termine l'échange avec la commande END. Sinon, il enregistre le joueur comme participant à cette table. Si c'est le premier joueur à cette table, l'attente d'autres joueurs commence et se terminera à la fin du délai passé en paramètre à la table. Une fois le délai passé, il n'est plus possible de se connecter et la partie commence. Le serveur distribue puis communique avec chaque joueur :
  - le serveur donne au joueur la liste des cartes du joueur, le score correspondant ainsi que la première carte du donneur. Il attend ensuite de savoir si le joueur veut une carte supplémentaire. Cela peut se faire en plusieurs messages et se termine par la commande '.'
  - le joueur répond par la commande MORE suivie de 1 pour une carte, 0 sinon.
  - ces étapes sont répétées jusqu'à ce que le joueur s'arrête
  - si le joueur a dépassé 21, le serveur lui donne le résultat.
  Une fois que tous les joueurs ont joué, le serveur choisit lui même de prendre des cartes tant qu'il n'a pas atteint au moins 17. Il annonce ensuite le résultat à chaque joueur :
  - le serveur envoie ses cartes et son score ainsi que le résultat puis termine avec la commande END
  - le serveur ferme la connexion avec le joueur
  Le serveur supprime finalement la table.

4. Attendus du serveur
 - Le serveur doit pouvoir gérer toutes les demandes de connexion de manière concurrente, il doit être possible de créer plusieurs tables et plusieurs parties peuvent être en cours à un moment donné.
 - Chaque table ne peut accueillir qu'une partie et doit être supprimée à la fin de celle-ci.
 - Les tours de jeu des joueurs doivent se faire de manière concurrente sans ordre établi entre eux.

5. Travail demandé

Vous écrirez le code du serveur dans un fichier "serverblackjack.py". Il doit pouvoir interagir avec les clients proposés comme exemples (fichier "/shared/croupier.py" et "/shared/joueur.py" dans le lab).

6. Réalisation, retour et évaluation

Le travail est à effectuer en binôme ou individuellement. Vous écrirez un unique fichier "serverblackjack.py" que vous placerez dans une archive "prenom1-nom1.prenom2-nom2.tar.gz (en remplaçant prénoms et noms par ceux de votre binôme) à déposer au plus tard le 27 novembre 2022 à 23h59 dans le dépôt prévu à cet effet sur la page celene. Tous les binômes sont autorisés y compris entre Ingé et MIAGE, mais chaque binôme doit rendre un et un seul devoir.

Des pénalités seront appliquées en cas de retard, d'archive mal formée (il ne faut pas mettre le lab dans l'archive !) ou mal nommée...

L'évaluation sera réalisée en testant et en lisant votre code, le test aura lieu dans un lab similaire à celui qui vous est fourni.

Le but est de fournir une application fonctionnelle : en cas d'erreur ou de message d'erreur sur une fonctionnalité, il n'y aura pas de point au titre de l'esthétique, de l'originalité ou d'un code partiellement correct.
