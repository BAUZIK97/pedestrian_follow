import cv2
import numpy as np
import os
import time
import serial
from CServo import CServo
import argparse

# ladowanie klasyfikatorow
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

STM32 = serial.Serial('COM3', 115200, timeout=0.1)
tolerance = 100

# przechwytywanie obrazu
cap = cv2.VideoCapture(0)
loop_counter = 0
servo_x = CServo(1175, tolerance)
servo_y = CServo(1400, tolerance)


def serial_read(stm321):
    data = stm321.readline()
    if data:
        data = data.decode()
        return data


def serial_communication():
    if servo_x.ms < 1000:
        data_x = '0' + str(servo_x.ms)
    if servo_y.ms < 1000:
        data_y = '0' + str(servo_y.ms)
    if servo_y.ms >= 1000 and servo_x.ms >= 1000:
        data_x = str(servo_x.ms)
        data_y = str(servo_y.ms)
        # data_x = '1850'
    data = data_y + data_x
    print(data)
    serial_write(STM32, data)
    print(serial_read(STM32))
    servo_x.ms = servo_x.ms + 50
    servo_y.ms = servo_y.ms + 50


def serial_write(stm321, data):
    stm321.write(str(data).encode())
    time.sleep(1)

# 14501224


def check_boundaries(x1, y1, cen_x, cen_y):
    if x1 > cen_x + tolerance:
        servo_x.sub_ms(2)
    if x1 < cen_x - tolerance:
        servo_x.add_ms(2)
    if y1 > cen_y + tolerance:
        servo_y.sub_ms(1)
    if y1 < cen_y - tolerance:
        servo_y.sub_ms(1)
    if servo_x.ms > 1850:
        servo_x.sub_ms(2)
    if servo_y.ms > 1800:
        servo_y.sub_ms(1)
    if servo_x.ms < 500:
        servo_x.add_ms(2)
    if servo_y.ms < 1000:
        servo_y.add_ms(1)


serial_communication()


while 1:
    ret, img = cap.read()
    # print(img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(img, (320-tolerance, 240-tolerance), (320+tolerance, 240+tolerance), (0, 0, 255), 2)
    # bodies = body_cascade.detectMultiScale(gray_image)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        loop_counter += 1
        if loop_counter == 20:
            check_boundaries((x + w) / 2, (y + h) / 2, img.shape[1], img.shape[0])
            serial_communication()
            loop_counter = 0

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
