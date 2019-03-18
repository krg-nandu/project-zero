import RPi.GPIO as GPIO
import time
import os

BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

def notify_button_press():
	os.system("espeak -ven+f5 -s170 'Go Ahead'")

def collect_and_process_audio():
	os.system("bash get_and_parse_input.sh")
	return 'tmpf.txt'

def voice_error_message():
	os.system("espeak -ven+f5 -s170 'I did not understand that'")

def voice_introduce():
	os.system("espeak -ven+f5 -s170 'My name is zero. I am still in beta mode'")
def main():
	# passively wait for the hardware trigger
	while True:
		state = GPIO.input(BUTTON)
		print(state)
		# on button press
		if not state:
			# first signal that Zero is ready to listen
			notify_button_press()
			# collect audio input from the microphone
			outputf = collect_and_process_audio()
			#outputf = 'output2.txt'
			#import ipdb; ipdb.set_trace();
			stri = open(outputf,'r').read().strip('\n\"\'')
			if stri == "introduce yourself":
				voice_introduce()
			else:
				voice_error_message()
		# continue listening
		time.sleep(0.2)

if __name__ == '__main__':
	main()
