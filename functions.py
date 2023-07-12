import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pytesseract
from PIL import Image
import os
from config import host, user, password, db_name
import pyautogui
import time
import pydirectinput
import easyocr
import webbrowser
import psycopg2
import keyboard
import tensorflow as tf
import keras_ocr

def getPetsFromDB(botName):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT pet, rarity, type, amount FROM public.order_list WHERE bot = %s""",
                (botName,)
            )
            result = cursor.fetchall()
            print(f"Result: {result}")
            return result

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

def deleteDBRows(botName):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """DELETE FROM public.order_list WHERE bot = %s""",
                (botName,)
            )

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

def joinServer(link):
    webbrowser.open(link, new=2)

def blockUnblock():
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\3dots.png")
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 5)
    pydirectinput.click()
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\blockUser.png")
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(10, 0)
    pydirectinput.click()
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\block.png")
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(10, 0)
    pydirectinput.click()
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\3dots.png")
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 5)
    pydirectinput.click()
    time.sleep(2)
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\unblockUser.png")
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 5)
    pydirectinput.click()
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\unblock.png")
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 5)
    pydirectinput.click()


def getTradeSenderName():
    os.chdir(r"C:\Users\billy")

    time.sleep(2)
    filename = r'C:\Users\billy\PycharmProjects\pythonProject\Image.png'
    screen2 = np.array(ImageGrab.grab(bbox=(950, 430, 1050, 500)))
    screen = np.array(ImageGrab.grab(bbox=(643, 370, 1264, 625)))
    cv2.imwrite(filename, screen2)

    mainColors = []
    img = Image.open(filename)
    colors = img.getcolors(1024)  # put a higher value if there are many colors in your image
    for c in colors:
        if c[0] > 1000:
            mainColors.append(c[1])

    mainColors = list(mainColors)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum1 += int(mainColors[0][0]) + int(mainColors[0][1]) + int(mainColors[0][2])
    sum2 += int(mainColors[1][0]) + int(mainColors[1][1]) + int(mainColors[1][2])
    sum3 += int(mainColors[2][0]) + int(mainColors[2][1]) + int(mainColors[2][2])

    exactColor = mainColors[0]

    if max(sum1, sum2, sum3) != sum2 and min(sum1, sum2, sum3) != sum2:
        exactColor = mainColors[1]
    elif max(sum1, sum2, sum3) != sum3 and min(sum1, sum2, sum3) != sum3:
        exactColor = mainColors[2]

    tmpstr = ('#%02x%02x%02x' % exactColor)
    cv2.imwrite(filename, screen)
    try:
        os.system(rf'convert C:\Users\billy\PycharmProjects\pythonProject\Image.png -fill black +opaque {tmpstr} C:\Users\billy\PycharmProjects\pythonProject\onlyTime.png')
    except:
        print("cmd error")
    img = Image.open(r'C:\Users\billy\PycharmProjects\pythonProject\onlyTime.png')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img)
    clientName = text[0: text.find(" ")]
    print(clientName)

    return clientName

def visitToAccept():
    while True:
        start = pyautogui.locateCenterOnScreen(r'color.png')
        if start is not None:
            time.sleep(0.25)
            pydirectinput.moveTo(start[0], start[1])
            pydirectinput.move(0, 20)
            pydirectinput.click()
            break

def openChat():
    start = None
    while True:
        if pyautogui.locateCenterOnScreen(r'D:\pets\chat2.png') != None:
            start = pyautogui.locateCenterOnScreen(r'D:\pets\chat2.png')
            break
        if pyautogui.locateCenterOnScreen(r'D:\pets\chat.png') != None:
            start = pyautogui.locateCenterOnScreen(r'D:\pets\chat.png')
            break
    time.sleep(0.25)
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def writeInChat(verificationCode):
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r'D:\pets\writeChat2.png')
    time.sleep(0.25)
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    keyboard.write(verificationCode)
    time.sleep(0.25)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\send2.png')
    time.sleep(0.25)
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def closeChat():
    start = pyautogui.locateCenterOnScreen(r'D:\pets\closeChat2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def checkTrade():
    emptyTrade2 = pyautogui.locateCenterOnScreen(r'D:\pets\emptyTrade2.png')
    if emptyTrade2 is None:
        closeApplication()
        return False
    return True

def sendTrade(name, atName):
    filename = r'D:\pets\name.png'
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r'D:\pets\cat2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    time.sleep(0.5)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\trade2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    pydirectinput.moveTo(750, 710)
    pydirectinput.move(0, 10)
    pydirectinput.click()
    keyboard.write(atName)
    time.sleep(1)
    text = ['']
    while text[0] != name and text[0].replace("?", "2") != name:
        screen = np.array(ImageGrab.grab(bbox=(440, 320, 710, 380)))
        cv2.imwrite(filename, screen)
        tmpstr = '#ffffff'
        os.system(rf'convert D:\pets\name.png -fill black +opaque {tmpstr} D:\pets\name2.png')
        img = cv2.imread(r'D:\pets\name2.png')
        reader = easyocr.Reader(["en"])
        text = reader.readtext(img, detail=0)
        if text == []:
            text = ['']

    time.sleep(30)
    while text[0] != name and text[0].replace("?", "2") != name:
        screen = np.array(ImageGrab.grab(bbox=(440, 320, 710, 380)))
        cv2.imwrite(filename, screen)
        tmpstr = '#ffffff'
        os.system(rf'convert D:\pets\name.png -fill black +opaque {tmpstr} D:\pets\name2.png')
        img = cv2.imread(r'D:\pets\name2.png')
        reader = easyocr.Reader(["en"])
        text = reader.readtext(img, detail=0)
    pydirectinput.moveTo(500, 350)
    pydirectinput.move(0, 10)
    pydirectinput.click()
    time.sleep(1)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\ok4.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def cropPicture(image):
    # выделяем рамку
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

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

def chooseItemsForBuy():
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
        screen = np.array(ImageGrab.grab(bbox=(x+5, y+5, x + 250, y + 300)))
        img = Image.fromarray(screen)
        img.save('screenshot.png')

        image = cv2.imread('screenshot.png')
        cropPicture(image)
        # Изменённое изображение сохраняется в 'thresh.jpg'

        # Получите список всех файлов в папке "train"
        files = os.listdir('thresh.jpg')

        # Создайте экземпляр пайплайна Keras-OCR
        pipeline = keras_ocr.pipeline.Pipeline()

        # Считайте изображение и преобразуйте его в RGB
        image = keras_ocr.tools.read('thresh.jpg')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Примените Keras-OCR
        predictions = pipeline.recognize([image])[0]

        # Выведите результат для каждого изображения
        text, box = predictions
        print(f"Detected text: {text}")

        tmpIndex = -1
        petRarity = ''
        petType = ''
        stop = False

        for rarindex, rarity in enumerate(rarityList):
            for rar in rarity:
                if text.find(rar) != -1:
                    tmpIndex = text.find(rar)
                    petRarity = rarList[rarindex]
                    temp = False
                    for typindex, type in enumerate(typeList):
                        for typ in type:
                            if text.find(typ) != -1:
                                petType = typList[typindex]
                                if temp:
                                    stop = True
                                    break
                                temp = True
                        if stop:
                            break
                if stop:
                    break
            if stop:
                break



        name = text[:tmpIndex]
        last_space_index = name.rfind(' ')  # ищем индекс последнего пробела
        if last_space_index != -1:  # если пробел найден
            second_last_space_index = name.rfind(' ', 0, last_space_index)  # ищем индекс второго пробела с конца
            if second_last_space_index != -1:  # если второй пробел найден
                name = name[:second_last_space_index]

        petList.append((name, petRarity, petType))
        print(petList)

        x += 60
        if count % 5 == 0:
            x = 710
            y += 60
        if count == 20:
            break
    return petList

chooseItemsForBuy()

def chooseItemsForSell(petList):
    text = ""
    rarityList = [("basic", "dasic"), ("rare", "rahe"), ("epic",), ("legen",), ("myth",), ("secret",), ("excl",),
                  ("event", "evemt")]
    typeList = [(" ",), ("gold", "geld"), ("dark",), ("rainb", "hainb")]
    while len(petList) != 0:
        for pet in petList:
            pydirectinput.moveTo(400, 750)
            pydirectinput.move(0,10)
            pydirectinput.click()
            keyboard.write(pet[0])
            amount = int(pet[3])
            x, y = 300, 380
            count = 0
            while amount != 0:
                pydirectinput.moveTo(x, y)
                pydirectinput.move(0, 10)
                time.sleep(0.25)
                os.chdir(r"C:\Users\miron")
                filename = r'D:\pets\tmp1.png'
                time.sleep(0.1)
                screen = np.array(ImageGrab.grab(bbox=(x + 15, y + 20, x + 250, y + 250)))
                # Ищем индексы пикселей с нужным цветом
                indices = np.where(np.all(screen == [59, 177, 252], axis=-1))

                # Находим координаты самого верхнего левого и правого нижнего пикселя
                min_x, min_y = np.min(indices, axis=1)
                max_x, max_y = np.max(indices, axis=1)

                # Обрезаем скриншот по найденным координатам
                cropped_screen = screen[min_y:max_y + 1, min_x:max_x + 1]
                cv2.imwrite(filename, cropped_screen)
                text = ""
                img2 = Image.open(rf"D:\pets\tmp1.png")
                img2.save(rf"D:\pets\tmp2.png")
                reader = easyocr.Reader(["en"])
                while len(text) < 3:
                    img = cv2.imread(rf"D:\pets\tmp2.png")
                    text = reader.readtext(img, detail=0)
                    while text.count('') != 0:
                        text.remove('')
                    img2 = img2.crop((0, 0, img2.width // 1.2, img2.height // 1.2))
                    img2.save(rf"D:\pets\tmp2.png")
                text = ("\n".join(text)).lower()
                print(text)
                if text.replace("\n", " ").find(pet[0].replace("B", "D").lower()) != -1 or text.replace("\n", " ").find(
                        pet[0].lower()) != -1:
                    for rar in rarityList[int(pet[1]) - 1]:
                        if text.replace("\n", " ").replace(pet[0].replace("B", "D").lower(), "").find(
                                rar) != -1 or text.replace("\n", " ").replace(pet[0].lower(), "").find(rar) != -1:
                            for typ in typeList[int(pet[2]) - 1]:
                                if text.replace("\n", " ").replace(pet[0].replace("B", "D").lower(), "").find(
                                        typ) != -1 or text.replace("\n", " ").replace(pet[0].lower(), "").find(
                                    typ) != -1:
                                    print("Found")
                                    pydirectinput.move(0,10)
                                    pydirectinput.click()
                                    amount -= 1
                                    deleted = True
                                    break
                            if deleted:
                                break
                count += 1
                x += 100
                if count % 3 == 0:
                    x = 300
                    y += 100
                if count == 12:
                    break

            petList.remove(pet)

    return len(petList) == 0

def acceptFriendRequest(username):
    webbrowser.open('https://www.roblox.com/users/friends#!/friend-requests', new=2)
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\ignoreAccept.png")
    count = 0
    text = ""
    username2 = username.replace("l", "I").lower()
    username3 = username.replace("B", "D").lower()
    username4 = username.replace("0", "o").lower()
    username = username.lower()
    time.sleep(5)
    x, y = 225, 320
    while True:
        count += 1
        time.sleep(0.25)
        filename = r'D:\pets\tmp1.png'
        time.sleep(0.1)
        screen = np.array(ImageGrab.grab(bbox=(x, y, x + 215, y + 80)))
        cv2.imwrite(filename, screen)
        text = ""
        img2 = Image.open(rf"D:\pets\tmp1.png")
        img2.save(rf"D:\pets\tmp2.png")
        img = cv2.imread(rf"D:\pets\tmp2.png")
        reader = easyocr.Reader(["en"])
        text = reader.readtext(img, detail=0)
        text = text[1].replace("@", "").lower()

        if text == username or text == username2 or text == username3 or text == username4:
            break

        x += 323
        if count % 3 == 0:
            x = 200
            y += 194
        if count == 12:
            x, y = 595, 300
            count = 0

    pydirectinput.moveTo(x+80, y+15)
    pydirectinput.click()
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\acceptFriend.png")
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def saveSuccessfullTrade():
    start = pyautogui.locateCenterOnScreen(r'D:\pets\cat2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    time.sleep(0.5)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\trade2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    start = pyautogui.locateCenterOnScreen(r'D:\pets\history2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    pydirectinput.moveTo(800, 360)
    pydirectinput.move(0, 10)
    pydirectinput.click()
    screen = np.array(ImageGrab.grab(bbox=(250, 320, 1050, 700)))
    cv2.imwrite(r'D:\pets\screen2.png', screen)

def finishTrade():
    start = pyautogui.locateCenterOnScreen(r'D:\pets\ready2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    time.sleep(0.5)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\yes2.png')
    if start is not None:
        pydirectinput.moveTo(start[0], start[1])
        pydirectinput.move(0, 10)
        pydirectinput.click()
        time.sleep(0.5)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\confirm2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    time.sleep(0.5)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\yes2.png')
    if start is not None:
        pydirectinput.moveTo(start[0], start[1])
        pydirectinput.move(0, 10)
        pydirectinput.click()
        time.sleep(0.5)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\ok5.png')
    while start is None:
        start = pyautogui.locateCenterOnScreen(r'D:\pets\ok5.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def removeFriend(username):
    webbrowser.open(r'https://www.roblox.com/users/friends#!/friends', new=2)
    time.sleep(3)
    count = 0
    text = ""
    username2 = username.replace("l", "I").lower()
    username3 = username.replace("B", "D").lower()
    username = username.lower()
    x, y = 595, 300
    while text != username and text != username2 and text != username3:
        count += 1
        time.sleep(0.25)
        os.chdir(r"C:\Users\miron")
        filename = r'D:\pets\tmp1.png'
        time.sleep(0.1)
        screen = np.array(ImageGrab.grab(bbox=(x + 15, y + 20, x + 210, y + 200)))
        cv2.imwrite(filename, screen)
        text = ""
        img2 = Image.open(rf"D:\pets\tmp1.png")
        img2.save(rf"D:\pets\tmp2.png")
        img = cv2.imread(rf"D:\pets\tmp2.png")
        reader = easyocr.Reader(["en"])
        text = reader.readtext(img, detail=0)
        text = text[1].replace("@", "").lower()
        print(text)
        if text != username and text != username2 and text != username3:
            x += 323
            if count % 3 == 0:
                x = 595
                y += 138
            if count == 12:
                x, y = 595, 300
                count = 0
    pydirectinput.moveTo(x + 110, y + 145)
    pydirectinput.click()

def closeApplication():
    pyautogui.hotkey("altleft", "f4")

def closeBrowserTab():
    pyautogui.hotkey("ctrlleft", "w")