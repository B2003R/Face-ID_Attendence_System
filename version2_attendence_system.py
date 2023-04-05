import face_recognition
import numpy
import cv2
import os
import time

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
    id = input("Enter the id :")
    print("Please look into the camera :")
    unknown_face_encoding = []
    while(len(unknown_face_encoding) == 0):
        # take a pic
        success , img = cap.read()
        # resize the pic
        img = cv2.resize(img,(0,0),None,0.25,0.25)
        # convert to rgb
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        unknown_face_encoding = face_recognition.face_encodings(img)
    try:
        matchrate = face_recognition.compare_faces(data[id],unknown_face_encoding)
    except KeyError:
        print('Invalid ID')
        continue
    # fing encodings
    # try:
    #     unknown_face_encoding = face_recognition.face_encodings(img)[0]
    #     matchrate = face_recognition.compare_faces(data[id],unknown_face_encoding)
    # except KeyError:
    #     print('Invalid Id')
    #     continue
    # except IndexError:
    #     i =0
    #     flag = 0
    #     while(i<100):
    #         i = i+1
    #         s,img = cap.read()
    #         if(i==50):
    #             print("Please wait")
    #         unknown_face_encoding = face_recognition.face_encodings(img)
    #         # print(len(unknown_face_encoding))
    #         if(len(unknown_face_encoding) == 1):
    #             try:
    #                 matchrate = face_recognition.compare_faces(data[id], unknown_face_encoding)
    #             except KeyError:
    #                 print('Invalid id')
    #                 break
    #             # print("Face Recognition SuccessFull")
    #             # print(matchrate)
    #             flag = 1
    #             break
    #     if(flag == 0):
    #         print("Face Recognition Failed")
    #         continue
    # print(type(matchrate))
    if(matchrate[0] == True):
        print('Attendence Marked')
    else:
        print('Face not matched')