import socket
import threading
from tkinter import Tk, Label, Entry, Button, Text, END

server_address = ('localhost', 5000)

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            chat_area.insert(END, f'{data.decode("utf-8")}\n')
        except:
            break

def send_message():
    name = name_entry.get()
    message = message_entry.get()
    message_entry.delete(0, END)
    if message:
        client_socket.send(f'{name}: {message}'.encode('utf-8'))
        chat_area.insert(END, f'{name}: {message}\n')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

threading.Thread(target=receive_messages).start()

window = Tk()
window.title('Cliente de chat')

chat_area = Text(window, width=50, height=20)
chat_area.pack()

name_label = Label(window, text='Nombre:')
name_label.pack()

name_entry = Entry(window)
name_entry.pack()

message_entry = Entry(window)
message_entry.pack()

send_button = Button(window, text='Enviar', command=send_message)
send_button.pack()

window.mainloop()
