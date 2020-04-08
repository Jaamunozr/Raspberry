import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1 #Ganancia de acuerdo al nivel de tension
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.center(70,"*")) #imprime columna
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4))) #impresion prueba
print('-' * 37)
while True:
    values = [0]*4
    for i in range(4):
	#Lea el valor del canal i en abc usando el valor de ganacia establecido
        values[i] = adc.read_adc(i,gain=GAIN)
        ####values[i] = adc.read_adc(i, GAIN, data_rate=128)
        #Data rate must be one of: 8, 16, 32, 64, 128, 250, 475, 860
    # Se imprimen los valores capturados
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    #Pausa:
    time.sleep(0.1)
