import cv2
from random import randrange

# loading pre-trained data, front view face
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

# testing video
webcam = cv2.VideoCapture(0)

def blur_background(img):
    face = trained_face_data.detectMultiScale(img)
    
    numFaces = len(face)
    text = str(numFaces) + ' face detected'

    if face != ():
        for (x_face, y_face, w_face, h_face) in face:
            #storing face
            roi_face= img[y_face: y_face+ h_face, x_face: x_face+ w_face]
            img = cv2.blur(img,(20,20))
            img[y_face: y_face+ h_face, x_face: x_face+ w_face]=roi_face
            cv2.rectangle(img, (x_face, y_face), (x_face + w_face, y_face + h_face), (0, 255, 255), 2)

        cv2.putText(img,text,(50,50), font, 1,(0,255,0),2,cv2.LINE_AA)
    else:
        img = cv2.blur(img,(10,10))
        cv2.putText(img,'No face recognized',(50,50), font, 1,(0,0,255),2,cv2.LINE_AA)
    #return image        
    return img

while True:
    succesfull_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('detected image: ', blur_background(frame))

    key = cv2.waitKey(2)

    if key == 81 or key == 113:
        break

"""
# load test image
#image_url = 'image.jpg'
#img =  cv2.imread(image_url)

# show image
#cv2.imshow('colored image: ', img)
#cv2.waitKey()

# converting image to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangle
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(125), randrange(125), randrange(125)), 2)

cv2.imshow('colored image: ', img)
cv2.waitKey()

"""

print("\nCode Completed\n")