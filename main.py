import cv2
import numpy as np
import face_recognition
# loading ambani image and converting it to rgb
imgambani = face_recognition.load_image_file('faces/ambani.jpeg')
imgambani = cv2.cvtColor(imgambani,cv2.COLOR_BGR2RGB)
# loading ambani test image and converting it to rgb
imgambanitest = face_recognition.load_image_file('faces/ambanitest.jpeg')
imgambanitest = cv2.cvtColor(imgambanitest,cv2.COLOR_BGR2RGB)
# loadinf tata pic and converting it into rgb
imgtata = face_recognition.load_image_file('faces/ratantata.jpeg')
imgtata = cv2.cvtColor(imgtata,cv2.COLOR_BGR2RGB)
# facelocations
ambanifaceloc = face_recognition.face_locations(imgambani)[0]
ambanitestfaceloc = face_recognition.face_locations(imgambanitest)[0]
tatafaceloc = face_recognition.face_locations(imgtata)[0]
# face encoding
encodeambani = face_recognition.face_encodings(imgambani)[0]
encodeambanitest = face_recognition.face_encodings(imgambanitest)[0]
encodetata = face_recognition.face_encodings(imgtata)[0]
# placing rectangle on facelocation
cv2.rectangle(imgambani,(ambanifaceloc[3],ambanifaceloc[0]),(ambanifaceloc[1],ambanifaceloc[2]),(255,0,255),2)
cv2.rectangle(imgambanitest,(ambanitestfaceloc[3],ambanitestfaceloc[0]),(ambanitestfaceloc[1],ambanitestfaceloc[2]),(255,0,255),2)
cv2.rectangle(imgtata,(tatafaceloc[3],tatafaceloc[0]),(tatafaceloc[1],tatafaceloc[2]),(255,0,255),2)
# comapring faces and face distances
result = face_recognition.compare_faces([encodeambanitest],encodeambani)
dist = face_recognition.face_distance([encodeambanitest],encodeambani)
print(result,dist)
# testing if loaded it correctly
cv2.imshow('ambani',imgambani)
cv2.imshow('ambanitest',imgambanitest)
cv2.imshow('tata',imgtata)
cv2.waitKey(0)