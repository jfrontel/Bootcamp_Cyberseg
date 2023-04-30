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

<h2> Analisis ft_opt</h2>

<h3>Contraseña de un solo uso basada en el tiempo (TOTP)</h3>
<p>La contraseña de un solo uso basada en el tiempo (TOTP) es una forma común de implementar la autenticación de dos factores en las aplicaciones. Funciona solicitando al usuario un token que generalmente se envía en un SMS, correo electrónico o un pase secreto generado al dispositivo del usuario con un tiempo de vencimiento. Compara el token provisto con el token generado real, luego los autentica si los tokens coinciden.</p>

<h3>Cómo funcionan las aplicaciones de autenticación TOTP</h3>
<p>Esencialmente, el proceso de autenticación con autenticadores implica el siguiente procedimiento:</p>

<p>[+]  El sitio web solicita al usuario que proporcione una contraseña de un solo uso generada por la aplicación de autenticación.</p>
<p>[+]  Luego, el sitio web genera otro token utilizando un valor inicial que tanto la aplicación de autenticación como él mismo conocen.</p>
<p>[+]  El sitio web procede a autenticar al usuario si el token recién generado coincide con el token proporcionado por el usuario.</p>

<h3>¿Qué es HMAC (Código de autenticación de mensajes basado en hash)?</h3>

<p>Los HMAC proporcionan al cliente y al servidor una clave privada compartida que solo ellos conocen. El cliente realiza un hash único (HMAC) para cada solicitud. Cuando el cliente solicita el servidor, procesa los datos solicitados con una clave privada y los envía como parte de la solicitud. Tanto el mensaje como la clave se codifican en pasos separados para que sea seguro. Cuando el servidor recibe la solicitud, crea su propio HMAC. Se comparan ambos HMACS y, si ambos son iguales, el cliente se considera legítimo<p/>

