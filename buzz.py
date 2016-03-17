import RPi.GPIO as GPIO
import time
def startMotor():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	buzzer = 18
	GPIO.setup(buzzer, GPIO.OUT)

	try:
		GPIO.output(buzzer, True)
		time.sleep(3)
		GPIO.output(buzzer, False)
	except:
		pass
	finally:
		GPIO.cleanup()


