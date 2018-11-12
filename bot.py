from telethon import TelegramClient, sync
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import FloodWaitError
from pprint import pprint
import time
import logging
import random

count = 0
api_id = 371XXX
api_hash = 'e6c796f63b5xxxxxxxxxxxxx'
phone_number = '7925554XXX'

msg = (
    "🚀🚀 Hey, do you want to send messages to multiple Telegram groups automatically? 👈👈\n"
    "🔥🔥 CONTACT ME RIGHT NOW! 💥💥"
)

groupsToJoin = [
    "https://t.me/DISCOVERmarket",
    "https://t.me/MoneyMartOG",
    "https://t.me/instaempiremarket",
    "https://t.me/TMGMarket",
    "https://t.me/buysellplace",
    "https://t.me/windsales",
    "https://t.me/TheFinalMarket",
    "https://t.me/SocialMarket",
    # "https://t.me/joinchat/AAAAAEKdBTcp8PCLxkUdIA",
    "https://t.me/AMmarkets",
    "https://t.me/MediaMarkett",
    "https://t.me/theblackmarket",
    "https://t.me/SocialCapitalmarket",
    "https://t.me/facemarket",
    "https://t.me/E1sales",
    "https://t.me/ExclusiveMarket",
    "https://t.me/beaversmarketplace",
    "https://t.me/projecttgmarket",
    "https://t.me/TheRedMarket",
    "https://t.me/MMMarket",
    "https://t.me/TheDMarket",
    "https://t.me/a1sell",
    "https://t.me/PowerMarketing",
    "https://t.me/surgemarket",
    "https://t.me/TheGalaxyMarket",
    "https://t.me/bluve",
    "https://t.me/sanemarket",
    "https://t.me/PlMPS",
    "https://t.me/BlackMarkets",
    "https://t.me/malcominthemiddle",
    "https://t.me/reconmarket",
    # "https://t.me/joinchat/AAAAAEH9NBde3QGYBge67Q",
    "https://t.me/igbst",
    "https://t.me/instagramventuresmarket",
    "https://t.me/ViralMarket",
    "https://t.me/royalmarkets",
    "https://t.me/themobilemarket",
    # "https://t.me/PlatinumMarket",
    "https://t.me/surgemarket",
    "https://t.me/GodsMarket",
    # "https://t.me/joinchat/BDy9lkL39d-rFIvkXjsEQw",
    "https://t.me/PremiumMarketplace",
    "https://t.me/EvolveMarket",
    "https://t.me/NsmIGGroup",
    "https://t.me/elitemarket",
    # "https://t.me/joinchat/AAAAAD9L4OL0xiEG8SS18w",
    "https://t.me/ThePlugMarket",
    "https://t.me/ThrillsMarket",
    # "https://t.me/joinchat/DsmONUBCjmcRdbhiRrmljw",
    # "https://t.me/joinchat/ELqb70BCcCFrsSjNcpW4cw",
    "https://t.me/almarketgroup",
    "https://t.me/marketinfinity",
    "https://t.me/LucifersMarket"
]

client = TelegramClient(phone_number, api_id, api_hash)
client.start()

def run_till_success(func):
    print("run_till_success")

    def wrapper(*args, **kwargs):
        print("wrapper")
        while True:
            try:
                return func(*args, **kwargs)
            except FloodWaitError as ex:
                print("FloodWaitError, for: " + str(ex.seconds))
                logging.log(logging.INFO, '%s: flood wait' % func.__name__)
                time.sleep(ex.seconds)
            except ValueError:
                print("ValueError")
                logging.log(logging.INFO, '%s: connecting again' %
                            func.__name__)
                client.connect()
            except TimeoutError:
                print("TimeoutError")
                logging.log(logging.INFO, '%s: timeout' % func.__name__)
                time.sleep(2)
                client.connect()
            # except Exception as ex:
            #    logging.log(logging.ERROR, "%s: %s ( %s )" % (func.__name__, type(ex), ex))

    return wrapper

def get_account_groups(getIds=False):
    myGroups = []
    print("Getting my groups\n")
    for dialog in client.get_dialogs():
        if(getIds):
            if (dialog.entity.id).isnumeric():
                myGroups.append(dialog.entity.id)
        else:
            if(str(dialog.entity.username) == dialog.entity.username):
                myGroups.append(dialog.entity.username)

    return myGroups

def clean_groups_list(groups):
    cleanGroups = []

    for i in range(len(groups)):
        groupType = 0
        string = groups[i].split("https://t.me/")[1]

        if "joinchat" in string:
            string = groups[i].split("joinchat/")[1]
            groupType = 1

        cleanGroups.append([string, groupType])

    return cleanGroups

@run_till_success
def join_groups(groups):
    myGroups = get_account_groups()
    groupsToJoin = clean_groups_list(groups)
    foo = 0

    for i in range(len(groupsToJoin)):
        print("Loop: " + str(i))

        if groupsToJoin[i][0] not in myGroups:
            foo = foo + random.randint(3, 10)

            try:
                if groupsToJoin[i][1] == 0:
                    client(JoinChannelRequest(groupsToJoin[i][0]))
                else:
                    client(ImportChatInviteRequest((groupsToJoin[i][0])))
            except Exception as e:
                print(e)

            print("Joining " + groupsToJoin[i][0])

            sleepFor = 10 + foo
            print("Sleep for: " + str(sleepFor) + " seconds\n")
            time.sleep(sleepFor)
        else:
            print("Skipping: " + groupsToJoin[i][0] + "\n")

myGroups = get_account_groups()

while True:
    for i in range(len(myGroups)):
        try:
            print("Loop: " + str(i) + ", group id: " + str(myGroups[i]))
            client.send_message(myGroups[i], msg2)
        except Exception as e:
            print(e)

        if (i + 1) % 30 == 0:
        	print("Sleep for: 60 seconds\n")
        	time.sleep(60)

    count = count + 1
    print("Count: " + str(count))
    print("Sleep for: 600 seconds\n\n")
    time.sleep(600)
