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
from filtre import Filtre
from facadelogs import FacadeLogs


class FacadeEscaquer:

    __port = None
    __nom = ""
    __tipus = ""
    __id = ""
    __switch = ""
    __descripcio = ""
    __carpeta = ""


    def __init__(self, port, nom, tipus, id, switch, descripcio, carpeta, nomfile):
        self.port = port
        self.nom = nom
        self.tipus = tipus
        self.id = id
        self.switch = switch
        self.descripcio = descripcio
        self.carpeta = carpeta
        self.nomfile = nomfile

    def executar(self):

        fcl = FacadeLogs(self.carpeta,self.nomfile)
        if fcl.exist_file_log_today():
            print("preparat!")

        linea = ""

        try:
            # Obre el port COM
            ser = serial.Serial(self.port, 9600)

            # Instancia el filtre per vigilar la integritat de la cadena
            filtre = Filtre()

            # Llegeix dades del port COM fins als confins
            # de l'univers
            while True:

                line = ser.readline().decode().strip()
                print(self.getDataHora())

                # Verifica si la cadena te el format adequat i no esta repetida
                if filtre.f_line_t64(line) and linea != line:

                    #obre l'arxiu del dia d'avui i escriu la linia
                    fcl.escriuaarxiuavui(line)

                    print(line)


                    linea = line

                else:
                    print("esperant canvis...")

        except serial.SerialException as e:
            print(f"No es pot obrir el port COM: {e}")



    def getDataHora(self):
        # Obtenir data i hora
        agora = datetime.datetime.now()

        # Formatejar
        data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

        return data_hora_formatada





