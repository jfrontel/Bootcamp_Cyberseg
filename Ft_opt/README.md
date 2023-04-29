<h2> ft_opt: Enunciado </h2>
<p>En el lenguaje de tu elección, debes implementar un programa que permita registrar
una clave inicial, y sea capaz de generar una nueva contraseña cada vez que se solicite.
Puedes utilizar cualquier librería que facilite la implementación del algoritmo, siempre
que no hagan el trabajo sucio, es decir, queda terminantemente prohibido hacer uso de
cualquier librería TOTP. Por supuesto, puedes y debes hacer uso de alguna librería o
función que te permita acceder al tiempo del sistema.</p>
<p>-- El programa deberá llamarse ft_otp.</p>
  
<p>-- Con la opción -g , el programa recibirá como argumento una clave hexadecimal
de al menos 64 caracteres. El programa guardará a buen recaudo esta clave en un
archivo llamado ft_otp.key, que estará cifrado en todo momento.</p>
    
<p>-- Con la opción -k, el programa generará una nueva contraseña temporal y la mos-
trará en la salida estándar.</p>
