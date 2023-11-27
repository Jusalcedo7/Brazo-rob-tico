import socket # Comunicación en red.
from servo import Servo # Controlar servomotores.
from time import sleep # Pausas en el programa.
from wifiAP import apConfig as connect # Configurar la conexión Wi-Fi en modo punto de acceso.


# Crea objetos Servo para diferentes componentes del brazo robótico.
garra = Servo(pin=2)
muñeca_p = Servo(pin=4)
muñeca_y = Servo(pin=5)
brazo = Servo(pin=18)
antebrazo = Servo(pin=19)
base = Servo(pin=21)


# Define la dirección y el puerto del servidor para la comunicación por socket.
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]

# Define el tamaño del búfer para recibir datos.
bufferSize  = 128

# Asigna SSID a la red wifi generada.
connect("ARM_UNAL", "87654321")


# Función para extraer el identificador del servo de los datos recibidos.
def identifier_servo(data):
    string = str(data)
    identifier = string[2:4]
    return identifier


# Función para extraer el valor de los grados del servo de los datos recibidos.
def degrades_servo(data):
    string = str(data)
    degrades = string[4:-1]
    return degrades


# Función para ejecutar el movimiento del servo e imprimir los datos recibidos.
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


# Crea un objeto de socket para establecer y gestionar conexiones.
sk = socket.socket()

# Enlaza el socket a la dirección y puerto del servidor.
sk.bind(serverAddressPort)

# Configura el socket para escuchar conexiones entrantes con una cola de 1.
sk.listen(1)

print("Listening on: ", serverAddressPort)


while True:
    # Acepta una conexión y obtiene el socket del cliente y la dirección.
    conn, addr = sk.accept() 
    while True:
        # Recibe continuamente los datos del cliente con el tamaño de búfer especificado.
        data = conn.recv(bufferSize)
        if data:
            # Si se reciben datos, ejecuta la función para manejar los servos.
            exec(data)
    conn.close()
