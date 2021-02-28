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


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: {0}".format(reply))
                print("Sending: {0}".format(reply))

            conn.sendall(str.encode(reply))
        except:
            break


current_player = 0

while True:
    conn, addr = s.accept()
    print("Connected to: {0}".format(addr))

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
