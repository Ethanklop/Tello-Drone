# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess

# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host, port)
tello_address = ('192.168.10.1', 8889)  # Get the Tello drone's address

# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep=6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)


# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....

def firstHoop():
    sendmsg('up 40')
    sendmsg('forward 210')


def secondHoop():
    sendmsg('go 250 0 60 60')


def thirdhoop():
    sendmsg('ccw 90')
    sendmsg('forward 250')
    sendmsg('ccw 90')
    sendmsg('forward 125')


def fourthhoop():
    sendmsg('250 0 -60 60')


print("\nEthan Klopschinski")
print("Program Name: Tello Drone Training School")
print("Date: 11.9.2020 ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
print("\n****CHECK IF CO-PILOT IS READY****")

ready = input('\nAre you ready to take flight: ')

try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')

        firstHoop()

        secondHoop()

        thirdhoop()

        fourthhoop()


        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
# etihad


























