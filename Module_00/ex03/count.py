import sys

def text_analyzer(str_1=''):
    '''Este es un programa para contar caracteres, mayusculas, minusculas, caracteres de puntuacion,
    y espacios en una frase. Entra en el interprete de python, importa la funcion text_analyzer con 
    <from count import text_analyzer> y luego escribe un frase de la siguiente forma:
    <text_analyzer('frase')>'''
    mayusc = 0
    minus = 0
    i = 0
    esp = 0

    if (not str_1):
        print('What is the text to analyze?')
        str_1 = input()
    if (str_1.isdigit() == True):
        print('Error argumento incorrecto, escriba una cadena de caracteres')

    else:
        while (i < len(str_1)):
            if str_1[i].isupper() == True:
                mayusc += 1
            elif  str_1[i].islower() == True:
                minus += 1
            if (str_1[i] in "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"):
                esp += 1
            i += 1
        print("El texto contiene %d caracteres" %len(str_1)) 
        print("- %d Mayusculas" %mayusc)
        print("- %d Minusculas" %minus)
        print("- %d Caracteres de puntuacion" %esp)
        print("- %d espacios en la frase" %str_1.count(' '))

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        print("What is the text to analyze?")
        str_2 = input()
        text_analyzer(str_2)
    elif (len(sys.argv) > 2):
        print("Error, Por favor introduce solo un parametro como argumento")
    else: 
        text_analyzer(sys.argv[1])
