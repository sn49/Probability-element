import json
import os
import hashlib

import reinforce
import inventory

import datetime
import random
import string

import hashlib


hashlib.sha3_256


userdata = {}


money = 50000
gameMoney = 0

randompool = string.ascii_letters + string.digits


def SingUpIn():
    global userdata

    loginID = input("id를 입력하세요.")
    loginPSW = input("password를 입력하세요.")

    if not os.path.isfile("data/alluserinfo.json"):
        SingUp(loginID, loginPSW)
    else:
        with open("data/alluserinfo.json", "r", encoding="UTF-8") as f:
            userdata = json.load(f)

        isRegister = False

        for user in userdata.keys():
            if userdata[user]["loginID"] == loginID:
                with open(f"data/user{user}.json", "r", encoding="UTF-8") as f:
                    userdata = json.load(f)
                    isRegister = True
                    break

        if not isRegister:
            SingUp(loginID, loginPSW)
        else:
            if (
                userdata["loginPSW"]
                == hashlib.sha256((loginPSW + userdata["salt"]).encode()).hexdigest()
            ):
                print("login complete")
            else:
                print("password is wrong")


def SingUp(loginID, loginPSW):
    now = datetime.datetime.now()
    nickname = input("nickname을 입력하세요.")

    userid = f"{random.randint(1000,9999)}{random.randint(1000,9999)}"

    nickCode = ""
    for i in range(5):
        nickCode += random.choice(randompool)
    userdata[userid] = {"loginID": loginID, "nickname": f"{nickname}#{nickCode}"}

    salt = ""
    for i in range(10):
        salt += random.choice(randompool)

    finalPSW = hashlib.sha256((loginPSW + salt).encode()).hexdigest()

    print(finalPSW)

    with open("data/alluserinfo.json", "w", encoding="UTF-8") as f:
        json.dump(userdata, f)

    writeData = {
        "loginPSW": finalPSW,
        "nickname": nickname,
        "nickcode": nickCode,
        "salt": salt,
        "registerdate": f"{now.year}{'%02d'%now.month}{now.day}",
    }

    with open(f"data/user{userid}.json", "w", encoding="UTF-8") as f:
        json.dump(writeData, f)

    writeData = {
        "gold": 100000,
        "moa": 0,
    }

    with open(f"data/finance{userid}.json", "w", encoding="UTF-8") as f:
        json.dump(writeData, f)


def GetMoney():
    mode = input("충전을 하려면 cash를, 노가다를 하려면 daily를 입력하세요.")

    if mode == "cash":
        pass
    elif mode == "daily":
        gameMoney += 1000000


SingUpIn()