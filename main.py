import time
import functions
import multiprocessing
import pyautogui
botName = "CubeNinja228"
user = "romka201616"

def getItemsFromUser(name, username):
    petList = functions.getPetsFromDB(botName)
    functions.acceptFriendRequest(username)
    #functions.joinServer(
    #    "https://www.roblox.com/games/6516141723?privateServerLinkCode=52365473118566909669998398571053")
    functions.sendTrade(name, username)
    functions.openChat()
    functions.writeInChat("your verification code - b16h73d28")
    functions.closeChat()
    time.sleep(0.5)
    functions.chooseItemsForSell(petList)
    time.sleep(30)
    if functions.checkTrade():
        functions.finishTrade()
        time.sleep(1)
        functions.saveSuccessfullTrade()
        time.sleep(0.5)
        functions.closeApplication()
        functions.deleteDBRows(botName)
    else:
        functions.closeApplication()

def ready():
    start = pyautogui.locateCenterOnScreen(r"D:\pets\arrow.png")
    while start is not None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\arrow.png")

def giveItemsToUser(name, username):
    petList = functions.getPetsFromDB(botName)
    functions.acceptFriendRequest(username)
    # functions.joinServer(
    #    "https://www.roblox.com/games/6516141723?privateServerLinkCode=52365473118566909669998398571053")
    functions.sendTrade(name, username)
    functions.openChat()
    functions.writeInChat("your verification code - b16h73d28")
    functions.closeChat()
    time.sleep(0.5)

    start = None
    while start is None:
        start = pyautogui.locateCenterOnScreen(r"D:\pets\arrow.png")

    checkReady = multiprocessing.Process(target=ready, args=())
    checkReady.start()
    checkItems = multiprocessing.Process(target=functions.chooseItemsForBuy, args=(petList,))
    checkItems.start()

    while True:
        if not checkReady.is_alive():
            checkItems.terminate()
            functions.closeApplication()
            break

        if not checkItems.is_alive():
            checkReady.terminate()
            break

    if checkItems.exitcode == 0:
        functions.finishTrade()
        time.sleep(1)
        functions.saveSuccessfullTrade()
        time.sleep(0.5)
        functions.closeApplication()
        functions.deleteDBRows(botName)
    else:
        functions.closeApplication()

def main():
    p = multiprocessing.Process(target=giveItemsToUser, args=(user,))
    p.start()
    p.join(10 * 60)  # Timer in brackets, minutes multiplied by seconds

    if p.is_alive():
        p.terminate()
        p.join()


if __name__ == '__main__':
    main()


