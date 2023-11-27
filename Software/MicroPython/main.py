import socket
from servo import Servo
from time import sleep
from wifiAP import apConfig as connect

garra = Servo(pin=2)
muñeca_p = Servo(pin=4)
muñeca_y = Servo(pin=5)
brazo = Servo(pin=18)
antebrazo = Servo(pin=19)
base = Servo(pin=21)
             
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
bufferSize  = 128

connect("ARM_UNAL", "87654321")

def identifier_servo(data):
    string = str(data)
    identifier = string[2:4]
    return identifier
    
def degrades_servo(data):
    string = str(data)
    degrades = string[4:-1]
    return degrades

def exec(data):
    print(data)
    g = int(degrades_servo(data))
    if identifier_servo(data) == "s1":
        print(degrades_servo(data))
        garra.move(g)
    elif identifier_servo(data) == "s2":
        print(degrades_servo(data))
        muñeca_p.move(g)
    elif identifier_servo(data) == "s3":
        print(degrades_servo(data))
        muñeca_y.move(g)
    elif identifier_servo(data) == "s4":
        print(degrades_servo(data))
        brazo.move(g)
    elif identifier_servo(data) == "s5":
        print(degrades_servo(data))
        antebrazo.move(g)
    elif identifier_servo(data) == "s6":
        print(degrades_servo(data))
        base.move(g)
    else:
        print("Unknow data")

sk = socket.socket()
sk.bind(serverAddressPort)
sk.listen(1)
print("Listening on: ", serverAddressPort)

while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(bufferSize)
        if data:
            exec(data)
    conn.close()
