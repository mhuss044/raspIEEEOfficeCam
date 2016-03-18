import RPi.GPIO as GPIO
import time
def startMotor():
	GPIO.setmode(GPIO.BCM)		# broadcom pin numbering scheme
	GPIO.setwarnings(False)

	buzzer = 18
	motor = 25
	duty = 10
	GPIO.setup(motor, GPIO.OUT)
	GPIO.setup(buzzer, GPIO.OUT)
	pwm = GPIO.PWM(buzzer, 850) # init pwm, on buzzerPin, f = 100hz

	try:
		pwm.start(duty)	# duty cycle set 0 - 100
		pwm.ChangeDutyCycle(duty)
		GPIO.output(motor, True)
		time.sleep(3)
		GPIO.output(motor, False)
	except:
		pass
	finally:
		pwm.stop()
		GPIO.cleanup()


