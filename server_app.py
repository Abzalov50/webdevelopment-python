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


if __name__ == '__main__':
    server_app()
