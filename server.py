import socket
import threading
from tkinter import Tk, Label, Entry, Button

server_address = ('localhost', 5000)

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            for client in clients:
                if client != client_socket:
                    client.send(data)
        except:
            break

    client_socket.close()
    clients.remove(client_socket)

def start_server():
    global clients

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    clients = []

    while True:
        client_socket, address = server_socket.accept()
        print(f'Conectado con {address}')
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

    server_socket.close()

window = Tk()
window.title('Servidor de chat')

label = Label(window, text='Puerto:')
label.pack()

entry_port = Entry(window)
entry_port.pack()

button = Button(window, text='Iniciar servidor', command=start_server)
button.pack()

window.mainloop()
