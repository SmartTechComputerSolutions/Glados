import cv2
#https://github.com/opencv/opencv/tree/master/data/haarcascades
print("starting Facial Recognition")

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

img = cv2.imread('face.jpg')

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

print(face_coordinates)

cv2.rectangle(img, () , (0, 255, 0), 2)

cv2.imshow('face detector', grayscaled_img)
cv2.waitKey()



print("facial recognition ended")