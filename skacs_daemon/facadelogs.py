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
import os
from datetime import datetime


class FacadeLogs:

    __folder = ""
    __nom = ""
    __perdurabilitat = ""

    __file_config = None
    __ruta_arxiu = None

    __shutup = True

    __lectura = None


    def __init__(self, lectura = None):
        self.__file_config = 'config.ini'
        self.__lectura = lectura
        self.setConfig()


    def setConfig(self):
        config = configparser.ConfigParser()
        config.read(self.__file_config)
        self.__folder = config.get("logs", "folder")
        self.__nom = config.get("logs", "nom")
        self.__perdurabilitat= config.get("logs", "perdurabilitat")

        self.__ruta_arxiu = os.path.join(os.getcwd(), self.__folder)
        nomfinal = self.__nom + self.getDataHora()
        self.__ruta_arxiu = os.path.join(self.__ruta_arxiu, nomfinal)

        # Si no hi arxiu amb data d'avui prepara el nom i la ruta on enregistrar els logs

        if self.existeixFitxerAmbDataDavui():

            pass

        else:

            try:
                # Obre l'arxiu en mode d'escriptura ('a' per afegir)
                with open(self.__ruta_arxiu, 'a') as arxiu:
                    arxiu.close()
            except Exception as e:
                print("error d'escriptura")


    def set_linia(self, lectura):
        try:
            with open(self.__ruta_arxiu, 'a') as arxiu:
                arxiu.write(lectura + "\n")
                arxiu.close()
        except Exception as e:
                print("Error al escriure al fitxer", str(e))


    #Revisa si hi ha un arxiu a la carpeta de logs del dia d'avui
    def existeixFitxerAmbDataDavui(self):
        # Obtener la fecha actual
        fecha_actual = datetime.now().date()

        # Iterar sobre los archivos en la carpeta
        for nombre_archivo in os.listdir(self.__folder):
            ruta_archivo = os.path.join(self.__folder, nombre_archivo)
            if os.path.isfile(ruta_archivo):
                # Obtener la fecha de modificación del archivo
                fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_archivo)).date()
                if fecha_modificacion == fecha_actual:
                    return True  # Si hay un archivo con fecha de modificación igual a la fecha actual, retornar True

        return False  # Si no se encuentra ningún archivo con fecha de modificación igual a la fecha actual, retornar False

    def getDataHora(self):
        # Obtenir data i hora
        agora = datetime.now()
        # Formatar
        data_hora_formatada = agora.strftime("%d%m%Y")
        return data_hora_formatada
