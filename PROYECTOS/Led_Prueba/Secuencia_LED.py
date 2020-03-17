import RPi.GPIO as GPIO
#Libreria instalada por defecto, abreviamos su nombre con el comando "as" y lo llamaremos "GPIO"
import time
#importa la libreria de tiempo
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Manera de asignar pines por medio de Broadcom y NO segun su configuracion fisica 
k=0
#GPIO.setmode(GPIO.BOARD) #Manera de asignar los pines de acuerdo a su asignacion  fisica

GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
#Nombramos los pines y bajo que configuracion se mantendran (Salida o entrada)
try:
	while True:
#if k<10:

		k+=1
		#Generamos un bucle infinito con "True" para que prendan y apaguen los led's
	        GPIO.output(26,GPIO.HIGH)
		#Encendemos el led conectado a pin 26
		time.sleep(0.5)
		#Damos un tiempo para que el siguiente led encienda, basicamente lo que hace este comando es generar un retardo  en el programa
		GPIO.output(19, True)
		#Encendemos el led conectado al pin 19 pero con otro comando
		time.sleep(0.5)
	       	GPIO.output(13, True)
		time.sleep(0.5)

		GPIO.output(13, False)
		GPIO.output(19, GPIO.LOW)
		GPIO.output(26, False)
		time.sleep(0.5)

		GPIO.output(13, True)
        	GPIO.output(19, GPIO.HIGH)
	        GPIO.output(26, True)
        	time.sleep(0.5)

		GPIO.output(13, False)
        	GPIO.output(19, GPIO.LOW)
	        GPIO.output(26, False)
        	time.sleep(0.5)

		GPIO.output(13, True)
        	GPIO.output(19, GPIO.HIGH)
	        GPIO.output(26, True)
        	time.sleep(0.5)

		GPIO.output(13, False)
		time.sleep(0.5)
	        GPIO.output(19, GPIO.LOW)
		time.sleep(0.5)
	        GPIO.output(26, False)
	        time.sleep(0.5)
except KeyboardInterrupt:
#	KeyboardInterrupt
	GPIO.cleanup()
