import cv2
import os
from os import listdir
import numpy as np
import time
from train import face_recognizer

face_classifier = cv2.CascadeClassifier('C:/Users/Lenovo/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def load_image():
    path = 'D:/final_prediction_dataset'
    if os.path.isdir(path):
        print('database_folder already there')
    else:
        os.mkdir(path)
    cam = cv2.VideoCapture(0)  # for default camera
    count = 0
    while True:

            ret, frame = cam.read()

            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #face_classifier = cv2.CascadeClassifier('C:/Users/Lenovo/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
            faces = face_classifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                count += 1

                file_name_path = 'D:/final_prediction_dataset/test '  + '.jpg'
                cv2.imshow('Face Cropper', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

                cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imwrite(file_name_path, frame)
            k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video# do take care of scope of k error i was doing
            if k == 27:
                break
            elif count >= 1:  # Take 30 face sample and stop video
                break


            cam.release()
            cv2.destroyAllWindows()

def detect_face(img):
        face_classifier = cv2.CascadeClassifier('C:/Users/Lenovo/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
        # convert the test image to gray image as opencv face detector expects gray images

        #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #gray = np.array(img,dtype= 'uint8')
        faces = face_classifier.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5);

        # if no faces are detected then return original img
        if (len(faces) == 0):
            return None, None

        # under the assumption that there will be only one face,
        # extract the face area
        (x, y, w, h) = faces[0]

        # return only the face part of the image
        return gray[y:y + w, x:x + h], faces[0]

def draw_rectangle(img, rect):
        (x, y, w, h) = rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # function to draw text on give image starting from
    # passed (x, y) coordinates.
def draw_text(img, text, x, y):
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


def predict(test_img):

    # detect face from the image
    #face, rect = detect_face(test_img)

    # predict the image using our face recognizer
    label, confidence = face_recognizer.predict(test_img)
    # get name of respective label returned by face recognizer
    label_text = str(label)

    # draw a rectangle around face detected
    draw_rectangle(img, rect)
    # draw name of predicted person
    draw_text(img, label_text, rect[0], rect[1] - 5)

    return img



load_image()  #loading the image and saving it in a camera
test_img1 = cv2.imread("D://final_prediction_dataset//test.jpg",cv2.IMREAD_GRAYSCALE)


predicted_img1 = predict(test_img1)



cv2.imshow('predicting...', predicted_img1)
print("Prediction complete")

cv2.destroyAllWindows()

