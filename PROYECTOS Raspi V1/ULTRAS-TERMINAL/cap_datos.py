#PROGRAMA SIN MODIFICACIONES

#import glob
import RPi.GPIO as GPIO
import time
from datetime import datetime
k=0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER =23
GPIO_ECHO    =24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)

sFileStamp = time.strftime('%Y%m%d%H%M')
sFileName = 'out/' + sFileStamp + '.txt' #Indica que se debe Guardar o abrir en la carpeta  "out"
f=open(sFileName, 'a')
f.write('Date, Time, Sample' + '\n') #Imprime y guarda el rotulo del texto
print ('Inicia proceso de captura de datos.')
try:
    while True:
#   while k<10:
        print ("Esperando por sensor")
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.000001)
        GPIO.output(GPIO_TRIGGER,False)
        start=time.time()
        while GPIO.input(GPIO_ECHO)==0:
            start=time.time()
        while GPIO.input(GPIO_ECHO)==1:
            stop=time.time()
        elapsed=stop-start
        distance=(elapsed*34300)/2
        sTimeStamp=time.strftime('%Y%m%d,%H:%M:%S')  #Variable que almacena la fecha
        f.write(sTimeStamp + ',' +str(distance) + '\n') #Imprime la fecha, un espacio y el dato de distancia 
        print (sTimeStamp + ' ' + str(distance))
        time.sleep(0.1) #Tiempo para imprimir y guardar cada  dato capturado
        sTmpFileStamp  = time.strftime('%Y%m%d%H%M')
#       k+=1
        if sTmpFileStamp != sFileStamp:
            f.close
            sFileName = 'out/' + sTmpFileStamp + '.txt'
            f=open(sFileName, 'a')
            sFileStamp = sTmpFileStamp
            print ('Creating new file')

except KeyboardInterrupt:
    print ('\n' + 'Termina ejecucion de programa' + '\n')
    print ('Hasta la vista')
    GPIO.cleanup()


