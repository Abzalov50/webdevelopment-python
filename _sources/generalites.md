# Généralités sur la programmation web en Python

## Permettez-moi de vous introduire au Web

Le **Web** (ou **World-Wide Web** ou **WWW** ou **W3**) est un système né vers 1990. Il a été développé par Tim Berners-Lee, initialement pour *faciliter la collaboration entre les membres de la communauté de Physique des Hautes Energies*. Il devait permettre un échange efficace d'information. La même information (en forme et fond) devait être accessible par tous les membres utilisant différents appareils. 

Tim développa 3 technologies afin de supporter son concept de Web :
- **HTML** (HyperText Markup Language): Langage de formatage de texte pour le Web.
- **URL** (Uniform Resource Identifier): Adresse unique identifiant chaque ressource sur le Web. L'URI est communément appelé URL, même si on pourrait faire une nuance entre les deux. 
- **HTTP** (HyperText Transfer Protocol): Protocole d'échange de documents sur le Web. 

Le concept était tellement général qu'il a pu être étendu à travers Internet. Aujourd'hui, tout le monde utilise le Web. Tous les sites internet sont accessibles via le Web. <br>
Dans la pratique, *si vous voulez accéder à une ressource sur le Web (un site web, par exemple), il faut que vous ayez accès à une architecture* ***client-serveur*** :
> Le client reçoit votre requête, la transmet au serveur. Le serveur traite cette requête, et envoie une réponse au client, à laquelle vous avez directement accès. Le client avec lequel vous interagirez le plus souvent est le navigateur internet (tel que Google Chrome, Mozilla Firefox, Safari, Microsoft Edge,...). Par conséquent, vous avez accès au Web à partir de tout appareil qui dispose d'un navigateur internet (PC, Mac, Smartphone, Tablette,...). 

En 1999, le concept de **Web 2.0** a été introduit par Darcy DiNucci, et rendu populaire par Tim O’Reilly et Dale Doughtery. ***La principale fonctionnalité du Web 2.0 est la possibilité offerte à l'utilisateur de contribuer en modifiant ou en ajoutant du contenu au site Web existant, plutôt que de juste consulter**. (Facebook est un exemple d'application de cette fonctionnalité). Ici, on passe de la notion de "**site Web**" à la notion d'**application Web**. Application parce que l'utilisateur peut contribuer au développement, à travers l'ajout de contenu (réseaux sociaux, wikis, forums,...) et à travers les infos générées par ma simple navigation (e-commerce).

Une ***application mobile*** est un logiciel développé pour un appareil électronique mobile, tel que le PDA, le smartphone, la tablette,... L'application mobile est donc intimement liée au système d'exploitation du mobile (Android, iOS, Windows Phone, Blackberry OS, Chrome OS, etc.). On dit "application Android", "application iOS", etc. 

Le Web est accessible via les appareils mobiles ; il suffit d'avoir une application client, telle que Firefox. C'est cette possibilité d'accéder au Web à partir de tout type d'appareils électroniques (mobile et PC), qui lui confère toute sa puissance.

> Avec le Web 2.0, les applications Web sont tout aussi (voire plus) puissantes que les applications Mobile.

## Mais, quelle est la différence entre Internet et Web ?

**Internet** est un ensemble d'ordinateurs et d'autres appareils électroniques interconnectés de diverses manières, notamment via les fils de cuivre, la fibre optique et les communications sans fil (WiFi).

Internet est né à la fin des années 60, donc bien avant le Web. Il s'appelait d'abord **ARPANET**, c'est-à-dire ***réseau d'ARPA***. ARPA (Advanced Research Projects Agency, US) a développé Internet dans le but de fournir une *interconnexion sécurisé* à l'armée américaine, en cas de guerre nucléaire. Initialement développé pour un ensemble restreint d'équipements, Internet est aujourd'hui utlisé à travers le monde et connecte des millions de machines {cite}`scobey17`. Nous sommes tous connectés !

Le Web est certainement le système de collaboraton le plus connu et le plus utilisé à travers Internet, sinon les échanges via Internet se font par principe via les [**sockets**](socks).

## Revenons plus en détail sur l'architecture Client/Serveur

L'architecture client-serveur est une approche (parmi tant d'autres) de communication entre deux applications logicielles qui résident généralement (mais pas toujours) sur des machines physiquement distinctes.

La {numref}`Figure %s <arch-client-serveur>` présente un modèle d'architecture client-serveur ([Source](https://info.blaisepascal.fr/nsi-sockets-python)). Cette figure montre 3 clients A, B et C en communicaton (via des requêtes et réponses) avec un (le même) serveur. Le serveur est représenté comme une unité centrale, car c'est la partie calcul du serveur qui nous intéresse plutôt que l'affichage.

```{figure} /_static/arch-clientserveur.png
:name: arch-client-serveur

Un modèle d'architecture client-serveur.
```

En général, une infinité de clients peuvent potentiellement se connecter au même serveur, et le serveur doit, de façon constante et cohérente, répondre à chaque requête. Il faut donc 2 types d'application pour entretenir cette communication :

- L'application côté serveur, ou simplement application "**serveur**" : qui attend (ou *écoute*) les requêtes client.
- Les applications côté client, ou simplement applications "**clients**" : qui se connectent au serveur (le navigateur Web, Skype, WhatsApp, Outlook sont des exemples de clients). 

Pour que le serveur reconnaisse précisément que tel client a envoyé telle requête, il lui faut avoir une information unique au client. De même pour que le client sache précisément quel serveur lui a envoyé une réponse donnée, il lui faut avoir une information unique au serveur. Cette information est appelée une **adresse IP** (ou **nom d'hôte** ou **host name**, en anglais), qui identifie une machine sur un réseau, qu'il soit local ou internet. Toute machine connectée à un réseau a donc un nom unique. Par exemple, aujourd'hui 01 octobre 2022, le serveur servant la page `google.ci` (son nom d'hôte) a comme adresse IP : `142.250.201.163`. Vous conviendrez avec moi que le nom d'hôte est plus facile à retenir que l'adresse IP :smiley: . 

Toutefois, cette seule information n'est pas suffisante pour permettre une communication cohérente. Pourquoi ? Vous souvenez qu'on a mis ***clients*** au pluriel ? On veut dire que sur une même machine peut résider plusieurs clients. N'avez-vous pas sur votre PC plusieurs navigateurs (Google Chome, Mozilla Firefox, Microsoft Edge, Apple Safari, ...), une application de messagerie (telle que Outlook), des applications de discussion instantanée (telle que Skype ou Signal) ? Toutes ces applications sont des clients. Aussi, l'adresse IP ne suffit pas pour identifier une application spécifique. Pour ce faire, on a recours à la notion de **numéro de port** (ou simplement **port**). L'application serveur à un port sur la machine-serveur. Chaque application-client a un port sur la machine-client. Le couple `(adresse, port)` représente un **socket** (Voir {numref}`Figure %s <fig-socket>`).

```{figure} /_static/fig-socket.png
:name: fig-socket

Un modèle de communication client-serveur via les sockets.
```

Afin d'uniformiser la communication via internet, certains protocoles ont été développés, notamment les protocoles de la pile TCP/IP. Ces protocoles fixent des numéros de port pour certains types de services (qui peuvent eux-mêmes être réglementés par des protocoles). Par exemple :

- Le port `80` est dédié au protocole HTTP (non sécurisé) et le port `443` est dédié au protocole HTTPS (la version sécurisée de HTTP).
- Le port `23` est dédié au service telnet.
- Le port `21` est dédié au protocole FTP d'échange de fichiers.
- Le port `22` est dédié au service de connexion Shell sécurisée.

(socks)=

## Les sockets Python

Un socket est un point de terminaison d'un canal de communication bidirectionnel entre le serveur et le client. Dans cette section, nous apprenons à développer une petite application client-serveur, dont les différentes étapes sont les suivantes :

1. Le serveur s'exécute et attend une connexion.
2. Le client initie la communication, et envoie une requête.
3. Le serveur répond précisément aux requêtes reçues.
4. Le client termine si l'utilisateur entre "Au revoir" comme requête. Le serveur s'arrête également (facultatif).

### Le programme serveur
```{code-cell} ipython3
import socket

def server_app():
    host = socket.gethostname()  # Obtenir le nom d'hôte de la machine serveur
    port = 8000  # Brancher le serveur à un port supérieur à 1024
    
    serv_socket = socket.socket()  # Créer un objet `socket'
    serv_socket.bind( (host, port) )  # Associer l'objet au socket
    
    serv_socket.listen(2)  # Spécifier le nombre de requêtes simultanées que le serveur peut traiter
    conn, address = serv_socket.accept()  # Le serveur est prêt à accepter une connexion
    print('#### Aide :')
    print('Pour arrêter le serveur, appuyer la touche Entrée sans saisir de texte, ou entrer "Au revoir" sans les guillemets.')
    print('####\n\n')
    print('Connexion depuis l\'adresse : {0}'.format(address))
    
    # Lancer la boucle de traitement des requêtes
    while True:
        req = conn.recv(1024).decode()  # Requête limitée à 1024 octets
        
        if not data:
            # Si aucune donnée, arrêter le serveur
            break
        print("Données reçues de l'utilisateur connecté : {0}".format(data))
        data = input(' >> ')
        conn.send(data.encode()) # Envoyer une réponse au client
    
    conn.close()  # Fermer la connexion à l'arrêt de la boucle de traitement.

"""
if __name__ == '__main__':
    server_app()
"""
```
### Le programme client
```{code-cell} ipython3
import socket


def client_app():
    host = socket.gethostname()  # Puisque le serveur et le client logent sur la même machine
    port = 5000  # Port auquel est connecté le serveur

    client_socket = socket.socket()  # Création du socket client
    client_socket.connect((host, port))  # connexion au serveur

    message = input(" -> ")

    while message.lower().strip() != 'au revoir':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Données envoyées par le serveur {0}: '.format(data)) 

        message = input(" -> ")

    client_socket.close()

"""
if __name__ == '__main__':
    client_app()
"""

```

```{bibliography}
```
