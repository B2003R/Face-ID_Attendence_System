import face_recognition
import numpy
import cv2
import os
import time
from pyzbar.pyzbar import decode

path = 'faces'
images = []
classname = []
mylist = os.listdir(path)
for cl in mylist:
    curimg = cv2.imread(f'{path}/{cl}')
    curimg = cv2.cvtColor(curimg,cv2.COLOR_BGR2RGB)
    images.append(curimg)
    classname.append(os.path.splitext(cl)[0])

known_face_encodings  = []

for img in images:
    currimg_encoding = face_recognition.face_encodings(img)[0]
    known_face_encodings.append(currimg_encoding)

data = {}

i = 0
while(i < len(classname)):
    data[classname[i]] = known_face_encodings[i]
    i = i+1
cap = cv2.VideoCapture(0)

while(True):


    # id = input("Enter the id :")
    # open camera and scanning qr
    print("Please Show you QR CODE")
    id = ''
    while (id == ''):
        suc, qr = cap.read()
        q = decode(qr)
        # cv2.imshow('QR',qr)
        # print(qr)
        cv2.imshow('Webcam',qr)
        cv2.waitKey(1)
        for i in q:
            id = i.data.decode()
    cv2.destroyAllWindows()
    print("Please look into the camera :")
    unknown_face_encoding = []
    while(len(unknown_face_encoding) == 0):
        #showing video and taking 1 pic from the video
        i = 0
        flag = 0
        while(i<100):
            i = i+1
            ran , img = cap.read()
            #resing the img
            imgs  = cv2.resize(img,(0,0),None,0.25,0.25);
            #taking a picture
            if(i == 50):
                img1 = imgs
            facloc = face_recognition.face_locations(imgs)
            # print(facloc," ",len(facloc))
            if(len(facloc) != 0):
                y1,x2,y2,x1 = facloc[0]
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.imshow('webcam', img)
            cv2.waitKey(1)
        # if(len(img1) == 0):
        #     print('Face not matched')
        #     cv2.destroyAllWindows()
        #     continue
        cv2.destroyAllWindows()

        # take a pic
        # success , img = cap.read()
        # resize the pic
        # img = cv2.resize(img,(0,0),None,0.25,0.25)
        # convert to rgb
        img = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        unknown_face_encoding = face_recognition.face_encodings(img)
        if(len(unknown_face_encoding) == 0):
            print('Please try again')
            flag = 1
            break
    if(flag == 1):
        continue
    try:
        matchrate = face_recognition.compare_faces(data[id],unknown_face_encoding)
        facedist = face_recognition.face_distance(data[id],unknown_face_encoding)
    except KeyError:
        print('Invalid ID')
        continue
    if(matchrate[0] == True and facedist < 0.5):
        print('Attendence Marked')
    else:
        print('Face not matched')
    # print(facedist)
    # print(matchrate)