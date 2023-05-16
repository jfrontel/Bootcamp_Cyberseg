print('''
--------------------------------------------------------------------------------------------------------------
==============================================================================================================                           
                                            	FT_OTP              	                   by jfrontel
==============================================================================================================
--------------------------------------------------------------------------------------------------------------
''')

# ____________________________________________ DESCRIPCION ____________________________________________________ #

'''ft_opt permite registrar una clave inicial, y es capaz de generar una nueva contraseña cada vez que se solicite. 
-- Con la opción -g , el programa recibirá como argumento una clave hexadecimal de al menos 64 caracteres. 
    El programa guardará a buen recaudo esta clave en un archivo llamado ft_otp.key, que estará cifrado en todo momento.
-- Con la opción -k, el programa generará una nueva contraseña temporal y la mos- trará en la salida estándar. ...]'''


# ____________________________________________ LIBRERIAS ____________________________________________________ #

import hmac, base64, struct, hashlib, time
from cryptography.fernet import Fernet
import sys
import os, re
import argparse

# ________________________________________  MENÚ DE ARGUMENTOS  _______________________________________________ #
# ft_get_argument() tomará los argumentos de entrada del programa ft_otp

def process_arguments():
    parser = argparse.ArgumentParser(description='Generate TOTP key')
    parser.add_argument('-g', '--store_key', type=str)
    parser.add_argument('-k', '--create_key', type=str)
    args = parser.parse_args()
    return args

# ____________________________________________  VALIDAR ARCHIVOS _______________________________________________ #
# ft_file_ok() toma por argumento el fichero dado al programa, comprueba que existe y es legible con permiso de lectura. 
# Lectura del fichero y verificación de que la clave es hexadecimal y que contiene al menos 64 caracteres  

def ft_file_ok(file):
	global secret_key
	if not (os.path.isfile(file) or os.access(file, os.R_OK)):
		print("ERROR: el fichero dado no existe o no tiene permiso de lectura.")
		exit()
	with open(file, "r") as f:
		secret_key = f.read()
	if re.match(r'^[0-9a-f+/i]{64,}', secret_key):
		print("La clave tiene formato correcto...")		
		return 1
	print("La clave no está en formato hexadecimal o no tiene el mínimo de 64 caracteres.")
	return 0


# ______________________________________________  HOPT y TOTP  _________________________________________________ #
# HOPT (HMAC-based One-Time Password), contraseña de un solo uso basada en eventos: basada en el algoritmo criptográfico HMAC 
# y depende de dos tipos de información. El primero es la clave secreta llamada “inicialización” la cual solo conoce el token y el 
# servidor que valida los códigos OTP enviados. el segundo es el factor móvil, que es un contador almacenado en el token y el servidor. 
# El contador del token incrementa al pulsar el botón del token, mientras que el contador del servicio solo se incrementa cuando se valida correctamente una OTP.

# TOPT (Time-based One-Time Password), contraseña de un solo uso basada en tiempo: Está inspirada en la anterior, HOTP, 
# pero su factor móvil es el tiempo en lugar de un contador. TOPT emplea tiempo en incrementos llamado “timestep” (30 seg). 
# De esta forma, cada OTP será válida mientras dura el “timestep”


def get_hotp_token(secret, timestep):
# Codificar el tiempo y la clave en una cadena de bytes
    secret_key = ''
    msg = struct.pack(">Q", timestep)
    secret_key = str(secret)
    secret_key = secret_key[2:-4]
    print(secret_key)
    key_b = bytes.fromhex(secret_key)
# Generar un hash de la llave hexadecimal y el paquete de tiempo codificado mediante cifrado sha1
    hash = hmac.new(key_b, msg, hashlib.sha1).digest()
# Obtener el valor de los últimos 4 bits de h (Operación AND entre '0b????' y '0b1111')
    o = o = hash[19] & 15 
# Generate a hash using both of these. Hashing algorithm is HMAC
    pass_temp = (struct.unpack(">I", hash[o:o+4])[0] & 0x7fffffff) % 1000000  # '[0]' porque 'struct.unpack' devuelve una lista
    print(f'pass_temp = {pass_temp}')
    return pass_temp

def get_totp_token(secret):
#Obtener tiempo cada intervalo de 30 segudos
    timestep = int((time.time())//30)
    pass_temp = str(get_hotp_token(secret, timestep))
# Bucle: colocar ceros delante del numero si este no tiene seis cifras
    while len(pass_temp)!=6:
        pass_temp +='0'
    return pass_temp

def store_key():
	try:
		with open(args.store_key, 'rb') as file:
			original_hex = file.read()
	except:
		print(f"El fichero no ha podido abrirse")
	if ft_file_ok(store_key) == 1:
		try:
			hex_key = (original_hex, 16)
			hex_key = str(original_hex)
			print(f"hex_key= {hex_key}")
			key = Fernet.generate_key()
			print(f"Fernet_generate_key= {key}" )
			with open(".key", "wb") as a:
				a.write(key)
			key = Fernet(key)
			print(f"Fernet_key= {key}" )  
			with open("ft_otp.key", "wb") as f:
				f.write(key.encrypt(hex_key.encode()))
			print("Key succesfully encrypted into ft_otp.key")
		except:
			print(f"El fichero {file} no ha podido abrirse") 
            
def create_key():
	try:
		with open(".key", "rb") as filekey:
			key1 = filekey.read()
	except:
	    print("No se pudo abrir ")
	key = Fernet(key1)
	with open(sys.argv[2], 'rb') as q:
		encrypted_data = q.read()
	decryted_data = key.decrypt(encrypted_data)
	c = len(decryted_data) - 1
	decryted_data = decryted_data[2:c]
	print(get_totp_token(decryted_data))
	code = get_totp_token(decryted_data)
	print(f'code = {code}')
	with open("key_secret.txt", "wt") as e:
		e.write(code)
  
if __name__ == "__main__":
    args = process_arguments()
    if args.store_key == None and args.create_key  == None or args.store_key != None and args.create_key  != None:
        print("ERROR. Introduzca <./ft_otp [-gk]> o -help para más ayuda")
        exit()
        
    if args.store_key != None:
        store_key()
    elif args.create_key != None:
        create_key()