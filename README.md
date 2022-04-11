# StreamlabsChatbotScripts
<img src="https://user-images.githubusercontent.com/15488788/162835662-87ab66e8-130c-45ca-8ebf-e4c2d10fcd40.png" align="right">
En este repositorio iré subiendo algún script que pueda ser empleado desde el <a href="https://www.usitility.com/es/streamlabs-chatbot/descargar-windows">Streamlabs Chatbot</a>.

<H1>Instrucciones para instalar los Scripts</H1>

Una vez tengamos instalado el ChatBot para poder activar la pestaña de scripts, que podemos encontrar al final de la imágen lateral, deberemos logearnos con las cuentas de **Twitch Bot** y **Twitch Streamer** en el icono de usuario de abajo a la izquierda de la imagen.

También será necesario instalar Python, para mas instruciones seguir el siguiente <a href=https://streamlabs.com/content-hub/post/chatbot-scripts-desktop>link</a>.
<br><br>En resumen es descargar Python desde el link que se indica, instalarlo con las opciones por defecto y configurar Streamlabs Chatbot siguiendo las instrucciones para indicar la carpeta donde encontrar lo anteriormente instalado.

Una vez logeado la pestaña de Scripts debería aparecer.

Para instalar los scripts simplemente podeis descargar el .zip dentro de las diferentes carpetas y seguñir las instrucciones que se indican en el <a href=https://streamlabs.com/content-hub/post/chatbot-scripts-desktop>link</a> anterior.

<H1>Support After Raid</H1>

Este script es simplemente para lanzar un mensaje de agradecimiento que puede ser customizado para cada usuario.

Para personalizar los mensajes, tanto el por defecto (Default) como los de los usuarios que queramos añadir deveremos hacer click derecho sobre el scipt y se abrira la carpeta donde se guarda (si se borra esta carpeta se borra el script).

<img src="https://user-images.githubusercontent.com/15488788/162838774-8d93e726-ed48-4ce0-8120-451bf483610e.png">

Dentro de la carpeta **Support After Raid** se encuentra el documento de texto **greetings.txt** en el se encuentran algunos ejemplos.

Cada usuario solo puede tener un mensaje y estos deben estar en la misma linea, la longitud máxima es la que permita Twitch en mensajes de usuario individuales.

El único que es **OBLIGATORIO** que permanezca es la línea del **Default** aunque el mensaje se puede personalizar.
El separador entre usuario y mensaje es **|$** y los **{0}** son el nombre de la persona que está raideando, por lo tanto un ejemplo del fichero podría ser:
<hr>
Default|$Gracias {0} por la raid! Podeis seguir a {0} en www.twitch.tv/{0}
<br>ibai|$Gracias {0} por la pedazo de raid! Visidad a {0} en www.twitch.tv/{0} y seguid a KOI en https://twitter.com/KOI
<br>Trator7|$Sigue a Trator en https://twitter.com/Trator7 y descarga su código abierto en https://github.com/Trator7
<hr>
Este sería un ejemplo de respuesta automática de una raid
<br><br><img src="https://user-images.githubusercontent.com/15488788/162838265-3aba312e-65ae-47d9-9c50-c5e128b2fadb.png">
