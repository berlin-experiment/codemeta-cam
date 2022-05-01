import subprocess
import os
# detects things in image and saves output.png
def darknet_detect(PATH):
	print("Running detector, this can take a while...")
	p = subprocess.run("./darknet detect cfg/yolov3.cfg yolov3.weights ./data/test.jpg", shell=True,cwd=PATH,capture_output=True)
	output =p.stdout.decode("utf-8") 	#decode bytes to string
	outputList = output.split("\n") 	#split by newlines
	
	# loop through each stdout line and search for "Predicted in" to know where the prediction starts
	startValue = 0
	for line in outputList:
		
		if line.find("Predicted in ")>0:
			print(line.split(": ")[1])
			startValue+=1
			break
		else:
			startValue+=1
	  
	# loop through each prediction and split on ": " to get the item and certainty
	# if the item is equal to "person" increment the people variable
	i = startValue
	people = 0 # <- people variable
	print("Items detected:")
	while i < len(outputList) -1:
		detection =outputList[i].split(": ")
		item = detection[0]
		certainty = detection[1]
		print("Detected a "+item+ " with " + certainty+" certainty")
		if item == "person":
			people+=1
			
		i+=1
	
	# print the number of people detected, and return the exit status code and the number of people counted
	print("Detected "+str(people)+" person(s)")
	return p.returncode, people
