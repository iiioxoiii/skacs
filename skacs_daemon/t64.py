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

import configparser

class T64:

    __status = {}
    __taulell = {
        "A1": 0, "A2": 1, "A3": 2, "A4": 3, "A5": 4, "A6": 5, "A7": 6, "A8": 7,
        "B1": 8, "B2": 9, "B3": 10, "B4": 11, "B5": 12, "B6": 13, "B7": 14, "B8": 15,
        "C1": 16, "C2": 17, "C3": 18, "C4": 19, "C5": 20, "C6": 21, "C7": 22, "C8": 23,
        "D1": 24, "D2": 25, "D3": 26, "D4": 27, "D5": 28, "D6": 29, "D7": 30, "D8": 31,
        "E1": 32, "E2": 33, "E3": 34, "E4": 35, "E5": 36, "E6": 37, "E7": 38, "E8": 39,
        "F1": 40, "F2": 41, "F3": 42, "F4": 43, "F5": 44, "F5": 45, "F7": 46, "F8": 47,
        "G1": 48, "G2": 49, "G3": 50, "G4": 51, "G5": 52, "G6": 53, "G7": 54, "G8": 55,
        "H1": 56, "H2": 57, "H3": 58, "H4": 59, "H5": 60, "H6": 61, "H7": 62, "H8": 63,
    }

    __liniaEntrada = None
    __nomEscaquer = None

    def __init__(self,entrada):
        self.__liniaEntrada=entrada

    # Retorna la cadena en brut enviada des de l'escaquer
    def getRAW(self):
        return self.__taulell

    def setRAW(self):
        numerobitcasella = self.getbitcasella(casella)

    def getstatus(self,entrada):
        return self.status

    # Configuracio del sistema
    def llegirconfig(self, arxiu):
        # Crie um parser de configuracio
        config = configparser.ConfigParser()
        # Llegir arxiu de configuracio
        config.read(arxiu)
        # Retorna la base de dades com un diccionari
        return dict(config['database'])

        # Configuracio del sistema

    def setconfig(self, arxiu):
        # Crie um parser de configuracio
        config = configparser.ConfigParser()
        # Llegir arxiu de configuracio
        config.read(arxiu)
        # Retorna la base de dades com un diccionari
        return dict(config['database'])

