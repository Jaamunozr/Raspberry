import time #Comparando el valor del canal 0
import Adafruit_ADS1x15
from pylab import *
y=[]
x=[]
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1 #Ganancia
adc.start_adc_comparator(0, #numero del canal
                         2506, 1000,  # High threshold value, low threshold value
                         active_low=True, traditional=True, latching=False,
			 #active_high=True, traditional=True, latching=False,
                         num_readings=1, gain=GAIN)
print('Reading ADS1x15 channel 0 for 5 seconds with comparator...')
#solo imprime este fragmento de texto
start = time.time()
i =0
while (time.time() - start) <= 10.0: #Imprime datos durante 50 seg.
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
    x.append(i)
    i=i+1
    y.append(value)
    time.sleep(0.1)
    plot(x,y,color='green')
    legend( ('Pinza CH1',), loc = 'upper left')
    title('Grafica de corriente')
    grid(True)
    show(block = False)
    close()
adc.stop_adc()
