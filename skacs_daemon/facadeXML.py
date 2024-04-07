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


import xml.etree.ElementTree as ET
from datetime import datetime


from xml.sax.handler import ContentHandler
from xml.sax import make_parser

    # Tupla on d'identifica el bit amb el nom de la casella
    # El bit s'agafa a partir de l'anotació empírica de la cadena retornada segons posició
    # de 64 caràcters.


def main():

    __llistaBITS = ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
                    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
                    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
                    "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
                    "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8",
                    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"
                    )

    __horaris = 'horaris.xml'
    __escaquer_t64 = 'escaquer_t64'
    __skac = "None"
    __usuaris = []

    __log_file = './logs/skacs03042024'


    if test_Integritat(__horaris):

        #Llegeix els usuaris donats d'alta a l'escaquer
        __usuaris= llegir_document_text(__escaquer_t64)


        us = __usuaris["A1"]
        print(us)
        obtenir_data_canvi_bit(__log_file, posicio("A1", __llistaBITS))
        print("hora prevista horari" + obtener_hora_inicial_mas_temprana_horario(us,datetime(2024, 4, 3)))

    else:

        pass











def obtenir_data_canvi_bit(nom_arxiu, num_bit):

    with open(nom_arxiu, 'r') as f:

        data_anterior = None

        for linia in f:
            components = linia.strip().split('#')
            data = components[0] + '#' + components[1]  # Concatenar la data i l'hora
            valor_bit = components[4][num_bit - 1]  # Obtenir el valor del bit en la posició indicada
            if valor_bit == '1' and data_anterior is not None:

                print("Skac!! Entrada: " + data + "" )
                return data_anterior
            data_anterior = data
    return None

# retorna només els registres amb valor not None
def llegir_document_text(fitxer):
        dic_usuaris= {}
        with open(fitxer, 'r') as f:
            for linia in f:
                linia = linia.strip()
                if linia:
                    id_item, valor = linia.split('#')
                    if valor:
                        dic_usuaris[id_item] = valor
        return dic_usuaris

def obtener_hora_inicial_mas_temprana_horario(id_horario, fecha):
        # Parsear el XML
        tree = ET.parse('horaris.xml')
        root = tree.getroot()

        # Obtener el día de la semana correspondiente a la fecha proporcionada
        dia_semana = fecha.strftime('%A').lower()


        # Buscar el horario correspondiente al ID proporcionado
        for horario in root.findall('horari'):
            if horario.find('id').text == id_horario:
                # Buscar el interval correspondiente al día de la semana y obtener la hora de inicio más temprana
                hora_inicial_mas_temprana = None
                for interval in horario.find(dia_semana):
                    inicio = datetime.strptime(interval.find('inici').text, '%H:%M')
                    if hora_inicial_mas_temprana is None or inicio < hora_inicial_mas_temprana:
                        hora_inicial_mas_temprana = inicio

                return hora_inicial_mas_temprana.strftime('%H:%M')

        return None

def obtener_hora_final_mas_tardia(id_horario, fecha):
        # Parsear el XML
        tree = ET.parse('horarios.xml')
        root = tree.getroot()

        # Obtener el día de la semana correspondiente a la fecha proporcionada
        dia_semana = fecha.strftime('%A').lower()

        # Buscar el horario correspondiente al ID proporcionado
        for horario in root.findall('horari'):
            if horario.find('id').text == id_horario:
                # Buscar el interval correspondiente al día de la semana y obtener la hora de finalización más tardía
                hora_final_mas_tardia = None
                for interval in horario.find(dia_semana):
                    final = datetime.strptime(interval.find('final').text, '%H:%M')
                    if hora_final_mas_tardia is None or final > hora_final_mas_tardia:
                        hora_final_mas_tardia = final

                return hora_final_mas_tardia.strftime('%H:%M')

        return None


def test_Integritat(horaris):
    saxparser = make_parser()
    saxparser.setContentHandler(ContentHandler())

    try:
        saxparser.parse(horaris)
        return True

    except Exception as e:
        print("Error en document")


def posicio(valor, tupla):
    for i, elem in enumerate(tupla):
        if elem == valor:
            return i+1
    return None


if __name__ == "__main__":
    main()
