#Importa elementos de los diferentes modulos que usara
import time
import Adafruit_GPIO.SPI as SPI #Importa libreria de Adafruit y la nombra SPI
import Adafruit_SSD1306 #Importa otra libreria de Adafruit para el Display

from PIL import Image
from PIL import ImageDraw #Dibujo
from PIL import ImageFont #Fuente

import subprocess
#Configuracion de los pines en Raspberry Pi
RST = None     # en el PiOLED este pin no se usa      NONE = ninguna
# Tenga en cuenta que los siguientes solo se utilizan con SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display con hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Inicializar Biblioteca
disp.begin()  #Begin =Empezar

# Borrar display.
disp.clear()
disp.display()

#Crear imagen en blanco para dibujar.
# Asegurese de crear una imagen con el modo '1' para el color de 1 bit.
width = disp.width #Width = Ancho
height = disp.height #Height = Alto
image = Image.new('1', (width, height))
# Obtener objeto de dibujo para dibujar en la imagen.
draw = ImageDraw.Draw(image)

# Dibuja un cuadro lleno de negro para borrar la imagen.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Alternativamente, carga una fuente TTF.
# la "coma" con el numero indica el tamano del objeto o letra cargada
LETRA1 = ImageFont.truetype('Montserrat-Light.ttf', 12) #LETRA
LETRA2 = ImageFont.truetype('Montserrat-Medium.ttf', 19) #LETRA
IMAGEN1 = ImageFont.truetype('fontawesome-webfont.ttf', 52) #IMAGENES
IMAGEN2 = ImageFont.truetype('fontawesome-webfont.ttf', 64) #IMAGENES
#font_text_big = ImageFont.truetype('Montserrat-Medium.ttf', 19) #LETRA
k=0
while True:
	while True:
#	while (k<=10):
	 k+=1
# Dibuja un cuadro lleno de negro para borrar la imagen.
	 draw.rectangle((0,0,width,height), outline=0, fill=0)
# ICONOS: Desde aqui podemos imprimir los iconos segun existan en el archivo .ttf
	 draw.text((30, 0),   unichr(int("f17c", 16)),  font=IMAGEN1, fill=255) #Imagen 1
###    draw.text((50, 52), unichr(int("f1c0", 16)),  font=IMAGEN1, fill=255) #Imagen 2
###    draw.text((0, 52),  unichr(int("f2c8", 16)),  font=IMAGEN1, fill=255) #Imagen 3
###    draw.text((0, 15),  unichr(int("f2db", 16)),  font=IMAGEN2, fill=255) #Imagen 4
#TEXTO
	 draw.text((22, 52),  str("RasPi 3 b+"),  font=LETRA1, fill=255)
         draw.text((18, 0),  str("hola mundo"),  font=LETRA1, fill=255)
###    draw.text((32, 12), str("HOLA MUNDO"), font=LETRA2, fill=255)
##Los numeros a la derecha desplazan el texto para arriba o abajo
##Los numeros a la izquierda desplazan texto a derecha o izquierda

	 disp.image(image)
	 disp.display()
	 time.sleep(2)
######## # Dibuja un cuadro lleno de negro para borrar la imagen.
	 disp.clear()
	 draw.rectangle((0,0,width,height), outline=0, fill=0)
	 draw.text((30, 0),   unichr(int("f17b", 16)),  font=IMAGEN2, fill=255) #Imagen 1
	 disp.image(image)
	 disp.display()
	 time.sleep(2)
###############
######## # Dibuja un cuadro lleno de negro para borrar la imagen.
         disp.clear()
         draw.rectangle((0,0,width,height), outline=0, fill=0)
         draw.text((30, 0),   unichr(int("f281", 16)),  font=IMAGEN2, fill=255) #Imagen 1
         disp.image(image)
         disp.display()
         time.sleep(2)
###############

