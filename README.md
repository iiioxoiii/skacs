# skacs
Projecte de desenvolupament d'un sistema de control d'assistència laboral.

## Objectiu
El desplegament descontrolat de sistemes de control associats a les dades biometriques suposa perill en els àmbits quotidians i posa en risc les llibertats individuals i col·lectives. Des del maig de 2022, la implantació de sistemes de control horari basats en dades biomètriques han d'estar degudament justificats pels mecanimes legals establerts.

> Sí el conveni col·lectiu de l'empresa no ho especifica, la necessitat de fer
> servir sistemes de control horari amb sistemes biomètrics recau en [el responsable de
> tractament de dades](https://apdcat.gencat.cat/ca/drets_i_obligacions/responsables/obligacions/delegat-proteccio-dades/).
> Aquest figura ha de justificar el canvi de sistema de control horari antic pel nou i justificar la necessitat d'incorporar les
> dades bionètriques al sistema nou [+info](https://periscopiofiscalylegal.pwc.es/el-nuevo-criterio-de-la-agencia-sobre-el-tratamiento-de-control-de-presencia-mediante-sistemas-biometricos/).
> Això és desprén de l'actualització de les Directrius 05/2022 del maig de 2022 sobre l'ús de reconeixement facial.

El sistema **Skacs** planteja un sistema transparent adaptat a la normativativa i sense associar dades biomèdiques a la persona física.

## Parts del projecte
El sistema consta de tres parts: 

1) **El taulell o taulells**: Els taulells són la cònsola o còsoles on els usuaris validen l'entrada i sortida del lloc de treball.
2) **El sistema intermediari de dades**: El sistema que rep les dades dels taulells i les envia a la BBDD.
3) **El pluggin Skacs pel Moodle**: El pluggin que permet relacionar les dades guardades a la BBDD (administrar el sistema i visualitzar les dades als usuaris.)

## Taulell o taulells
En desenvolupament.

## Sistema intermediari
En desenvolupament

## Pluggin Moodle
Dins la carpeta **local** està la carpeta **skacs** dins la qual hi han els fitxers pel pluggin de Moodle **Skacs**. 


