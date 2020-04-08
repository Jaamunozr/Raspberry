import RPi.GPIO as GPIO
import time
#pwmSetMode(PWM_MODE_MS)
#pwmFrequency in Hz = 19.2e6 Hz/pwmClock/pwmRange
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24,30000) #Salida ,  Frecuencia
p.start(50)
while True:
	p.ChangeDutyCycle(20)
#input('Press return to stop:')   # use raw_input for Python 2
#p.stop()
#GPIO.cleanup()
