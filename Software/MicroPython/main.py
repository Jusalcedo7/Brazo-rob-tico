import socket
from servo import Servo
from time import sleep

'''
motor = Servo(pin=2)
while True:
    motor.move(0)
    sleep(1)
    motor.move(90)
    sleep(1)
    motor.move(180)
    sleep(1)
    motor.move(90)
    sleep(1)
    motor.move(0)
    sleep(1)
    
garra = Servo(pin=2)
muñeca_pitch = Servo(pin=4)
muñeca_yaw = Servo(pin=25)
brazo = Servo(pin=26)
antebrazo = Servo(pin=#)
base = Servo(pin=#)
'''

# Agregar nport de donde está el servidor TCP, en el ejemplo: 3000
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
# Cantidad de bytes a recibir
bufferSize  = 128

# Descomentar si el esp32 será una estación
# from wifiSTA import connectSTA as connect

# Descomentar si el esp32 estará en modo de acceso AP
from wifiAP import apConfig as connect

# poner acá el nombre de red ssid y password para conectarse
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
    if identifier_servo(data) == "s7":
        print(degrades_servo(data))
    elif identifier_servo(data) == "s6":
        print(degrades_servo(data))
    elif identifier_servo(data) == "s5":
        print(degrades_servo(data))
    elif identifier_servo(data) == "s4":
        print(degrades_servo(data))
    elif identifier_servo(data) == "s2":
        print(degrades_servo(data))
    elif identifier_servo(data) == "s1":
        print(degrades_servo(data))
    else:
        print("Otro")

sk = socket.socket()
sk.bind(serverAddressPort)
sk.listen(1)
print("Listening on: ", serverAddressPort)

while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(bufferSize)
        # Si dato fue recibido, se decide que hacer con el.
        if data:
            exec(data)
            # Con la siguiente instruccion se pueden enviar datos al
            # dispositivo conectado
            conn.sendall("ok")
            # conn.send("ok")
    conn.close()