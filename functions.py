import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pytesseract
from PIL import Image
import os
import pymysql
from config import host, user, password, db_name
import pymysql.cursors
import pyautogui
import time
import pydirectinput
import mouse
import easyocr
import webbrowser

def joinServer(link):
    webbrowser.open(link, new=2)

#Take screanshot and get cliendName
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

#Func for test
def acceptTrade(cliendNameFromDB, cliendName):
    if cliendNameFromDB == cliendName:
        print("Successful :)")
        visitToAccept()
        givePets()
    else:
        print("Scam trade sender >:(")

#Get trade
def getClientName():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        try:
            # select all data from table
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM `users` LIMIT 1")
                # cursor.execute("SELECT * FROM `users`")
                result = cursor.fetchall()
                if result:
                    clientNameDB = result[0]
                    print(f"Client name: {clientNameDB}")
                else:
                    print("No rows found")
                print("#" * 20)

            # delete data
            # with connection.cursor() as cursor:
                delete_query = "DELETE FROM `users` WHERE clientName = clientNameDB"
                cursor.execute(delete_query)
                connection.commit()

        finally:
            connection.close()


    except Exception as ex:
        print("Connection refused...")
        print(ex)
    return clientNameDB['name']

def visitToAccept():
    while True:
        start = pyautogui.locateCenterOnScreen(r'color.png')
        if start is not None:
            time.sleep(0.25)
            pydirectinput.moveTo(start[0], start[1])
            pydirectinput.move(0, 20)
            pydirectinput.click()
            break

def searchItemForSell():
    time.sleep(3)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\pet3.png')
    while start is None:
        pydirectinput.moveTo(900, 500)
        pydirectinput.move(0, 20)
        mouse.wheel(-5)
        start = pyautogui.locateCenterOnScreen(r'D:\pets\pet3.png')
    time.sleep(0.25)
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 20)
    pydirectinput.click()

def openChat():
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r'D:\pets\chat.png')
    time.sleep(0.25)
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def writeInChat(verificationCode):
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r'D:\pets\writeChat.png')
    time.sleep(0.25)
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    pydirectinput.write(verificationCode)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\send.png')
    time.sleep(0.25)
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def closeChat():
    start = pyautogui.locateCenterOnScreen(r'D:\pets\closeChat.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()

def checkTrade():
    emptyTrade = pyautogui.locateCenterOnScreen(r'D:\pets\emptyTrade.png')
    if emptyTrade is None:
        closeApplication()
        return False
    return True

def givePets():
    openChat()
    writeInChat("your verification code - b16h73d28")
    closeChat()
    if checkTrade():
        print("successfull trade")

def sendTrade(name):
    filename = r'D:\pets\name.png'
    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r'D:\pets\cat.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 20)
    pydirectinput.click()
    time.sleep(0.5)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\trade.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 20)
    pydirectinput.click()
    findClient(name, filename)
    time.sleep(1)
    mult = findClient(name, filename)
    print(mult)
    pydirectinput.moveTo(850, 310+100*mult)
    pydirectinput.move(0, 20)
    time.sleep(0.25)
    pydirectinput.click()
    time.sleep(1)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\ok2.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 20)
    pydirectinput.click()

def findClient(name, filename):
    mult = -1
    while mult < 0:
        screen = np.array(ImageGrab.grab(bbox=(700, 290, 1050, 760)))
        cv2.imwrite(filename, screen)
        tmpstr = '#ffffff'
        os.system(rf'convert D:\pets\name.png -fill black +opaque {tmpstr} D:\pets\name2.png')
        img = Image.open(r'D:\pets\name2.png')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(img)
        text = text.split()

        for i in range(len(text)):
            if len(text[i]) < 3:
                text.pop(i)
                break
        for i in range(len(text)):
            if len(text[i]) < 3:
                text.pop(i)
                break
        for i in range(len(text)):
            if len(text[i]) < 3:
                text.pop(i)
                break
        for i in range(len(text)):
            if text[i] == name:
                mult = i
                break

        print(text)
        if mult >= 0:
            return mult
        time.sleep(1)
        pydirectinput.moveTo(850, 310)
        pydirectinput.move(0, 10)
        if (mult // 2) % 2 == 0:
            mouse.wheel(2)
            time.sleep(0.25)
            mouse.wheel(2)
        else:
            mouse.wheel(-2)
            time.sleep(0.25)
            mouse.wheel(-2)
        mult -= 1

def searchItemForSell(petName):
    count = 0
    text = ""
    x, y = 500, 350
    while text != petName:
        count+=1
        pydirectinput.moveTo(x, y)
        pydirectinput.move(0, 10)
        time.sleep(0.25)
        os.chdir(r"C:\Users\miron")
        filename = r'D:\pets\tmp1.png'
        time.sleep(0.1)
        screen = np.array(ImageGrab.grab(bbox=(x+15, y+20, x+250, y+250)))
        cv2.imwrite(filename, screen)
        text = ""
        img2 = Image.open(rf"D:\pets\tmp1.png")
        img2.save(rf"D:\pets\tmp2.png")
        reader = easyocr.Reader(["en"])
        while len(text) < 3:
            img = cv2.imread(rf"D:\pets\tmp2.png")
            text = reader.readtext(img, detail=0)
            while text.count('') != 0:
                text.remove('')
            img2 = img2.crop((0, 0, img2.width//1.2, img2.height//1.2))
            img2.save(rf"D:\pets\tmp2.png")
        text = "\n".join(text)
        print(text)
        x += 100
        if count % 4 == 0:
            x = 500
            y += 100
        if count == 12:
            break

def acceptFriendRequest(username):
    webbrowser.open('https://www.roblox.com/users/friends#!/friend-requests', new=2)
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
                y += 194
            if count == 12:
                x, y = 595, 300
                count = 0
    pydirectinput.moveTo(x+110, y+145)
    pydirectinput.click()
    time.sleep(1)
    closeApplication()

def saveSuccessfullTrade():
    start = pyautogui.locateCenterOnScreen(r'D:\pets\cat.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    time.sleep(0.5)
    start = pyautogui.locateCenterOnScreen(r'D:\pets\trade.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    start = pyautogui.locateCenterOnScreen(r'D:\pets\history.png')
    pydirectinput.moveTo(start[0], start[1])
    pydirectinput.move(0, 10)
    pydirectinput.click()
    pydirectinput.moveTo(800, 360)
    pydirectinput.move(0, 10)
    pydirectinput.click()
    screen = np.array(ImageGrab.grab(bbox=(420, 320, 1500, 800)))
    cv2.imwrite(r'D:\pets\screen.png', screen)

def finishTrade():
    start = pyautogui.locateCenterOnScreen(r'D:\pets\ready.png')
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