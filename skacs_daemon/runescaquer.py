'''
This file is part of Skacs.
Foobar is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Skacs is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Skacs.
If not, see <https://www.gnu.org/licenses/>.
'''



import serial
import datetime
import pygame

from facadelogs import FacadeLogs

class RunEscaquer():

    __port = ""
    __nom = ""
    __tipus = ""
    __id = ""

    __lectura = ""

    def __init__(self, port=None, nom=None, tipus=None, id=None, lectura=None):
        self.port = port
        self.nom = nom
        self.tipus = tipus
        self.id = id
        self.lectura = lectura

    # Getter y setter para __port
    def get_port(self):
        return self.__port

    def set_port(self, port):
        self.__port = port

    # Getter y setter para __nom
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    # Getter y setter para __tipus
    def get_tipus(self):
        return self.__tipus

    def set_tipus(self, tipus):
        self.__tipus = tipus

    # Getter y setter para __id
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    # Getter y setter per __lectura
    def get_lectura(self):
        return self.__lectura

    def set_lectura(self, lectura):
        self.__lectura = lectura

    def print_values(self):
        print("Port:", self.__port)
        print("Nom:", self.__nom)
        print("Tipus:", self.__tipus)
        print("id:", self.__id)
        print("Lectura:", self.__lectura)





    def executar(self):

        try:
            # Connectar-se.
            # print("Serial POrt:" , self.port)
            ser = serial.Serial(self.__port, 9600)

            linia_anterior = None

            faclogs = FacadeLogs()

            while True:

                linia = ser.readline().decode().strip()



            # Si s'ha agafat alguna cadena en el port en qüestio filtrar que la cadena pernanyi a un escaquer
                if linia is not None and self.isGoodLine(linia) and linia != linia_anterior:

                    print("skac!")
                    '''
                    print("tipus", linia.split('@')[0])
                    print("nom", linia.split('@')[1].split('#')[0])
                    print("id", linia.split('@')[1].split('#')[1])
                    '''
                    self.reproducir_wav("sound.wav")


                    print(self.getDataHora(), linia.split('@')[1].split('#')[2])
                    self.set_lectura(linia.split('@')[1].split('#')[2])
                    linia_anterior = linia


                    linia = self.getDataHora() + linia
                    faclogs.set_linia(linia)

                else:
                    print(self.getDataHora(), linia)

        except serial.SerialException as e:\
            print(f"No es pot obrir el port COM: {e}")


    def getDataHora(self):
        # Obtenir data i hora
        agora = datetime.datetime.now()

        # Formatejar
        data_hora_formatada = agora.strftime("%d/%m/%Y#%H:%M:%S#")

        return data_hora_formatada


    def isGoodLine(self,linia):

        # Separar la cadena en 4 parts
        parts = linia.split('@')
        if len(parts) != 2:
            return False
        middle_parts = parts[1].split('#')
        if len(middle_parts) != 3:
            return False
        # Comprovar si l'última part té una longitud de 64
        if len(middle_parts[-1]) != 64:
            return False
        if len(middle_parts[-1]) == 64:
            self.lectura=middle_parts[-1]

        return True


    def reproducir_wav(self,arxiu):
        # Inicializar pygame
        pygame.init()

        try:
            # Cargar el archivo WAV
            pygame.mixer.music.load(arxiu)

            # Reproducir el archivo WAV
            pygame.mixer.music.play()

            # Esperar a que termine de reproducirse
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except pygame.error as error:
            print("Error al reproducir el archivo:", error)

        # Detener la mezcla de audio y salir
        pygame.mixer.quit()


