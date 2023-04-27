import requests
from bs4 import BeautifulSoup
import argparse
import os


# Inicializa el parser de argumentos de la línea de comandos.
def ft_coger_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", dest = 'recursividad', help="Descarga de forma recursiva las imágenes en una URL.", action="store_true")
    parser.add_argument("-l", dest = "level_depth", type=int, help="Indica el nivel profundidad máximo de la descarga recursiva. Por defecto 5", default = 5)
    parser.add_argument("-p", dest = "path_download", type=str, help="Indica la ruta donde se guardarán los archivos descargados. Por defecto ./data/.", default = './data/')
    parser.add_argument("--URL", dest = "url", type=str, help="Url de donde vamos a descargar las imagenes")
    args = parser.parse_args()
    return(args)

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

def ft_download_img(args, url):
        
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        table_img = list(soup.find_all('img'))
        lst_url_imagen = ft_search_format(table_img)
        for img_url in lst_url_imagen:
            try:
                resp = requests.get(img_url, timeout=5)
                if resp.status_code == 200:
                    nombre = img_url.split("/")[-1]
                    path_home = args.path_download
                    if not os.path.exists(path_home):
                        os.makedirs(path_home)
                    with open((path_home) + "/" + nombre, "wb") as archivo:
                        archivo.write(resp.content)
            except Exception as excepcion:
                print(excepcion.args) 
        print(f"Loading photos the {url} in folder... {args.path_download}")
       
def ft_search_urlweb(url, level):
    try:
        lst_urlweb = []
        req = requests.get(url)
        if req.status_code == 200: 
            soup = BeautifulSoup(req.content, 'html.parser')
            table_web = list(soup.find_all('a'))
            for im in table_web:
                urlweb = str(im)
                format_protocol = ['https://', 'http://']
                for q in format_protocol:
                    start = 0
                    end = len(urlweb)                
                    try:
                        if urlweb.find(f'a href="{q}') != -1:
                            start = urlweb.find('a href="{q}') + len('a href="{q}') - 1
                            end = urlweb.find('/"')
                            if ((start > 0 and end < len(urlweb) - 1)):
                                simple_urlweb = urlweb[start:end]
                                if (simple_urlweb not in sitios_encontrados and simple_urlweb.find('"')  < 0):
                                    lst_urlweb.append(simple_urlweb)
                                    sitios_encontrados.append(simple_urlweb)
                                    print(f'nivel: {level} url: {simple_urlweb}')
                                    if level < args.level_depth:
                                        print('buscando siguiente nivel de url...')
                                        ft_search_urlweb(simple_urlweb, level + 1)
                    except Exception as excepcion:
                        print(excepcion.args)
                
    except Exception as excepcion:
        print(excepcion.args)
    print("-----------------------------------------------------------------------------")
    print(sitios_encontrados)
    return lst_urlweb         

if __name__ == "__main__":
    args = ft_coger_argumentos()
    sitios_encontrados = [args.url, ]
    # Extraer todas las URLs necesarias
    print("Analizando datos de entrada para su procesado...")
    if args.recursividad == True:
        ft_search_urlweb(args.url, 0)          # Extraer todos los sitios web

    for i in sitios_encontrados:
        ft_download_img(args, i)