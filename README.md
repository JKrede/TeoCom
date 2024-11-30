<h1 align="center">Proyecto <div color="#2c5f66">Con</div><div color="#ddc77a">Sens</div></h1>
A través de distintos modulos arduino con sensores de presion, temperatura y humedad con el fin de recolectar dichos datos y una antena con su correspondiente modulo ("Industrial wireless communication" (NRF24L01) o "LoRa" (RFM95)) para transmitir los datos recolectados a un Gateway desarrollado con un ESP32S y este a su vez enviar los datos a la pagina web con el fin de ser guardados en una base de datos, mostrar dichos datos en una pagina web y en una aplicacion de telefono, y ademas enviar alertas basadas en valores criticos.
<h2 align="center">La pagina web</h2>
Consiste principalmente en almacenamiento y visualizacion de datos de los datos recibidos, ademas los usuarios que tengan poder de administrador tienen la capacidad de establecer un valor minimo y maximo para cada tipo de dato (temperatura, presion y humedad) y para cada modulo con el fin de enviar una alerta.
<h3 align="center">Detalles de desarrollo</h3>
Frontend: Fue desarrollado usando HTML y CSS.
Backend: Fue desarrollando en Python V3.12 usando el framework Django V5.1 y el modulo Django Rest Framework V3.15 para desarrollar la API REST, y el motor de base de datos usado fue MySQL


