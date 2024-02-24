<?php

require_once('lib.php');
require_once('../../config.php'); // Ajusta la ruta segons la ubicació del teu script

require_once($CFG->libdir.'/outputrenderers.php');


// Verifiquem si l'usuari està autenticat
require_login();

// Obtenim l'objecte de l'usuari actual
$user = $USER;

// Imprimim la capçalera de Moodle amb la barra de navegació
// Carreguem la barra de navegació

echo $OUTPUT->header();




// Comprovem si l'usuari pertany al grup "Teachers"
if (user_has_role_assignment($user->id, 3)) {
	
    //Això no funciona. 
    //Molaria posar una nova barra de navegacio.
    //$PAGE->navbar->add('La meva pàgina', new moodle_url('/path/to/your/page.php'));

    // L'usuari pertany al grup "Teachers", mostrem "Hola"
    echo ('<h2>Hola '  . $user->firstname . '!');
    echo '<h1>Taulell Skacs</h1>';
	$horaInfo = '<h2>'. getHoraActual() .'</h2>';
	echo ($horaInfo);



    //Consulta a la BBDD i retorna un array
	$records = my_function_making_use_of_database();
    //echo count($records);
    $dades_per_a_mustache = array();
    
    //echo json_encode($records);
    
    foreach ($records as $fila) {

    // Processa cada fila i afegeix les dades al teu array
    $dades_per_a_mustache[] = array(
        'id' => $fila->id,
        'escaquer' => $fila->escaquer,
        'user'=> $fila->user,
        'estat' => $fila->estat,
        'ts'=> $fila->ts
    );
    //echo json_encode($dades_per_a_mustache);
    
    }

        /**
        $dades_per_a_mustache[] = array(
                'id' =>"40",
                'escaquer' => "1",
                'user'=> "2",
                'estat' => "1",
                'ts'=> "2024-01-08 16:31:51"
            );
        **/
     //Pinta l'escaquer 
    echo $OUTPUT-> render_from_template('local_skacs/skacs',array('dades' => $dades_per_a_mustache));











} else {
    // L'usuari no pertany al grup "Teachers", pots gestionar-ho com vulguis
    echo "No ets del grup 'Teachers'";
}


// Imprimim la peça final de la pàgina
echo $OUTPUT->footer();



echo '<h1>EOP</h1>';

    // You can access the database via the $DB method calls here.