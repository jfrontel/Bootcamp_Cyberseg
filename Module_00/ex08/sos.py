import sys

equivalencias = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}


def caracter_plano_a_morse(caracter):
    if caracter in equivalencias:
        return equivalencias[caracter]
    else:
        # Si no existe, regresamos una cadena vacía
        return "error"


def codificar_morse(texto_plano):
    # A mayúsculas para evitar hacer más comparaciones
    texto_plano = texto_plano.upper()
    morse = ""  # Aquí alojamos el resultado
    for caracter in texto_plano: # Por cada carácter, buscamos su equivalencia
        caracter_codificado = caracter_plano_a_morse(caracter)
        if caracter_codificado == 'error':
            return 'error'
        # Lo concatenamos al resultado, además de agregar un espacio
        morse += caracter_codificado + " "
    return morse


palabra = ''
if (len(sys.argv) < 2):
    print('ERROR')
else:
    for arg in sys.argv[1:]:     
        if arg == sys.argv[-1]:
            palabra += arg
        else:
            palabra += arg + ' '
            
    print(f"Codificando... {palabra}")
    codificado = codificar_morse(palabra)
    if codificado == 'error':
        print ('ERROR')
    else:
        print(codificado)