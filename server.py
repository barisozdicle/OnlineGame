import socket
from _thread import *
import sys

server = "192.168.1.50"
port = 5555

# AF_INET SOCK_STREAM bunlar baglanti cesitleri
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Server'a kac kisi baglansin biz burada 2 kisi verdik
s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: {0}".format(reply))
                print("Sending: {0}".format(reply))

            conn.sendall(str.encode(reply))
        except:
            break


while True:
    conn, addr = s.accept()
    print("Connected to: {0}".format(addr))

    start_new_thread(threaded_client, (conn,))
