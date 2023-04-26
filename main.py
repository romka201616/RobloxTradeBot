import functions
import multiprocessing


def getItemsFromUser(username):
    functions.acceptFriendRequest(username)
    functions.joinServer(
        "https://www.roblox.com/games/6516141723?privateServerLinkCode=52365473118566909669998398571053")
    functions.sendTrade(username)
    functions.givePets()
    functions.openChat()
    functions.writeInChat("your verification code - b16h73d28")
    functions.closeChat()
    functions.searchItemForSell()
    if functions.checkTrade():
        print()
    else:
        return


def main():
    p = multiprocessing.Process(target=getItemsFromUser, args=("Romka201616",))
    p.start()
    p.join(15)  # Timer in brackets

    if p.is_alive():
        p.terminate()
        p.join()


if __name__ == '__main__':
    main()
