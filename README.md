<h1 align="center">Proyecto ConSens</h1>
A través de distintos modulos Arduino equipados con sensores de presión, temperatura y humedad con el fin de recolectar esos datos, y una antena con su correspondiente modulo ("Industrial wireless communication" (NRF24L01) o "LoRa" (RFM95)) para transmitir los datos recolectados a un Gateway desarrollado con un ESP32S y este a su vez enviar los datos a la pagina web con el fin de ser guardados en una base de datos, mostrar dichos datos en la pagina y en una aplicacion de telefono, y además enviar alertas basadas en valores criticos.
<h3>Modulos</h3>
Cada modulo debe enviar su id con el que fue registrado, la ubicación donde se encuentra y los datos de temperatura en grados celcius[°C], humedad en humedad relativa[%] y presión en hectopascales [hPa].
<h3>Valores Criticos</h3>
Para cada dato se puede establecer un valor maximo y/o minimo (en el caso de poner un solo valor el otro se autocompleta utilizando el anterior) con el fin de enviar una alerta mediante la aplicacion de telefono y mostrar ese valor de manera distintiva en la pagina web.
Cada modulo debe enviar su id con el que fue registrado, la ubicación donde se encuentra y los datos de temperatura en grados celcius[°C], humedad en humedad relativa[%] y presión en hectopascales [hPa].
<h2 align="center">La pagina web</h2>
Consiste principalmente en almacenamiento y visualizacion de datos de los datos recibidos, ademas los usuarios que tengan poder de administrador tienen la capacidad de establecer un valor minimo y maximo para cada tipo de dato (temperatura, presión y humedad) y para cada modulo con el fin de enviar una alerta.
<h3>Detalles de desarrollo</h3>
Frontend: Fue desarrollado usando HTML y CSS.
Backend: Fue desarrollando en Python V3.12 usando el framework Django V5.1 y el modulo Django Rest Framework V3.15 para desarrollar la API REST, y el motor de base de datos utilizado fue MySQL.

