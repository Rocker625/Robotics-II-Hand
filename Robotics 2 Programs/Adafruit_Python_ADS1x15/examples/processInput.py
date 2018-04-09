from __future__ import division
import time
import Adafruit_ADS1x15
import Adafruit_PCA9685

adc = Adafruit_ADS1x15.ADS1115()
pwm = Adafruit_PCA9685.PCA9685()

GAIN = 1
channel = 0

pwm.set_pwm_freq(60)

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    inputValue = 0
    inputValue = adc.read_adc(channel, gain=GAIN)
    servoValue = int(inputValue/50+75)
    print(servoValue)
    pwm.set_pwm(0, 0, servoValue)
    time.sleep(0.1)
