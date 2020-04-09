import time
import Adafruit_ADS1x15
import datetime
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} '.format(1))
print('-' * 37)
k=0
tension=[]
tiempo=[]
p=1
while p==1:
    while k<1000:
        k=k+1
        #time.sleep(0.5)
        tension.append(adc.read_adc(0, gain=GAIN, data_rate=860))
        #print(values)
        tiempo.append(datetime.datetime.now())
    else:
        tension=str(tension)
        tiempo=str(tiempo)
        texto=open("texto.xlsx","w")
        texto.write(tension + '\n')
        #texto.write("
        texto.write(tiempo)
        texto.close()
    p=0