# AUTHOR: saeed salimi shad
# ID INSTAGRAM: saeedsalimi_shad
# ID GITHUB: salimisaeed
# This script will detect faces via your webcam.
#-------------------------------------------------------------------------------
import cv2
cap = cv2.VideoCapture(0) # Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#-------------------------------------------------------------------------------
while(True): # capture frame-by-frame
	ret, frame = cap.read() # Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30) #flags = cv2.CV_HAAR_SCALE_IMAGE
	)
	print("I Can Find {0} faces!".format(len(faces)))
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imshow('frame', frame) 	# Display the resulting frame
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
#-------------------------------------------------------------------------------
cap.release() # When everything done, release the capture
cv2.destroyAllWindows()
