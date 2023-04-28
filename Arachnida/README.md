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
<p>./spider [-rlp] URL</p>
<p>• Opción -r : descarga de forma recursiva las imágenes en una URL recibida como
parámetro.</p>
<p>• Opción -r -l [N] : indica el nivel profundidad máximo de la descarga recursiva.
En caso de no indicarse, será 5.</p>
<p>• Opción -p [PATH] : indica la ruta donde se guardarán los archivos descargados.
En caso de no indicarse, se utilizará ./data/.</p>
<p>El programa descargará por defecto las siguientes extensiones: .jpg/jpeg, .png, .gif, .bmp</p>

<h3>Scorpion</h3>
<p>El segundo programa scorpion recibirá archivos de imagen como parámetros y será
capaz de analizarlos en busca datos EXIF y otros metadatos, mostrándolos en pantalla.
El programa será compatible, al menos, con las mismas extensiones que gestiona spider.
Deberá mostrar atributos básicos como la fecha de creación, así como otros datos EXIF.
El formato en el que se muestren los metadatos queda a tu elección.</p>
<p>./scorpion FILE1 [FILE2 ...]</p>


<h2>Analisis Spider</h2>

<h4>Librería requests de Python</h4>

<p> requests es una librería Python que facilita enormemente el trabajo con peticiones HTTP. Esta librería se encarga de obtener respuestas que se realizan en el protoloco HTTP de una plataforma web que se haya establecido con anterioridad con una API.</p>

<p>Para hacer una petición inicial desde esta librería, solo debes ingresar en tu programa la siguiente instrucción: respuesta = requests.get (‘url’). A continuación, le podrás imprimir una respuesta con la instrucción print («respuesta»).</p>

<p>Instalar e importar la librería requests</p>
<p>En un principio, para instalar la librería requests en Python deberás utilizar el paquete de instalación de Python pip install de la siguiente manera: python -m pip install requests.</p>

<h4>Librería beautifulsoup de Python</h4>

<p>El paquete Beautiful Soup es ampliamente utilizado en técnicas de «scraping» permitiendo «parsear» principalmente código HTML.</p>

<p>pip install beautifulsoup4</p>
Para empezar a trabajar con Beautiful Soup es necesario construir un objeto de tipo BeautifulSoup que reciba el contenido a «parsear»:

<p>Buscaremos en el contenido ya parseado todos los enlaces de esa url buscado en la sopa con soup.find_all('a') formateamos cada uno de estos datos hasta conseguir las url limpias que iremos guardando en una lista</p>

<h4>Librería argparse de Python</h4>

# Inicializa el parser de argumentos de la línea de comandos.
<p>parser = argparse.ArgumentParser()</p>
<p>parser.add_argument("-r", dest = 'recursividad', help="Descarga de forma recursiva las imágenes en una URL.", action="store_true")</p>
<p>parser.add_argument("-l", dest = "level_depth", type=int, help="Indica el nivel profundidad máximo de la descarga recursiva. Por defecto 5", default = 5)</p>
<p>parser.add_argument("-p", dest = "path_download", type=str, help="Indica la ruta donde se guardarán los archivos descargados. Por defecto ./data/.", default = './data/')</p>
<p>parser.add_argument("--URL", dest = "url", type=str, help="Url de donde vamos a descargar las imagenes")
<p>args = parser.parse_args()</p>

<h2> Estructura Spider </h2>
<p>  - Procesar los argumentos de entrada:</p>
<p>     ---- Existe Recursividad: </p>
<p>     ---------- Existe l entonces l=argumento</p>
<p>     ---------- No l entonces l(profundidad)=5  </p>
<p>     ---- No existe Recursividad</p>
<p>     ----------- Descargar fotos de url = argumento</p>
  

