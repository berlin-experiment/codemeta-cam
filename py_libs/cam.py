import subprocess
import os

# captures + saves jpg
def capture_image(PATH):
	print("Capturing image, please hold still...")
	p = subprocess.run(["libcamera-still", "--nopreview", "--output", PATH + "/data/test.jpg", "--width", "640", "--height", "480" ], capture_output=True)
	if p.returncode == 1:
		print("An error ocurred during the capturing process...")
	else:
		print("Image captured successfully")
	return p.returncode
