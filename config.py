host = "localhost"
user = "postgres"
password = "1234"
db_name = "online_store"
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pytesseract
from PIL import Image
import os
import pyautogui
import time
import pydirectinput
import easyocr
import webbrowser
import psycopg2
import keyboard
import tensorflow as tf
import keras_ocr

def cropPicture(image):
    # выделяем рамку
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    image, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # находим рамку с наибольшей площадью
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    # вырезаем рамку из изображения
    x, y, w, h = cv2.boundingRect(max_contour)
    frame = image[y:y+h, x:x+w]
    cv2.imwrite('thresh.jpg', frame)

start = None
while start is None:
    start = pyautogui.locateCenterOnScreen(r'D:\pets\changeView.png')
pydirectinput.moveTo(start[0], start[1])
pydirectinput.move(0, 5)
pydirectinput.click()
count = 0
text = ""
x, y = 710, 360
rarityList = [("basic", "dasic"), ("rare", "rahe"), ("epic",), ("legen",), ("myth",), ("secret",), ("excl",),
              ("event", "evemt")]
typeList = [(" ",), ("gold", "geld"), ("dark",), ("rainb", "hainb")]

rarList = ["basic", "rare", "epic", "legendary", "mythical", "secret", "exclusive", "event"]
typList = ["regular", "golden", "dark matter", "rainbow"]

petList = []

while True:
    count += 1
    pydirectinput.moveTo(x, y)
    pydirectinput.move(0, 1)
    os.chdir(r"C:\Users\miron")
    filename = r'D:\pets\tmp1.png'
    time.sleep(0.5)
    screen = np.array(ImageGrab.grab(bbox=(x + 5, y + 5, x + 250, y + 300)))
    img = Image.fromarray(screen)
    img.save('screenshot.png')

    image = cv2.imread('screenshot.png')
    cropPicture(image)
    # Изменённое изображение сохраняется в 'thresh.jpg'

    # Создайте экземпляр пайплайна Keras-OCR
    pipeline = keras_ocr.pipeline.Pipeline()

    # Считайте изображение и преобразуйте его в RGB
    image = keras_ocr.tools.read('thresh.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Примените Keras-OCR
    predictions = pipeline.recognize([image])[0]

    print(f"Detected text: {predictions}")

    x += 60
    if count % 5 == 0:
        x = 710
        y += 60
    if count == 20:
        break
