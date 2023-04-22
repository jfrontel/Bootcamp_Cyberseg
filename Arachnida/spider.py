'''Python requests. La librería para hacer peticiones http en Python'''

import requests
from bs4 import BeautifulSoup
import argparse
import os

def ft_coger_argumentos():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", help="Descarga de forma recursiva las imágenes en una URL.", nargs = '?')
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

def ft_download_img(args, lst_url):
    for img_url in lst_url:
        resp = requests.get(img_url, timeout=2)
        if resp.status_code == 200:
            nombre = img_url.split("/")[-1]
            path = args.path_download
            if not os.path.exists(path):
                os.makedirs(path)
            with open((path) + "/" + nombre, "wb") as archivo:
                archivo.write(resp.content)

def ft_search_urlweb(table_web):
    i = 0
    lst_urlweb = []
    for im in table_web:
        start = 0
        urlweb = str(table_web[i])
        end = len(urlweb)
        format_protocol = ['https://', 'http://']
        for q in format_protocol:
            if urlweb.find(f'a href="{q}') != -1:
                start = urlweb.find('a href="{q}') + len('a href="{q}') - 1
        end = urlweb.find('/"')
 
        if ((start > 0 and end < len(urlweb) - 1)):
            img_urlweb = urlweb[start:end]
            if (img_urlweb not in lst_urlweb):
                lst_urlweb.append(img_urlweb)
        i += 1
    print("-----------------------------------------------------------------------------")
    print(lst_urlweb)      
    return lst_urlweb

        
args = ft_coger_argumentos()
print(args.level_depth)
niv = 0
url = args.url
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
table = list(soup.find_all('img'))
lst_url = ft_search_format(table)
ft_download_img(args, lst_url)
table_web = list(soup.find_all('a'))
lst_urlweb = ft_search_urlweb(table_web)
    
sitios_extraidos = [args.url] 
while niv < args.level_depth:
    for j in lst_urlweb:
        req = requests.get(j)
        if j not in sitios_extraidos and req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            table = list(soup.find_all('img'))
            lst_url = ft_search_format(table)
            ft_download_img(args, lst_url)
            table_web = list(soup.find_all('a'))
            lst_urlweb = ft_search_urlweb(table_web)
            sitios_extraidos += [j]
            print(sitios_extraidos)

    niv += 1

print(sitios_extraidos)

    

