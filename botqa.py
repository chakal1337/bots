import sys
import socks
import time
import threading
import string
import random
import ssl
import os
import hashlib

'''
 ravenaq.net
 user: fucme
 hash: 5CD29695E8AF3F9A9696E5BDB2
'''
moveenterspawn="%xt%zm%moveToCell%0%Enter%Spawn%\x00"
retreivedatas="%xt%zm%retrieveUserDatas%0%0%\x00"
retreiveinv="%xt%zm%retrieveInventory%0%0%\x00"
firstjoin="%xt%zm%firstJoin%1%\x00"
gar="%xt%zm%gar%0%0%aa>m:1%wvz%\x00"
gar1="%xt%zm%gar%0%0%aa>m:1%wvz%\x00"
gar2="%xt%zm%gar%0%0%a1>m:1%wvz%\x00"
gar3="%xt%zm%gar%0%0%a2>m:1%wvz%\x00"
gar4="%xt%zm%gar%0%0%a3>m:1%wvz%\x00"
gar5="%xt%zm%gar%0%0%a4>m:1%wvz%\x00"


def goto(who, s):
 goto="%xt%zm%cmd%1%goto%{}%\x00".format(who)
 s.send(goto)
 time.sleep(1)

def tfter(where, s):
 tft="%xt%zm%cmd%1%tfer%{}%{}%\x00".format(sys.argv[3], where)
 s.send(tft)
 time.sleep(1)

def msg(content, s):
 msg="%xt%zm%message%0%{}%zone%\x00".format(content)
 s.send(msg)
 time.sleep(1)

def msgworld(content, s):
 msg="%xt%zm%message%0%{}%world%\x00".format(content)
 s.send(msg)
 time.sleep(1)

def movetocell(cell, pad, s):
 msg="%xt%zm%moveToCell%0%{}%{}%\x00".format(cell, pad)
 s.send(msg)
 time.sleep(1)

def emote(emotetouse, s):
 s.send("%xt%zm%emotea%1%{}%\x00".format(emotetouse))
 time.sleep(1)

def attack(s):
 s.send(gar)
 time.sleep(1)

def attack1(s):
 s.send(gar1)
 time.sleep(1)

def attack2(s):
 s.send(gar2)
 time.sleep(1)

def attack3(s):
 s.send(gar3)
 time.sleep(1)

def attack4(s):
 s.send(gar4)
 time.sleep(1)

def attack5(s):
 s.send(gar4)
 time.sleep(1)


def processcmd(cmd, s):
 if "msgworld:" in cmd:
  msgworld(cmd.split(":")[1], s)
 if "msg:" in cmd:
  msg(cmd.split(":")[1], s)
 if "tfter:" in cmd:
  tfter(cmd.split(":")[1], s)
 if "cell:" in cmd:
  splitten=cmd.split(":")
  cell=splitten[1]
  pad=splitten[2]
  movetocell(cell, pad, s)
 if "goto:" in cmd:
  splitten=cmd.split(":")
  who=splitten[1]
  goto(who, s)
 if "attack" in cmd:
  attack(s)
 if "attack1" in cmd:
  attack1(s)
 if "attack2" in cmd:
  attack2(s)
 if "attack3" in cmd:
  attack3(s)
 if "attack4" in cmd:
  attack4(s)
 if "attack5" in cmd:
  attack5(s)
 if "emote:" in cmd:
  splitten=cmd.split(":")
  which=splitten[1]
  emote(which, s)

def join_flow(s):
 time.sleep(1)
 s.send(retreivedatas)
 print(retreivedatas)
 s.recv(1024)
 time.sleep(1)
 s.send(retreiveinv)
 print(retreiveinv)
 s.recv(1024)
 time.sleep(1)
 s.send(moveenterspawn)
 print(moveenterspawn)
 s.recv(1024)
 while True:
  print("cmds:\ntfter:area\nmsg:message\nmsgworld:message\ncell:cell:pad\nattack1-5\ngoto:player\n")
  print("cmd: ")
  cmd=raw_input()
  try:
   processcmd(cmd, s)
  except Exception as error:
   print(error)


def emu_login(): 
 while True: 
  try:
   s=socks.socksocket()
   s.setproxy(socks.SOCKS5, "127.0.0.1", 9050)
   s.connect((sys.argv[1], int(sys.argv[2])))
   s.recv(1024)
   req = "<msg t=\'sys\'><body action=\'login\' r=\'0\'><login z=\'zone_master\'><nick><![CDATA[N7B5W8W1Y5B1R5VWVZ~{}]]></nick><pword><![CDATA[{}]]></pword></login></body></msg>\x00".format(sys.argv[3], sys.argv[4])
   s.send(req)
   print(req)
   s.recv(1024)
   time.sleep(1)
   s.send(firstjoin)
   print(firstjoin)
   s.recv(1024)
   time.sleep(1)
   join_flow(s)
  except Exception as error: 
   print(error)
   s.close()

if len(sys.argv) < 5:
 print("<ip> <port> <user> <hash>") 
 sys.exit(0)
while True:
 emu_login()

'''
         -> removeItem
         -> doMining
         -> tradeUnlock
         -> house
         -> acceptQuest
         -> getfriendlist
         -> ti
         -> afk
         -> aggroMon
         -> bankToInv
         -> declineFriend
         -> whisper
         -> getDrop
         -> sellItem
         -> tia
         -> restRequest
         -> tid
         -> doFishing
         -> buyItem
         -> guild
         -> buyBagSlots
         -> mute
         -> buyHouseSlots
         -> updateQuest
         -> da
         -> setAchievement
         -> getAdData
         -> tradeDeal
         -> getXmasGift
         -> firstJoin
         -> enhanceItemShop
         -> getQuests
         -> changeArmorColor
         -> gar
         -> cmd
         -> powergem
         -> housesave
         -> tradeFromInv
         -> guildcolor
         -> changeColor
         -> deleteFriend
         -> bankFromInv
         -> cc
         -> gp
         -> loadHairShop
         -> bankSwapInv
         -> PVPQr
         -> genderSwap
         -> loadShop
         -> moveToCell
         -> requestFriend
         -> rebirth
         -> retrieveUserData
         -> buyBankSlots
         -> equipItem
         -> getMapItem
         -> dd
         -> retrieveInventory
         -> loadBank
         -> ia
         -> geia
         -> unequipItem
         -> enhanceItemLocal
         -> tryQuestComplete
         -> duel
         -> serverUseItem
         -> mtcid
         -> restart
         -> loadOffer
         -> emotea
         -> mv
         -> tradeCancel
         -> redeemCode
         -> addFriend
         -> message
         -> retrieveUserDatas
         -> isModerator
         -> tradeToInv
         -> resPlayerTimed
         -> book
         -> tradeLock
         -> em
         -> reloadShop
         -> setHomeTown

'''


