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
import time
import threading

from runescaquer import RunEscaquer
from test import Test





def main():

    test = Test()
    ## test.getTestPort("COM11")
    # test.printSystemPorts()
    pintaBanner()

    print("Benvingut a Skacs!!")
    print("<Inici del procès de configuració>")
    input("<prem una tecla per continuar>")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("IMPORTANT!!! Connecta l'escaquer o escaquers a els ports USB de l'ordinador abans de continuar. \n")
    print(":) \n")
    input("<prem una tecla per continuar>")
    print("configurant...")
    for segon in range(10, 0, -1):
        print(f"un momentet: {segon} segons", end='\r')
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    escaquers_conectats = test.getEscaquersConectats()
    print (escaquers_conectats)

    # Nom de l'arxiu de configuracio
    file_config = 'config.ini'
    config = configparser.ConfigParser()
    config.read(file_config)

    if escaquers_conectats is None:
        print("No s'ha detectat cap escaquer")
    else:
        for escaquer in escaquers_conectats:
            # Definicio d'una seccio de configuracio per cada escaquer
            num_escaquer = 1
            nom_seccio_escaquer = "escaquer_"+ str(num_escaquer)

            if config.has_section(nom_seccio_escaquer):
                config.remove_section(nom_seccio_escaquer)

            config.add_section(nom_seccio_escaquer)

            for clau, valor in escaquer.items():
                config.set(nom_seccio_escaquer, clau, valor)
                print(clau + ": " + valor)

            num_escaquer += 1

    # Mira si la secció logs de l'arxiu de configuracio existeix. Si no, el crea
    if not config.has_section("logs"):
        config.add_section("logs")
        config.set("logs", "folder", "logs")
        config.set("logs", "nom", "skacs")
        config.set("logs", "perdurabilitat", "30")

    # Mira si la secció MySQL de l'arxiu de configuracio existeix. Si no el crea
    if not config.has_section("MySQL"):
        config.add_section("MySQL")
        config.set("MySQL", "host", "")
        config.set("MySQL", "user", "")
        config.set("MySQL", "password", "")
        config.set("MySQL", "database", "")

    with open(file_config, 'w') as configfile:
        config.write(configfile)

    # Configuracio de la carpeta logs

    file_config = 'config.ini'
    config = configparser.ConfigParser()
    config.read(file_config)
    nom_carpeta = config.get("logs", "folder")

    if not carpetaLogsExisteix(nom_carpeta):
        # print("Creació de carpeta 'logs'")
        creaCarpeta(nom_carpeta)

    ########
    # Carrega la configuració dels escaquers de la pàgina config.ini
    escaquers = buscar_escaquers(file_config)

    for escaquer in escaquers:

        esc=RunEscaquer()

        p = config.get(escaquer, "port")
        esc.set_port(p)
        t = config.get(escaquer, "tipus")
        esc.set_tipus(t)
        n = config.get(escaquer, "nom")
        esc.set_nom(n)
        id = config.get(escaquer, "id")
        esc.set_id(id)

        esc.executar()
        ##

    '''
    # -------------------------------------------------------------------------------------------
    # Crear un semàfor
    semaphore = threading.Semaphore(1)  # Inicialitzar amb 1 per permetre només un fil a la vegada
    # Per cada escaquer llençar un tread
    # Crear i iniciar fils
    threads = []
    for escaquer in escaquers:

        ##


        thread = threading.Thread(target=llegir_escriure_arxiu, name=escaquer, args=(semaphore, 'arxiu.txt', "asdasdadadadad"))
        threads.append(thread)
        thread.start()



    # Esperar que tots els fils finalitzin
    for thread in threads:
        thread.join()
    print("Tots els fils han finalitzat la seva execució.")
    '''


# Funció per llegir i escriure en un arxiu
def llegir_escriure_arxiu(semaphore, nom_arxiu, cadena):
    with semaphore:  # Bloquejar l'accés al semàfor
        print(f"Fil {threading.current_thread().name} ha agafat el semàfor i està llegint/escribint l'arxiu.")
        # Simular la lectura i escriptura de l'arxiu
        with open(nom_arxiu, 'a') as file:
            file.write(threading.current_thread().name + '\n')

        print(f"Fil {threading.current_thread().name} ha alliberat el semàfor.")


def buscar_escaquers(config_file):
    parser = configparser.ConfigParser()
    parser.read(config_file)

    escaquers_encontrados = []

    # Iterar sobre todas las secciones
    for section in parser.sections():
        # Comprobar si la sección comienza con "escaquer-"
        if section.startswith("escaquer_"):
            escaquers_encontrados.append(section)

    return escaquers_encontrados


# Retorna True si la carpeta existeix
def carpetaLogsExisteix(nom_carpeta):
    directori_projecte = os.getcwd()  # Obtenim el directori del projecte actual
    ruta_carpeta = os.path.join(directori_projecte, nom_carpeta)  # Creem la ruta completa de la carpeta

    return os.path.isdir(ruta_carpeta)  # Retorna True si la carpeta existeix, False altrament

# Crea una carpeta amb el nom de l'arxiu de config
def creaCarpeta(nom_carpeta):
    directori_projecte = os.getcwd()  # Obtenim el directori del projecte actual
    ruta_carpeta = os.path.join(directori_projecte, nom_carpeta)  # Creem la ruta completa de la carpeta
    os.makedirs(ruta_carpeta)

# Configuracio del sistema
def llegirconfig(arxiu,dic):
    # Crie um parser de configuracio
    config = configparser.ConfigParser()
    # Llegir arxiu de configuracio
    config.read(arxiu)
    # Retorna la base de dades com un diccionari
    return dict(config[dic])

def pintaBanner():
    print("    o")
    print("   (^))")
    print(" -= H = - SKACS")
    print("   ] [")
    print(" / ___ \\")
    print("")



if __name__ == "__main__":
    main()

