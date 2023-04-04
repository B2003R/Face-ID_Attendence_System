import cv2
import os
import face_recognition
import numpy as np

path = 'faces'
images = []
classname = []
mylist = os.listdir(path)
for cl in mylist:
    curimg = cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classname.append(os.path.splitext(cl)[0])

def findencoding(images):
    encodinglist = []
    for img in images:
        # converting the image to rgb
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodinglist.append(encode)
    return encodinglist

databaseencoding = findencoding(images)

cap = cv2.VideoCapture(0)
i=0
# while(True):
#     i=i+1
#     success, img = cap.read()
#     facelocation = face_recognition.face_locations(img,number_of_times_to_upsample=0,model="hog")
#     # print(facelocation)
#     y1,x2,y2,x1=0,0,0,0
#     if(len(facelocation) == 1):
#         y1,x2,y2,x1 = facelocation[0]
#     cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
#     cv2.imshow('webcam', img)
#     cv2.waitKey(1)

# capturing faces from camera
cap = cv2.VideoCapture(0)
# while(1):
success, img = cap.read()
i = 0
while (i<100):
    i = i+1
    success, img2 = cap.read()
    if(i == 50):
        img = img2
    facelocation = face_recognition.face_locations(img2, number_of_times_to_upsample=0, model="hog")
    # print(facelocation)
    y1, x2, y2, x1 = 0, 0, 0, 0
    if (len(facelocation) == 1):
        y1, x2, y2, x1 = facelocation[0]
    cv2.rectangle(img2, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('webcam', img2)
    cv2.waitKey(1)
# resizing the captured images and converting them to rgb
imgs = cv2.resize(img,(0,0),None,0.25,0.25)
imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
# finding face locations in captured video and encodings
facecurrframe = face_recognition.face_locations(imgs)
encodecurrframe = face_recognition.face_encodings(imgs,facecurrframe)
for encodeface,faceloc in zip(encodecurrframe,facecurrframe):
    matches = face_recognition.compare_faces(databaseencoding,encodeface)
    facedis = face_recognition.face_distance(databaseencoding,encodeface)
    # print(facedis)
    matchindex = np.argmin(facedis)

    if matches[matchindex]:
        name = classname[matchindex].upper()
        print(name)
        # y1,x2,y2,x1 = faceloc
        # y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1 *4
        # cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        # cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        # cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


# cv2.imshow('Webcam',img)
# cv2.waitKey(1)
# cv2.imshow('Webcame',showimg)
