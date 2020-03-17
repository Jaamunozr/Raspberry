# Copyright (c) 2017 Industrias Adafruit
# Autor: Tony DiCola y James DeVito
#
# Se otorga el permiso, sin cargo, a cualquier persona que obtenga una copia.
# de este software y los archivos de documentacion asociados (el "Software"), para tratar
# en el Software sin restriccion, incluyendo sin limitacion los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y / o vender
# copias del Software, y para permitir que las personas a quienes el Software esta

# amueblado para hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluiran en
# Todas las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTIA DE NINGUN TIPO, EXPRESA O
# IMPLICADO, INCLUYENDO PERO NO LIMITADO A LAS GARANTIAS DE COMERCIALIZACION,
# APTITUD PARA UN PROPOSITO PARTICULAR Y NO INCUMPLIMIENTO. EN NINGUN CASO DEBE

# LOS AUTORES O LOS TITULARES DEL DERECHO DE AUTOR SERAN RESPONSABLES POR CUALQUIER RECLAMACION, DANO O OTRO

# RESPONSABILIDAD, PESADA EN UNA ACCION DE CONTRATO, TORTADA O DE OTRA MANERA, DERIVADA DE,
# FUERA O EN CONEXION CON EL SOFTWARE O EL USO O OTRAS REPARACIONES EN
# EL SOFTWARE.
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

#Configuracion de los pines en Raspberry Pi
RST = None     # en el PiOLED este pin no se usa
# Tenga en cuenta que los siguientes solo se utilizan con SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display con hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Inicializar Biblioteca
disp.begin()

# Borrar display.
disp.clear()
disp.display()

#Crear imagen en blanco para dibujar.
# AsegUrese de crear una imagen con el modo '1' para el color de 1 bit.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Obtener objeto de dibujo para dibujar en la imagen.
draw = ImageDraw.Draw(image)

# Dibuja un cuadro lleno de negro para borrar la imagen.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Dibuja algunas formas.
# Primero, defina algunas constantes para permitir un facil cambio de tamano de las formas.
padding = -2
top = padding
bottom = height-padding
81/5000
# Mueva de izquierda a derecha siguiendo la posicion x actual para dibujar formas.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternativamente, carga una fuente TTF. Asegurese de que el archivo de fuente .ttf este en el mismo directorio que python scr $
# Algunas otras fuentes agradables para probar: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('Montserrat-Light.ttf', 12)
font2 = ImageFont.truetype('fontawesome-webfont.ttf', 14)
font_icon_big = ImageFont.truetype('fontawesome-webfont.ttf', 20)
font_text_big = ImageFont.truetype('Montserrat-Medium.ttf', 19)

while True:
    # Dibuja un cuadro lleno de negro para borrar la imagen.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts para la supervision del sistema desde aqui: https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1 | head --bytes -1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"MEM: %.2f%%\", $3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"HDD: %d/%dGB %s\", $3,$2,$5}'"
    cmd = "df -h | awk '$NF==\"/\"{printf \"%s\", $5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp | cut -d '=' -f 2 | head --bytes -1"
    Temperature = subprocess.check_output(cmd, shell = True )

    # Iconos
    draw.text((x, top),       unichr(61931),  font=font2, fill=255)
    draw.text((x+50, top+52), unichr(61888),  font=font2, fill=255)
    draw.text((x, top+52),    unichr(62152),  font=font2, fill=255)
    draw.text((x, top+15),    unichr(62171),  font=font_icon_big, fill=255)

    draw.text((18, top),      str(IP),  font=font, fill=255)
    draw.text((x+22, top+12), str(CPU), font=font_text_big, fill=255)
    draw.text((x, top+36),    str(MemUsage),  font=font, fill=255)
    #draw.text((x, top+39),   str(Disk),  font=font, fill=255)
    draw.text((x+66, top+52), str(Disk),  font=font, fill=255)
    draw.text((x+10, top+52), str(Temperature),  font=font, fill=255)


    # Mostrar Imagen
    disp.image(image)
    disp.display()
    time.sleep(5)
