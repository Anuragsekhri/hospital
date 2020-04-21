import cv2
import os
from os import listdir
import numpy as np
import time
import importlib




print('enter your id')
id = input()

def collect_data():
    face_classifier = cv2.CascadeClassifier('C:/Users/Lenovo/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

    print('hello' + '  ' + id)
    #rndm = int(round(time.time() * 1000))
    
    while True:

        subpath = 'D:/final_creation_dataset/user ' + str(rndm)
        if os.path.isdir(subpath):
            # it will check whether a file or folder exits at that path

            print('directory already there and saving images on it')

            ret, frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                count += 1

                file_name_path = 'D:/final_creation_dataset/user ' + str(rndm) + '/' + str(count) + '.jpg'
                cv2.imshow('Face Cropper', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

                cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imwrite(file_name_path, gray[y:y+h,x:x+w])
            k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video# do take care of scope of k error i was doing
            if k == 27:
                break
                cam.release()
            elif count >= 30:  # Take 30 face sample and stop video
                break
                cam.release()


        else:
            os.mkdir(subpath)
            ret, frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                count += 1

                file_name_path = 'D:/final_creation_dataset/user ' + str(rndm) + '/' + str(count) + '.jpg'
                cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imwrite(file_name_path, gray[y:y+h,x:x+w])


                cv2.imshow('Face Cropper', frame)

            k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break
                cam.release()
            elif count > 30:  # Take 30 face sample and stop video
                break
                cam.release()
collect_data()# calling the  function
print('Colleting Samples Complete!!!')

cv2.destroyAllWindows()

#here one thing to do mark the rndm no(date-time)  with  patient name.
#also look for how to pass.
#os.system('C:/Users/Lenovo/PycharmProjects/hospital/venv/Scripts/entepatientdata.py')
