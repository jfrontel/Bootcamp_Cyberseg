import requests
from bs4 import BeautifulSoup
import argparse
import os


# Inicializa el parser de argumentos de la línea de comandos.
def ft_coger_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', dest = "url", help='the URL to start the spider')
    if parser.add_argument('-r', '--recursive', dest = 'recursividad', action='store_true', help='download images'):
        parser.add_argument('-l', '--level_depth', dest = "level_depth", type=int, default=5, help='maximum depth level')
    parser.add_argument('-p', '--path', dest = "path_download", default = './data/', help='path to save download files')
    return parser.parse_args()

def ft_search_format(table):
    i = 0
    lst_url = []
    for im in table:
        imag_1 = str(table[i])
        index_j = imag_1.find('src=') + 5
        format = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        for w in format:
            if (imag_1.find(w) != -1):
                index_z = imag_1.find(w) + 4
        if (index_j > 0 and index_z < len(imag_1)):
            img_url = imag_1[index_j:index_z]
            lst_url.append(img_url)
        i += 1
    return lst_url

def ft_download_img(url):  
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    table_img = list(soup.find_all('img'))
    lst_url_imagen = ft_search_format(table_img)
    for img_url in lst_url_imagen:
        try:
            resp = requests.get(img_url, timeout=5)
            if resp.status_code == 200:
                nombre = img_url.split("/")[-1]
                path = args.path_download
                if not os.path.exists(path):
                    os.makedirs(path)
                with open((path) + "/" + nombre, "wb") as archivo:
                    archivo.write(resp.content)
        except Exception as excepcion:
            print(excepcion.args) 


def ft_search_urlweb(url, level):
    try:
        req = requests.get(url)
        if req.status_code == 200: 
            soup = BeautifulSoup(req.content, 'html.parser')
            table_web = list(soup.find_all('a'))
            for im in table_web:
                urlweb = str(im)
                format_protocol = ['https://', 'http://', 'https://www', 'http://www']
                for q in format_protocol:
                    start = 0
                    end = len(urlweb)                
                    if urlweb.find(f'a href="{q}') != -1:
                        start = urlweb.find('a href="{q}') + len('a href="{q}') - 1
                        end = urlweb.find('/"')
                        if ((start > 0 and end < len(urlweb) - 1)):
                            simple_urlweb = urlweb[start:end]
                            if (simple_urlweb not in sitios_encontrados and simple_urlweb.find('"')  < 0):
                                sitios_encontrados.append(simple_urlweb)
                                if level < args.level_depth:
                                    print(f'\nAnalizado: {url} level: {level} \n buscando en {simple_urlweb} siguiente nivel {level + 1} de url...')
                                    ft_search_urlweb(simple_urlweb, level + 1)
    except Exception as excepcion:
        print(excepcion.args)

if __name__ == "__main__":
    args = ft_coger_argumentos()
    print (args)
    print("args.url")
    if not args.url:
        print("Error. Usa <python ./spider.py -h> para mas informacion")
    sitios_encontrados = [args.url, ]
    # Extraer todas las URLs necesarias
    print("Analizando datos de entrada para su procesado...")
    if args.recursividad == True:
        ft_search_urlweb(args.url, 0)          # Extraer todos los sitios web

    for i in sitios_encontrados:
        print(f'\nDescargando imagenes de: {i} en carpeta {args.path_download}')
        ft_download_img(i)







'''
import os
import argparse
import requests
import re
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import shutil

IMAGE_EXTS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
DOCS_EXTS = ['.doc', '.pdf']
DEFAULT_MAX_DEPTH = 5
DEFAULT_PATH = './data/'
CREDITS = 'Arachnida v0.1.0 by jledesma@student.42malaga.com'
LOGO = """
\t           _     _           
\t          (_)   | |          
\t ___ _ __  _  __| | ___ _ __ 
\t/ __| '_ \| |/ _` |/ _ \ '__|
\t\__ \ |_) | | (_| |  __/ |   
\t|___/ .__/|_|\__,_|\___|_|   
\t    | |                      
\t    |_|        
"""    


def parseador():
    """
    Inicializa el parser y los parámetros necesarios.

    Returns:
    parser: un objeto ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description='Download all images from a website')
    parser.add_argument('url', help='the URL to start the spider')
    if parser.add_argument('-r', '--recursive', action='store_true', help='download images'):
        parser.add_argument('-l', '--max-depth', type=int, default=5, help='maximum depth level')
    parser.add_argument('-p', '--path', default=DEFAULT_PATH, help='path to save download files')
    return parser.parse_args()

def get_urls(url):
    """
    Obtiene todos los enlaces de una página web.

    Args:
    url: str, la URL de la página web a analizar.

    Returns:
    urls: una lista de objetos BeautifulSoup que representan los enlaces de la página web.
    """
    try:
        response = requests.get(url)
        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')
            urls = soup.find_all('a', href=re.compile('https?://'))
            print(F'Found {len(urls)} urls in {url}')
            return urls
    except Exception as e:
        print(f'Error: Failed connection {e}')
        return
    
def get_imgs(url):
    """
    Obtiene todas las imágenes de una página web.

    Args:
    url: str, la URL de la página web a analizar.

    Returns:
    imgs: una lista de objetos BeautifulSoup que representan las imágenes de la página web.
    """
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            imgs = soup.find_all('img', src=re.compile('(https?|file)://'))
            print(f'Found {len(imgs)} images in {url}')
            return imgs
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed connection to {url} ")
        return

def download_img_url(url, path, extensions, max_depth, curr_depth=0, visited_urls=set(), downloaded_imgs=set(), total=0):
    """
    Descarga todas las imágenes de una página web en directorios locales.

    Args:
    url: str, la URL de la página web local a analizar.
    path: str, la ruta del directorio de destino para guardar las imágenes.
    extensions: list, las extensiones de archivo permitidas para descargar.
    max_depth: int, la profundidad de búsqueda recursiva para enlaces adicionales.
    curr_depth: int, el nivel de profundidad actual en la búsqueda recursiva.
    visited_urls: set, el conjunto de URLs visitadas para evitar descargas duplicadas.
    downloaded_imgs: set, el conjunto de imágenes descargadas para evitar descargas duplicadas.
    total: int, el número total de imágenes descargadas anteriormente. Se utiliza solo para llamadas recursivas.
    """
    if curr_depth > max_depth:
        return
    if url in visited_urls:
        return
    visited_urls.add(url)
    try:
        response = requests.get(url)
    except Exception as e:
        print(f'Error: Failed connection {e}')
        return
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        imgs = soup.find_all('img', src=re.compile('https?://'))
        print(f'\t Found {len(imgs)} images in {url} ({curr_depth} depth)')
        cont_downloads = 0
        for img in imgs:
            img_url = img['src']
            img_ext = os.path.splitext(img_url)[1]
            if img_ext.lower() not in extensions:
                continue
            img_name = img_url.split('/')[-1]
            if img_name in downloaded_imgs:
                continue
            img_path = os.path.join(path, img_name)
            r = requests.get(img_url)
            with open(img_path, 'wb') as f:
                f.write(r.content)
                cont_downloads += 1
            downloaded_imgs.add(img_name)
        print(f'\t Downloaded {cont_downloads} images downloaded ({curr_depth} depth)')
        urls = get_urls(url)
        for u in urls:
            download_img_url(u['href'], path, extensions, max_depth, curr_depth+1, visited_urls, downloaded_imgs, total)
            
    
if __name__ == '__main__':
    global url_web, path, recursive, level, errors, total_downloads
    
    args = parseador()
    url_web = args.url
    path = args.path
    recursive = args.recursive
    level = args.max_depth
    total_downloads = 0


    cont = 0
    extensions = IMAGE_EXTS + DOCS_EXTS
    if level != 5 and not recursive:
        print(f" ERROR you need use -r or --recursive")
        exit()
    print(LOGO)
    print(f"\t\tInitiating spider...")
    print(f"\tURL: {url_web}")
    if not os.path.exists(path):
        os.makedirs(path)
    base_url = urlparse(url_web).scheme + '://' + urlparse(url_web).netloc

    if recursive:
        download_img_url(url_web, path, extensions, level)
        print(f'\nFinished spidering {CREDITS}')
    else:
        imgs = get_imgs(url_web)
        downloaded_imgs = set()
        try:
            for img in imgs:
                img_url = img['src']
                img_ext = os.path.splitext(img_url)[1]
                if img_ext.lower() not in extensions:
                    continue
                img_name = img_url.split('/')[-1]
                if img_name in downloaded_imgs:
                    continue
                img_path = os.path.join(path, img_name)
                r = requests.get(img_url)
                with open(img_path, 'wb') as f:
                    f.write(r.content)
                downloaded_imgs.add(img_name)
                total_downloads += 1
                #print(f'Downloaded {img_path}')
        except Exception as e:
            print(f'\tNo images found in {url_web} or URL incorrect, only https:// or http://')
        print(f'Total images downloaded: is {total_downloads} in {url_web}')
        print(f'\nFinished spidering {CREDITS}')



#https://github.com/Falitomal/Arachnida/blob/main/spider.py'''