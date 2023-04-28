<h2>Enunciado</h2>
<p>Los dos programas pueden ser scripts o binarios. En caso de lenguajes compilados,
debes el código fuente y compilarlo durante la evaluación. Puedes utilizar funciones o
librerías que te permitan crear peticiones HTTP y manejar archivos, pero la lógica de
cada programa debe estar desarrollada por ti. Es decir, utilizar wget o scrapy será
considerado cheat y supondrá suspender el proyecto</p>

<h3>Spider</h3>
<p>El programa spider permitirá extraer todas las imágenes de un sitio web, de manera
recursiva, proporcionando una url como parámetro. Gestionarás las siguientes opciones
del programa:</p>
<p>./spider [-rlpS] URL</p>
<p>• Opción -r : descarga de forma recursiva las imágenes en una URL recibida como
parámetro.</p>
<p>• Opción -r -l [N] : indica el nivel profundidad máximo de la descarga recursiva.
En caso de no indicarse, será 5.</p>
<p>• Opción -p [PATH] : indica la ruta donde se guardarán los archivos descargados.
En caso de no indicarse, se utilizará ./data/.</p>
<p>El programa descargará por defecto las siguientes extensiones: .jpg/jpeg, .png, .gif, .bmp</p>

<h3>Spider</h3>
<p>El segundo programa scorpion recibirá archivos de imagen como parámetros y será
capaz de analizarlos en busca datos EXIF y otros metadatos, mostrándolos en pantalla.
El programa será compatible, al menos, con las mismas extensiones que gestiona spider.
Deberá mostrar atributos básicos como la fecha de creación, así como otros datos EXIF.
El formato en el que se muestren los metadatos queda a tu elección.</p>
<p>./scorpion FILE1 [FILE2 ...]</p>
