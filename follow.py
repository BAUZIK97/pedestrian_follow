import cv2
import numpy as np
import os
tolerance = 20
from CServo import CServo
import argparse

# ladowanie klasyfikatorow
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')


# przechwytywanie obrazu
cap = cv2.VideoCapture(0)
loopcounter = 0
servo1 = CServo(1200, 20)
servo2 = CServo(1200, 20)



def check_boundries(x, y, w, h, img, loopcounter):
    loopcounter += 1
    if (x + w)/2 > img.shape[1]/2 - tolerance:
        print('turn_right' + str(loopcounter))
        servo1.add_ms(10)
    if (x + w)/2 < img.shape[1]/2 + tolerance:
        print('turn_left'+ str(loopcounter))
        servo1.add_ms(-10)
    if (y + h)/2 > img.shape[0]/2 - tolerance:
        print('turn_up' + str(loopcounter))
        servo2.add_ms(10)
    if (y + h)/2 < img.shape[0]/2 + tolerance:
        print('turn_down'+ str(loopcounter))
        servo2.add_ms(-10)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # bodies = body_cascade.detectMultiScale(gray_image)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        check_boundries(x, y, w, h, img, loopcounter)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break



cap.release()
cv2.destroyAllWindows()
# out.release()

