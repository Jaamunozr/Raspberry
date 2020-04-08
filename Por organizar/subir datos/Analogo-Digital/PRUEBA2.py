import time #Comparando el valor del canal 0
import Adafruit_ADS1x15
##----
from pylab import *

# importar el MOdulo pyplot
import matplotlib.pyplot as plt
In [1]: from pylab import *      # importar todas las funciones de pylab
In [2]: x = arange(10.)          # array de floats, de 0.0 a 9.0

AIn [3]: plot(x)                  # generar el gráfico de la funciOn y=x
Out[3]: [<matplotlib.lines.Line2D object at 0x9d0f58c>]

In [4]: show() 


##----
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1 #Ganancia
adc.start_adc_comparator(0, #numero del canal
                         10000, 9000,  # High threshold value, low threshold value
                         active_low=True, traditional=True, latching=False,
			 #active_high=True, traditional=True, latching=False,
                         num_readings=1, gain=GAIN)
print('Reading ADS1x15 channel 0 for 5 seconds with comparator...')
#solo imprime este fragmento de texto
start = time.time()
while (time.time() - start) <= 50.0: #Imprime datos durante 50 seg.
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
#     print('Channel 0:' + value)    ###Verificar porque no se puede imprimir asi
    time.sleep(0.25)
adc.stop_adc()
