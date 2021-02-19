import cv2
from random import randrange
# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
# img = cv2.imread('rdj.jpg')

webcam = cv2.VideoCapture(0)

# Iterate forever over frames
while True:
    #Read the current frame
    succesful_frame_read, frame = webcam.read()
    
    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
    
    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)
    
    # Stop if Q key is pressed
    if key==81 or key==113:
        break
    

print("Code Completed")