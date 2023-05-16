print('''
--------------------------------------------------------------------------------------------------------------
==============================================================================================================                           
                                            		FT_OTP              	                   by jfrontel
==============================================================================================================
--------------------------------------------------------------------------------------------------------------
''')

import hmac, base64, struct, hashlib, time
from cryptography.fernet import Fernet
import sys
import os, re
import argparse

# __________________________________________  MENÚ DE ARGUMENTOS  _____________________________________________ #
# ft_get_argument() tomará los argumentos de entrada del programa ft_otp

def process_arguments():
    parser = argparse.ArgumentParser(description='Generate TOTP key')
    parser.add_argument('-g', '--savekey', type=str)
    parser.add_argument('-k', '--tempkey', type=str)
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
		
	if re.match(r'{64,}', secret_key):
		print("La clave tiene formato correcto...")		

		return 1
	else:
		print("La clave no está en formato hexadecimal o no tiene el mínimo de 64 caracteres.")
		return 0


'''    if not re.match(r'^[0-9a-fA-F]{64,}$', key):
        print("La clave no está en formato hexadecimal o no tiene el mínimo de 64 caracteres.")'''
        
'''		        f = open(args.savekey, 'r')
        hexkey = f.read().strip()
        hexcad = 'abcdef123456789ABCDEF'
        if len(hexkey) >= 64 and all(c in hexcad for c in hexkey):
            with open('ft_otp.key', 'w') as f:
                f.write(hexkey)
        else:
            print("Key has to be at least 64 hexadecimal characters")'''
            
'''    try:
        if len(key) >= 64:
            int(key, 16)
            return True
        else:
            return False
    except Exception:
        return False'''
        
'''def is_hex(key_hex):
	"""Function to verify if string is hex of 64 characters"""
	if len(key_hex) >= 64:
		try:
			int(key_hex, 16)
		except ValueError:
			return False
		return True
	else:
		return False'''
            

def get_hotp_token(secret, intervals):
    '''Con la ayuda del base64.b16decode() método, podemos decodificar la cadena binaria usando alfabetos base16 en forma normal.
Sintaxis: base64.b32decode(b_string). Retorno: Devuelve la cadena decodificada.'''
    key = base64.b16decode(secret, True)
    #decoding our key:
    print(f'key = {key}')
    '''Este módulo convierte entre valores de Python y estructuras C representadas como bytesobjetos de Python. 
Las cadenas de formato compacto describen las conversiones previstas a/desde valores de Python. 
struct.pack(format, v1, v2, ...) Devuelve un objeto de bytes que contiene los valores v1 , v2... empaquetados de acuerdo con el formato de cadena de formato. 
Los argumentos deben coincidir exactamente con los valores requeridos por el formato. >Q - entero largo largo; >I entero''' 
    msg = struct.pack(">Q", intervals)
    print(f'msg = {msg}')
    h = hmac.new(key, msg, hashlib.sha1).digest()
    print(f'hmac_new = {h}')
    o = o = h[19] & 15  # Operación AND entre '0b????' y '0b1111'
    print(f'o = {o}')
    #Generate a hash using both of these. Hashing algorithm is HMAC
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000  # '[0]' porque 'struct.unpack' devuelve una lista
    print(f'h = {h}')
    #unpacking
    return h

def get_totp_token(secret):
    #ensuring to give the same otp for 30 seconds
    intervals = int((time.time())//30)
    print(time.time())
    print(secret)
    print(f"intervals_no= {intervals}")
    pass_temp = str(get_hotp_token(secret, intervals))
    #adding 0 in the beginning till OTP has 6 digits
    while len(pass_temp)!=6:
        pass_temp +='0'
    return pass_temp



def store_key(file1):
	try:
		with open(file1, 'rb') as file:
			original_hex = file.read()
	except:
		print(f"El fichero no ha podido abrirse")
	if ft_file_ok(file1) == 1:
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
	with open(".key", "rb") as filekey:
			key1 = filekey.read()
	key = Fernet(key1)
	with open(sys.argv[2], 'rb') as q:
		encrypted_data = q.read()
	decryted_data = key.decrypt(encrypted_data)
	c = len(decryted_data) - 1
	decryted_data = decryted_data[2:c]
	print(get_totp_token(decryted_data))
	code = get_totp_token(decryted_data)
	with open("code.txt", "wt") as e:
		e.write(code)
  
if __name__ == "__main__":
    args = process_arguments()
    print(args.savekey)
    print(args.tempkey)
    if args.savekey == None and args.tempkey  == None or args.savekey != None and args.tempkey  != None:
        print("ERROR. Introduzca <./ft_otp [-gk]> o -help para más ayuda")
        exit()
        
    if args.savekey != None:
        store_key(args.savekey)
    elif args.tempkey != None:
        create_key()
