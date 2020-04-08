#import glob
import RPi.GPIO as GPIO		#Importa libreria  "RPi.GPIO" y les reasigna un nombre "GPIO"
import time			#Importa libreria "time"
import os			#Importa libreria "os" para borrar datos en terminal y no dejar acumular
from datetime import datetime
k=0
GPIO.setwarnings(False) #IMPORTANTE - ESTE COMANDO ELIMINA LAS POSIBLES ADVERTENCIAS
GPIO.setmode(GPIO.BCM) #Indica que se utilizara  la numeracion de BROADCOM y no la fisica
GPIO_TRIGGER =23 #Se usara el pin GPIO 23
GPIO_ECHO    =24 #Se usara el pin GPIO 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)   #Configuracion de pin 23 como salida
GPIO.setup(GPIO_ECHO,GPIO.IN)       #Configuracion de pin 24 como entrada
GPIO.output(GPIO_TRIGGER, False)    #Salida de pin 23 en 0 logico

sFileStamp = time.strftime('%Y.%m.%d,%H:%M')
"""Genera una variable cuyo dato sea la fecha y hora, y de acuerdo a su ultima letra (M=Minuto) permite guardar 
un documento de texto cada minuto"""

sFileName = 'out/' + sFileStamp + '.txt'
"""Indica que se debe GENERAR una variable de nombre "sFileName" que se guardara en la carpeta 'out'
y tendra en su interior la variable 'sFileName' y '.txt'. ADICIONALMENTE, PODEMOS GENERAR CUALQUIER EXTENCION PARA GUARDAR 
NUETROS ARCHIVOS, YA SE PROBO EN .docx   """

f=open(sFileName, 'a')
''' "a" permite editar y/o crear un archivo (solo si no existe), poniendo como nombre lo que se encuentra
 en la variable "sFileName", generando asi un archivo de texto (.txt) '''

f.write('Date, Time, Sample' + '\n') #Guarda el rotulo del texto en el documento creado en el archivo .txt
print "Inicia proceso de captura de datos."
try:     #COMANDO DE EXCEPCIONES "Que pase esto pero si muestra excepciones no entraria o se salta"
	while True:
#	while k<=20:
		print"Esperando por sensor"
		GPIO.output(GPIO_TRIGGER,True)   #Habilita la salida 23 (1 logico)
		time.sleep(0.000001)
		 #Genera un retardo en el programade  1 us (micro-segundo)
		 #para el Trigger, duracion minima del pulso de
		 #disparo
		GPIO.output(GPIO_TRIGGER,False)  #Deshabilita la salida 23 (0 logico)
		start=time.time()
				#Tiempo Universal Coordinado (UTC), convierte el
				#dato y la hora actual en segundos y los almacena en
				#la variable (start)    """
		while GPIO.input(GPIO_ECHO)==0:	 #Mientras que el pin 24 sea igual a "0" se realizara lo siguiente
			start=time.time()	 #Se guarda el dato inicial de muestreo en funcion de la fecha
						 #y hora en segundos en la variable "Start".'''
		while GPIO.input(GPIO_ECHO)==1:	 #Mientras que el pin 24 sea igual a "1" se realizara lo siguiente
			stop=time.time()	  #Se guardara el dato inicial de muestreo en funcion  de la fecha
						  # y hora en segundos en la variable "stop".'''
		elapsed=stop-start		#Se realiza la diferencia de horario para establecer el tiempo de demora
		distance=(elapsed*34300)/2	#Guarda el valor de la dstancia calculada de la siguiente manera:

						#V=2d/t o bien d=V*t/2 teniendo en cuenta que la velocidad del
						#sensor es de aproximadamente 343m/s o 34300cm/s  que es
						# aproximadamente la velocidad del sonido
 		sTimeStamp=time.strftime('%Y.%m.%d,%H:%M:%S')  #Variable que almacena la fecha
		f.write(sTimeStamp + ',' +str(distance) + '\n') #Guarda en el documento .txt el dato de la fecha, un
								# espacio y el dato de distancia calculada'''
		os.system("clear")	#Borra lo datos en la terminal, no los deja acumular
		print sTimeStamp + ' ' + str(distance)
		time.sleep(1) 			#Tiempo para visualizar el dato capturado
		sTmpFileStamp  = time.strftime('%Y.%m.%d,%H:%M') #Guarda el dato de la fecha en esa nueva variable POR MINUTO
		#k+=1
		if sTmpFileStamp <> sFileStamp:  #Ejemplo de operador de comparacion "Diferente" entre horas
			f.close #cierra el .txt
			sFileName = 'out/' + sTmpFileStamp + '.txt' #Genera un nuevo .txt con la nueva fecha como nombre
			f=open(sFileName, 'a')  #Permite abrir y editar el archivo
			sFileStamp = sTmpFileStamp #Configura las dos horas a comparar como iguales
			print 'Creating new file'  #Imprime la observacion de que ya se tiene un nuevo docuemnto cargand datos

except KeyboardInterrupt:  # Esto solo pasara si presiona "Ctrl+C"
	print '\n' + 'Termina ejecucion de programa' + '\n'
	print 'Hasta la vista'
	GPIO.cleanup() #Reinicia la configuracion de los pines GPIO
