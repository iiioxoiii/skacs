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

import mysql.connector
import requests

class FacadeBBDD:

    __host = ""
    __user = ""
    __password = ""
    __database = ""

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None

    def connectar(self):

        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                print("Connexió a la base de dades establerta.")
        except mysql.connector.Error as e:
            print(f"No s'ha pogut connectar a la base de dades: {e}")

    def tancar_connexio(self):
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()
            print("Connexió a la base de dades tancada.")


    def executar_consulta(self, consulta):
        try:
            cursor = self.conn.cursor()
            cursor.execute(consulta)
            resultats = cursor.fetchall()
            return resultats
        except mysql.connector.Error as e:
            print(f"Error en executar la consulta: {e}")

    def test_internet(self):

        # Pinta la connexió internet
        url = "http://www.google.com"
        print("Connexió a internet...")

        try:
            # Intenta obtenir una resposta de Google
            response = requests.get(url)
            if response.status_code == 200:
                print("Connexió a Internet establerta.")
                return True
            else:
                print("No es pot connectar a Internet.")

        except requests.ConnectionError:
            print("No es pot connectar a Internet.")



