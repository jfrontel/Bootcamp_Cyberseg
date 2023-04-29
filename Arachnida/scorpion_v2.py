import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def ft_coger_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("--f", dest="FILE", help="image archive.", type=str),
    parser.add_argument("--ff", dest="FILE_ADD", help="other image archives", nargs="*")
    args = parser.parse_args()
    return(args)


def scorpion(file):
    if not file:
        print('ERROR. Directorio {file} no encontrado')
    else:
        for n in file:
            file_1 = Image.open(n)
            print(file_1)

            # extracting the exif metadata
            exifdata = file_1.getexif()
            
            # looping through all the tags present in exifdata
            for tag_id in exifdata:
                try:
                    # getting the tag name instead of tag id
                    tagname = TAGS.get(tag_id, tag_id)
                
                    # passing the tagid to get its respective value
                    value = exifdata.get(tag_id)
                    
                    # printing the final result
                    print(f"{tagname:25}: {value}")
                except: 
                    print(f"Etiqueta {tag_id} no encontrada.")
                
if __name__ == "__main__":
    args = ft_coger_argumentos()

    # Leer las imágenes desde la línea de comandos
    ubicaciones = list()
    ubicaciones.append(args.FILE)
    ubicaciones.append(args.FILE_ADD)

    scorpion(ubicaciones)