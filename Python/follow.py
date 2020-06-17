import cv2
import serial
from CServo import CServo

# ladowanie klasyfikatorow
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

STM32 = serial.Serial('COM3', 115200)
tolerance = 100
# przechwytywanie obrazu
cap = cv2.VideoCapture(0)
loop_counter = 0
servo_x = CServo(1175, tolerance)
servo_y = CServo(1400, tolerance)
Data_x = str(servo_x.ms)
Data_y = str(servo_y.ms)
Data = Data_y + Data_x


def serial_communication(data_x, data_y):
    if servo_x.ms < 1000:
        data_x = '0' + str(servo_x.ms)
    if servo_y.ms < 1000:
        data_y = '0' + str(servo_y.ms)
    if servo_y.ms > 999 and servo_x.ms > 999:
        data_x = str(servo_x.ms)
        data_y = str(servo_y.ms)
    data = data_y + data_x
    serial_write(STM32, data)


def serial_write(stm321, data):
    stm321.write(str(data).encode())


def check_boundaries(x1, y1, cen_x, cen_y):
    if x1 > cen_x + tolerance:
        servo_x.sub_ms(40)
    if x1 < cen_x - tolerance:
        servo_x.add_ms(40)
    if y1 > cen_y + tolerance:
        servo_y.add_ms(20)
    if y1 < cen_y - tolerance:
        servo_y.sub_ms(20)
    if servo_x.ms > 1850:
        servo_x.ch_ms(1850)
    if servo_y.ms > 1800:
        servo_y.ch_ms(1800)
    if servo_x.ms < 500:
        servo_x.ch_ms(500)
    if servo_y.ms < 1000:
        servo_y.ch_ms(1000)


serial_communication(Data_x, Data_y)


while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_x = int(img.shape[1] / 2)
    img_y = int(img.shape[0] / 2)
    cv2.rectangle(img, (img_x-tolerance, img_y-tolerance),
                  (img_x+tolerance, img_y+tolerance), (0, 0, 255), 2)
    # faces = body_cascade.detectMultiScale(gray_image)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        loop_counter += 1
        if loop_counter == 10:
            check_boundaries((x + w) / 2, (y + h) / 2, img.shape[1], img.shape[0])
            serial_communication(Data_x, Data_y)
            loop_counter = 0

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
