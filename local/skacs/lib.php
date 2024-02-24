<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * Plugin functions for the local_skacs plugin.
 *
 * @package   local_skacs
 * @copyright 2023, Amos <apere118@xtec.cat>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

/**
function local_skacs_before_footer(){
	die('Hello');
}
**/

function local_skacs_before_footer(){

	//die(getHoraActual());
	//die('Hello');
}


/**
 * Retorna l'hora actual.
 * @return retorna una cadena.
 */

function getHoraActual() {
    // Establecer la zona horaria según tus necesidades
    date_default_timezone_set('Europe/Barcelona'); // Cambia 'Europe/Barcelona' a tu zona horaria preferida

    // Obtener la hora actual en formato de 24 horas
    $horaActual = date('H:i:s');

    return $horaActual;
}


function my_function_making_use_of_database() {
    global $CFG, $DB;
    $taula = 'mdl_skacs';

    $records=$DB->get_records_sql("SELECT * FROM $taula");
    echo ("Numero de registres: ". count($records));

    /**
    foreach ($records as $record) {
    	foreach ($record as $campo => $valor) {
        echo "$campo: $valor<br>";
    	}
    }

	//$DB->execute('SELECT * FROM mdl_skacs', $params);
	//$DB->get

	 echo '<h1>EOF</h1>';
	**/
	
	return $records;

}
	    

/**
 * Retona la darrera activitat de l'escaquer
 * La query retorna una llista dels darrers
 * SELECT id, escaquer,user, estat, MAX(ts) AS hora
FROM mdl_skacs
WHERE user IN ('1', '2', '3','4','5','10','11','12',19,20)  and escaquer='2'
GROUP BY user;
 * 
 */

function get_darrers_registres_de_caselles() {
	global $CFG, $DB;
    $taula = 'mdl_skacs';

    $query = "SELECT id, escaquer,user, estat, MAX(ts) AS hora
				FROM mdl_skacs
				WHERE user IN ('1', '2', '3','4','5','10','11','12','19','20')  and escaquer='1'
				GROUP BY user";

    $records=$DB->get_records_sql($query);

    echo ("Numero de registres: ". count($records));

    echo "<br>";
    echo "--------------<br>";

    foreach ($records as $record) {
    	foreach ($record as $campo => $valor) {
        echo "$campo: $valor<br>";
    	}
    echo "--------------<br>";
    }

	//$DB->execute('SELECT * FROM mdl_skacs', $params);
	//$DB->get

	echo '<h1>EOF</h1>';

	return $records;

}


