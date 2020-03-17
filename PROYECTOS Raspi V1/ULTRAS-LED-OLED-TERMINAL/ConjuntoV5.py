import time
import RPi.GPIO as GPIO
#### Datos configuracion de Sensor
import os     #Importa libreria "os" para borrar datos en terminal y no$
from datetime import datetime
GPIO.setwarnings(False) #IMPORTANTE - ESTE COMANDO ELIMINA LAS POSIBLES ADVERTENCIAS
GPIO.setmode(GPIO.BCM) #Indica que se utilizara  la numeracion de BROADCOM y no la fisica
GPIO_TRIGGER =23 #Se usara el pin GPIO 23
GPIO_ECHO    =24 #Se usara el pin GPIO 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)   #Configuracion de pin 23 como salida
GPIO.setup(GPIO_ECHO,GPIO.IN)       #Configuracion de pin 24 como entrada
GPIO.output(GPIO_TRIGGER, False)    #Salida de pin 23 en 0 logico
TTiempo = time.strftime('%Y.%m.%d,%H:%M')
Inicio=0
Documento = 'out/' + TTiempo + '.txt'
f=open(Documento, 'a')
f.write('Date, Time, Sample' + '\n')

print "Inicia proceso de captura de datos."
########################### Datos configuracion de OLED
import time
import Adafruit_GPIO.SPI as SPI #Importa libreria de Adafruit y la nombra SPI
import Adafruit_SSD1306 #Importa otra libreria de Adafruit para el Display
from PIL import Image
from PIL import ImageDraw #Dibujo
from PIL import ImageFont #Fuente
import subprocess
RST = None  # En el PiOLED este pin no se usa      NONE = ninguna
DC = 23 	# pin que solo se utilizan con SPI
SPI_PORT = 0    # pin que solo se utilizan con SPI
SPI_DEVICE = 0  # pin que solo se utilizan con SPI
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)  # 128x64 display con hardware I2C:
disp.begin()  #Begin =Empezar
disp.clear()  #Borra Display OLED
disp.display() #Configuracion pantalla
width = disp.width #Width = Ancho
height = disp.height #Height = Alto
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image) # Obtener objeto de dibujo para dibujar en la imagen.
draw.rectangle((0,0,width,height), outline=0, fill=0) # Dibuja un cuadro lleno de negro para borrar la imagen.
# La "coma" con el numero indica el tamano del objeto o letra cargada
LETRA1 = ImageFont.truetype('Montserrat-Light.ttf', 12)     #LETRA Cargada por fuente TTF
LETRA2 = ImageFont.truetype('Montserrat-Medium.ttf', 19)    #LETRA Cargada por fuente TTF
IMAGEN1 = ImageFont.truetype('fontawesome-webfont.ttf', 52) #IMAGENES Cargada por fuente TTF
IMAGEN2 = ImageFont.truetype('fontawesome-webfont.ttf', 64) #IMAGENES Cargada por fuente TTF
#############################3###Fin configuraciones
try:
        while True:
###################### Inicio Presentacion
		while Inicio ==0:
			Inicio=1;
	                draw.rectangle((0,0,width,height), outline=0, fill=0)
        	        draw.text((20, 0),   unichr(int("f17c", 16)),  font=IMAGEN1, fill=255) #Imagen 1
               		draw.text((18, 52),  str("RasPi 3 B+"),  font=LETRA1, fill=255)
	                draw.text((60, 0),  str("Hola "),  font=LETRA1, fill=255)
			draw.text((60, 15), str("Mundo 1.0"), font=LETRA1, fill=255)
        	        disp.image(image)
	                disp.display()
			time.sleep(1)
####################   Fin presentacion
###################### Inicio captura y alamcenamiento de datos

                print "Esperando por sensor"
                GPIO.output(GPIO_TRIGGER,True)   #Habilita la salida 23 (1 logico)
                time.sleep(0.000001)
                GPIO.output(GPIO_TRIGGER,False)  #Deshabilita la salida 23 (0 logico)
                start=time.time()
                while GPIO.input(GPIO_ECHO)==0:  #Mientras que el pin 24 sea igual a "0" $
                        start=time.time()        #Se guarda el dato inicial de muestreo e$
                while GPIO.input(GPIO_ECHO)==1:  #Mientras que el pin 24 sea igual a "1" $
                        stop=time.time()          #Se guardara el dato inicial de muestre$
                elapsed=stop-start              #Se realiza la diferencia de horario para$
                distance=(elapsed*34300)/2      #Guarda el valor de la dstancia calculada$
                FechaHoraRegistrada=time.strftime('%Y.%m.%d,%H:%M:%S')  #Variable que almacena la $
		Fecha=time.strftime('%d - %m - %Y')
		Hora=time.strftime('%H:%M:%S')
                f.write(FechaHoraRegistrada + ',' +str(distance) + '\n') #Guarda en el documento .$
#               os.system("clear")      #Borra lo datos en la terminal, no los deja acumu$
                Dato=( FechaHoraRegistrada + ' ' + str(distance))
		Distancia=str(distance)
		print Dato
                FechaHoraMin= time.strftime('%Y.%m.%d,%H:%M') #Guarda el dato de la fe$
                if FechaHoraMin <> TTiempo:  #Diferencia entre Hora Min actual y el Hora Min registrado
                        f.close #cierra el .txt
                        Documento = 'out/' + FechaHoraMin + '.txt' #Genera un nuevo .txt$
                        f=open(Documento, 'a')  #Permite abrir y editar el archivo
                        TTiempo = FechaHoraMin #Configura las dos horas a comparar co$
                        print 'Nuevo archivo creado'  #Imprime la observacion de que ya se t$
###################  Fin Capturas de datos
###################  Inicio impresion de pantalla OLED
                disp.clear()
                draw.rectangle((0,0,width,height), outline=0, fill=0)
                draw.text((0,0),  str("-- Fecha --"),  font=LETRA1, fill=255)
                draw.text((0,10),  str(Fecha),  font=LETRA1, fill=255)
		draw.text((0,20),  str("-- Hora --"),  font=LETRA1, fill=255)
                draw.text((0,30),  str(Hora),  font=LETRA1, fill=255)
		draw.text((0,40),  str("-- Dato sensor --"),  font=LETRA1, fill=255)
                draw.text((0,50),  str(Distancia),  font=LETRA1, fill=255)
               	disp.image(image)
                disp.display()
###################  Fin impresion de pantalla OLED
		time.sleep(0.999999)
except KeyboardInterrupt:  # Esto solo pasara si presiona "Ctrl+C"
        print '\n' + 'Termina ejecucion de programa' + '\n'
        print 'Hasta la vista'
	disp.clear()
	disp.display()
        GPIO.cleanup() #Reinicia la configuracion de los pines GPIO
