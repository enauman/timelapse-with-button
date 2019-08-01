import RPi.GPIO as GPIO
import time
import picamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
prev_input = 1
buttonPin = 8
ledPin = 17
GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(ledPin,GPIO.OUT)

camera = picamera.PiCamera(resolution=(1280, 720), framerate=30)
# Set ISO to the desired value
camera.iso = 200
# Wait for the automatic gain control to settle
time.sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
camera.hflip = True
camera.vflip = True
interval = 5 # In seconds
number = 180 #Total number of pictures
# @5 sec interval, 180 pics = 15 min
def timelapse():
	for i, filename in enumerate(
	camera.capture_continuous('pics/image{counter:04d}.jpg')):
		print(filename)
		time.sleep(interval)
		if i == number:
			break

while True:
        #take reading
        input = GPIO.input(buttonPin)
        if ((not prev_input) and input):
                GPIO.output(ledPin,True)
                timelapse()
                GPIO.output(ledPin,False)
        #update previous input
        prev_input = input
        #pause
        time.sleep(0.5)

