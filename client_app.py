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


if __name__ == '__main__':
    client_app()
