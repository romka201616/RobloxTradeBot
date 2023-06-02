import time
import functions
import multiprocessing
import pyautogui
botName = "CubeNinja228"
name = "romka201616"
username = "romka201616"

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
    while True:
        if pyautogui.locateCenterOnScreen(r"D:\pets\arrow2.png") is None:
            break

def giveItemsToUser(name, username):
    petList = functions.getPetsFromDB(botName)
    functions.acceptFriendRequest(username)
    functions.joinServer(
       "https://www.roblox.com/games/6284583030?privateServerLinkCode=29261471894633459457020891970579")
    functions.sendTrade(name, username)
    functions.openChat()
    functions.writeInChat("Your verification code is: b16H7g3D28")
    functions.closeChat()

    functions.chooseItemsForSell(petList)

    functions.openChat()
    functions.writeInChat('Trade is ready. Press "ready" button to continue.')
    functions.closeChat()

    while True:
        if pyautogui.locateCenterOnScreen(r"D:\pets\emptyTrade2.png") is not None:
            break

    functions.finishTrade()
    time.sleep(1)
    functions.saveSuccessfullTrade()
    time.sleep(0.5)
    functions.closeApplication()
    functions.deleteDBRows(botName)
    functions.closeBrowserTab()
    functions.blockUnblock()

def main():
    while True:
        while functions.getPetsFromDB(botName) == ([]):
            functions.getPetsFromDB(botName)
        p = multiprocessing.Process(target=giveItemsToUser, args=(name, username,))
        p.start()
        print("Starting proccess")
        p.join(10 * 60)  # Timer in brackets, minutes multiplied by seconds

        if p.is_alive():
            p.terminate()
            p.join()


if __name__ == '__main__':
    main()


