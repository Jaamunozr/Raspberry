import time
import Adafruit_ADS1x15
import datetime
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} '.format(1))
print('-' * 37)
k=0
while True:
    k=k+1
    #values= adc.read_adc(0, gain=GAIN)
    values= adc.read_adc(0, gain=GAIN, data_rate=860)
    #print('| {0:>6} | '.format(values))    
    #time.sleep(0.5)
    print(k)
    print(datetime.datetime.now())