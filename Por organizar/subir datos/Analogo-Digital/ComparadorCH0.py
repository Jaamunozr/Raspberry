import time #Comparando el valor del canal 0
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1 #Ganancia
adc.start_adc_comparator(0, #numero del canal
                         #10000, 9000,  # High threshold value, low threshold value
			 2506,1000,
			 #Umbral = Threshold
                         active_low=True, traditional=True, latching=False,
			 #active_high=True, traditional=True, latching=False,
			 #Latching=Cerrojo
                         num_readings=1, gain=GAIN)
print('Reading ADS1x15 channel 0 for 5 seconds with comparator...')
start = time.time()
while (time.time() - start) <= 50.0:
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
#     print('Channel 0:' + value)    ###Verificar porque no se puede imprimir asi
    time.sleep(0.25)
adc.stop_adc()
