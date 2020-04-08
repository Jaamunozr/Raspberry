import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
k=0
###########################
import os     #Importa libreria "os" para borrar datos en terminal y no$
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
sFileName = 'out/' + sFileStamp + '.txt'
f=open(sFileName, 'a')
f.write('Date, Time, Sample' + '\n')

print "Inicia proceso de captura de datos."
try:
        while True:
#       while k<=20:

####
		k+=1
                GPIO.output(26,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(19, True)
                time.sleep(0.5)
                GPIO.output(13, True)
                GPIO.output(13, True)
                time.sleep(0.5)

                GPIO.output(13, False)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, False)
                time.sleep(0.5)

                GPIO.output(13, True)
                GPIO.output(19, GPIO.HIGH)
                GPIO.output(26, True)
                GPIO.output(26, True)
		time.sleep(0.5)

		GPIO.output(13, False)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, False)
                time.sleep(0.5)

                GPIO.output(13, True)
                GPIO.output(19, GPIO.HIGH)
                GPIO.output(26, True)
                GPIO.output(26, True)
                time.sleep(0.5)

                GPIO.output(13, False)
                time.sleep(0.5)
                GPIO.output(19, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(26, False)
                time.sleep(0.5)
###except KeyboardInterrupt:
###        GPIO.cleanup()




####

                print"Esperando por sensor"
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
                sTimeStamp=time.strftime('%Y.%m.%d,%H:%M:%S')  #Variable que almacena la $
                f.write(sTimeStamp + ',' +str(distance) + '\n') #Guarda en el documento .$
                os.system("clear")      #Borra lo datos en la terminal, no los deja acumu$
                print sTimeStamp + ' ' + str(distance)
                time.sleep(1)                   #Tiempo para visualizar el dato capturado
                sTmpFileStamp  = time.strftime('%Y.%m.%d,%H:%M') #Guarda el dato de la fe$
                #k+=1
                if sTmpFileStamp <> sFileStamp:  #Ejemplo de operador de comparacion "Dif$
                        f.close #cierra el .txt
                        sFileName = 'out/' + sTmpFileStamp + '.txt' #Genera un nuevo .txt$
                        f=open(sFileName, 'a')  #Permite abrir y editar el archivo
                        sFileStamp = sTmpFileStamp #Configura las dos horas a comparar co$

                        print 'Creating new file'  #Imprime la observacion de que ya se t$

except KeyboardInterrupt:  # Esto solo pasara si presiona "Ctrl+C"
        print '\n' + 'Termina ejecucion de programa' + '\n'
        print 'Hasta la vista'
        GPIO.cleanup() #Reinicia la configuracion de los pines GPIO
#############################
""" k

try:
        while True:
#if k<10:

                k+=1
                GPIO.output(26,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(19, True)
                time.sleep(0.5)
                GPIO.output(13, True)
                GPIO.output(13, True)
                time.sleep(0.5)

                GPIO.output(13, False)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, False)
                time.sleep(0.5)

                GPIO.output(13, True)
                GPIO.output(19, GPIO.HIGH)
                GPIO.output(26, True)
                GPIO.output(26, True)
                time.sleep(0.5)
##
                GPIO.output(13, False)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, False)
                time.sleep(0.5)

                GPIO.output(13, True)
                GPIO.output(19, GPIO.HIGH)
                GPIO.output(26, True)
                GPIO.output(26, True)
                time.sleep(0.5)

                GPIO.output(13, False)
                time.sleep(0.5)
                GPIO.output(19, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(26, False)
                time.sleep(0.5)
except KeyboardInterrupt:
        GPIO.cleanup()

"""
