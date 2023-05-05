import time
import functions
import multiprocessing

botName = "CubeNinja228"

def getItemsFromUser(username):
    petList = functions.getPetsFromDB(botName)
    functions.acceptFriendRequest(username)
    functions.joinServer(
        "https://www.roblox.com/games/6516141723?privateServerLinkCode=52365473118566909669998398571053")
    functions.sendTrade(username)
    functions.givePets()
    functions.openChat()
    functions.writeInChat("your verification code - b16h73d28")
    functions.closeChat()
    functions.chooseItemsForSell(petList)
    time.sleep(1)
    if functions.checkTrade():
        functions.finishTrade()
        time.sleep(4)
        functions.closeApplication()
        time.sleep(0.5)
        functions.removeFriend(username)
        return True
    else:
        functions.closeApplication()
        return False


def main():
    p = multiprocessing.Process(target=getItemsFromUser, args=("Romka201616",))
    p.start()
    p.join(10 * 60)  # Timer in brackets, minutes multiplied by seconds

    if p.is_alive():
        p.terminate()
        p.join()


if __name__ == '__main__':
    main()


