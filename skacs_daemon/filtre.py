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



class Filtre:

    __linia = ""
    __tipus = None
    __nom = None
    __switch = 0


    # Funcio que retorna True si la linia es correcta
    def f_line_t64(self,linia):

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

        return True