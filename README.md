<h1 align="center">Proyecto IoT ConSens</h1>
El proyecto consistió de modulos Arduino equipados con sensores de presión, temperatura y humedad y una antena la cual variaba dependiendo el grupo de trabajo ("Industrial wireless communication" (NRF24L01) o "LoRa" (RFM95)) con el fín de transmitir los datos recolectados a un Gateway desarrollado con un ESP32S y este a su vez enviar los datos a la pagina web para finalmente ser guardados en una base de datos, mostrar dichos datos en la pagina y en una aplicacion de telefono, y además enviar alertas basadas en valores criticos.
<h2 align="center">La pagina web</h2>
Consiste principalmente en almacenamiento y visualizacion de datos de los datos recibidos, ademas los usuarios que tengan poder de administrador tienen la capacidad de establecer un valor minimo y maximo para cada tipo de dato (temperatura, presión y humedad) y para cada modulo con el fin de enviar una alerta.
<h3>Detalles del desarrollo</h3>
- Frontend: Fue desarrollado usando HTML y CSS.
- Backend: Fue desarrollando en Python V3.12 usando el framework Django V5.1 y el modulo Django Rest Framework V3.15 para desarrollar la API REST
- Base de datos: MySQL
---
<h3>Modulos</h3>
Cada modulo debe enviar su id con el que fue registrado, la ubicación donde se encuentra y los datos de temperatura en grados celcius [°C], humedad en humedad relativa [%] y presión en hectopascales [hPa].
<h3>Valores Criticos</h3>
Para cada tipo de dato se puede establecer un valor maximo y/o minimo con el fin de enviar una alerta mediante la aplicacion de telefono y mostrar ese valor de manera distintiva en la pagina web.
---
Finalmente no se pudo desarrollar la aplicación de telefono, pero se estableció la estructura para poder intercomunicar la pagina web con la aplicación.

