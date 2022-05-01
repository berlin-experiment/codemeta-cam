import os
from py_libs.cam import capture_image
from py_libs.detect import darknet_detect

# gets our current working directory for metacam
PATH = os.getcwd() + "/darknetV2"

# to ensure we capture an image

try:
	while True:
		new_img = 1
		while new_img == 1:
			new_img = capture_image(PATH)
			
		err, people = darknet_detect(PATH)
		print("Detector detected "+ str(people)+" person(s)")
		
except KeyboardInterrupt:
	print("Cheusies")
