import serial
from serial.tools import list_ports
import time

class Test:

    __port = None
    __t_test_lectura = 5
    __escaquers_data = []

    # Sense constuctor
    # Python mola!

    def getTestPort(self, port):

        try:
            # Obre el port COM
            ser = serial.Serial(port, 9600)

            # Llegeix dades del port COM i mostra-les
            while True:
                line = ser.readline().decode().strip()
                print(port + ":" + line)

            # Tancar el port COM
            ser.close()

        except serial.SerialException as e:

            print(f"No es pot obrir el port COM: {e}")

            return False


    def getEscaquersConectats(self):

        # Obtenir una llista dels ports disponibles
        ports = list_ports.comports()

        if not ports:
            print("-----------------------------------")
            print("No s'han trobat ports disponibles.")
            return

        for port in ports:
            # print("-----------------------------------")
            # print("Port device:", f"- {port.device}")
            # print("description", f"- {port.description}")
            # print("manofacturer",f"- {port.manufacturer}")
            # print("name", f"- {port.name}")
            # print("hwid", f"- {port.hwid}")
            # print("vid", f"- {port.vid}")
            # print("pid", f"- {port.pid}")
            # print("serial_number", f"- {port.serial_number}")
            # print("location", f"- {port.location}")
            # print("manufacturer", f"-{port.manufacturer}")
            # print("product", f"- {port.product}")

            # Descartar els ports Bluetooth
            # Els port Bluetooth deixen el test clavat!!!

            if not "Bluetooth" in port.description:
                try:
                    # Provar de connectar-se al port
                    ser = serial.Serial(port.device, 9600)

                    t_inicial = time.time()
                    t_limit = t_inicial + self.__t_test_lectura

                    # Llegeix dades del port durant els segons del test
                    darrera_linia = ''
                    while time.time() < t_limit:
                        line = ser.readline().decode().strip()
                        darrera_linia = port.name + ":" + line

                    # Si s'ha agafat alguna cadena en el port en questio filtrar que la cadena pernanyi a un escaquer

                    if darrera_linia is not None:

                        delimitadors = [":", "@", "#"]
                        segments = [darrera_linia]

                        # Dividir la cadena fent servir cada delimitador
                        for delimitador in delimitadors:
                            nous_segments = []
                            for segment in segments:
                                nous_segments.extend(segment.split(delimitador))
                            segments = nous_segments

                        info =dict(
                            {
                                "port": port.device,
                                "nom": segments[2],
                                "tipus": segments[1],
                                "id": segments[3]
                            }
                        )

                        # Append la info de l'escaquer
                        self.__escaquers_data.append(info)

                    else:
                        print("La transmissió es defectuosa")

                except serial.SerialException as e:
                    print(f"No es pot obrir el port COM: {e}")

        return self.__escaquers_data


    def printSystemPorts(self):

        # Obtenir una llista dels ports disponibles
        ports = list_ports.comports()

        if not ports:
            print("-----------------------------------")
            print("No s'han trobat ports disponibles.")
            return

        print("Els ports següents estan disponibles:")
        for port in ports:
            print("-----------------------------------")
            print("Port device:", f"- {port.device}")
            print("description", f"- {port.description}")
            print("manofacturer",f"- {port.manufacturer}")
            print("name", f"- {port.name}")
            print("hwid", f"- {port.hwid}")
            print("vid", f"- {port.vid}")
            print("pid", f"- {port.pid}")
            print("serial_number", f"- {port.serial_number}")
            print("location", f"- {port.location}")
            print("manufacturer", f"-{port.manufacturer}")
            print("product", f"- {port.product}")

            ##Descartar els ports Bluetooth
            if not "Bluetooth" in port.description:
                print(port.description)
                try:
                    # Provar de connectar-se al port
                    ser = serial.Serial(port.device, 9600)

                    t_inicial = time.time()
                    t_limit = t_inicial + self.__t_test_lectura

                    # Llegeix dades del port durant els segons del test
                    while time.time() < t_limit:
                        line = ser.readline().decode().strip()
                        print(port.name + ":" + line)

                except serial.SerialException as e:
                    print(f"No es pot obrir el port COM: {e}")
            else:
                print("exit")


        print("Final tests Ports---------------------------------")


    def conte_paraula_Bluetooth(cadena):
        if "Bluetooth" in cadena:
            return True
        else:
            return False




