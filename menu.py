import os,time,random,sys,requests
from bin.McybearX import iklan
from bin.toktok import *
m="\x1b[1;91m";h="\x1b[1;92m";k="\x1b[1;93m";b="\x1b[1;94m";u="\x1b[1;95m";l="\x1b[1;96m";p="\x1b[1;97m";emil=print;usup=input;sistem = os.system;mx = u+"ʕ"+m+" x"+u+"_"+m+"×"+u+"ʔ";sup = "\x1b[4;95m               \x1b[0;95m/\x1b[3;91mM\x1b[1;95mcybear\x1b[1;91mX\x1b[0;90m";McybearX = "Usup_Ganteng"
try:
	sistem("mkdir .token")
	sistem("cd .token && touch MbfX MbfiX MddosX MspamX MbotX")
	mbfx=open(".token/MbfX","r").read()
	mbfix=open(".token/MbfiX","r").read()
	mddosx=open(".token/MddosX","r").read()
	mspamx=open(".token/MspamX","r").read()
	mbotx=open(".token/MbotX","r").read()
except KeyError:
	pass
def ting():sistem("play-audio .sound/ting.wav & ")
def animasi(Yusuf):
 for suport in Yusuf + "\n":sys.stdout.write(suport);sys.stdout.flush();time.sleep(1./150)
def logo():
	animasi("""
\x1b[1;91m     __  ___ \x1b[1;95m__                 __     \x1b[1;91m _  __
\x1b[1;91m    /  |/  /\x1b[1;95m/ /_ ____   ____   / /_____\x1b[1;91m| |/ /
\x1b[1;91m   / /|_/ /\x1b[1;95m/ __// __ \ / __ \ / // ___/\x1b[1;91m|   / 
\x1b[1;91m  / /  / /\x1b[1;97m/ /_ / /_/ // /_/ // /(__  )\x1b[1;91m/   |  
\x1b[1;91m /_/  /_/\x1b[1;97m \__/ \____/ \____//_//____/\x1b[1;91m/_/|_|  \x1b[1;97mby \x1b[1;91m𝙼\x1b[1;95m𝚌𝚢𝚋𝚎𝚊𝚛\x1b[1;91m𝚇
""")
def menu():
	sistem("clear")
	logo()
	emil(u+" ["+m+"X"+u+"]"+p+" 𝙰𝚞𝚝𝚑𝚘𝚛  : "+m+"𝙼"+u+"𝚌𝚢𝚋𝚎𝚊𝚛"+m+"𝚇")
	emil(u+" ["+m+"X"+u+"]"+m+" 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 "+p+": 𝙼𝙱𝙴𝚆𝙻𝙴𝙶𝚂")
	emil(u+" ["+m+"X"+u+"]"+p+" 𝚈𝚘𝚞𝚛 𝙸𝙿 :", requests.get("https://api.ipify.org").text)
	emil(sup)
	emil(u+" ["+m+"o1"+u+"]"+p+" Crack FB")
	emil(u+" ["+m+"o2"+u+"]"+p+" Crack IG")
	emil(u+" ["+m+"o3"+u+"]"+p+" DDos Attack")
	emil(u+" ["+m+"o4"+u+"]"+p+" Spam Brutal")
	emil(u+" ["+m+"o5"+u+"]"+p+" BOT Fb/Web")
	emil(u+" ["+m+"o6"+u+"]"+p+" Musik")
	emil(u+" ["+m+"o7"+u+"]"+k+" Tentang Author")
	emil(sup)
	try:
		yakan = int(usup(mx+p+" No : "+m))
	except ValueError:
		emil(mx+m+" Isi Hanya Menggunakan Angka!!!");time.sleep(2)
		menu()
	if yakan==1:
		ting()
		if mbfx==tok1:
			iklan()
			sistem("cd .,/MbfX && python mbfx.py")
		else:
			animasi(u+" ["+m+"!"+u+"]"+m+" Token Invalid")
			iw=usup(mx+p+" Masukan Token : \x1b[0;00m")
			if iw==tok1:
				iklan()
				anj=open(".token/MbfX","w");anj.write(iw);anj.close()
				sistem("cd .,/MbfX && python mbfx.py")
			else:
				animasi(u+" ["+m+"!"+u+"]"+m+" Token Invalid")
				exit()
			exit()
	elif yakan==2:
		ting()
		if mbfix==tok2:
			iklan()
			sistem("cd .,/MbfiX && python mbfix.py")
		else:
			animasi(u+" ["+m+"!"+u+"]"+m+" Token Invalid")
			iw=usup(mx+p+" Masukan Token : \x1b[0;00m")
			if iw==tok2:
				iklan()
				anj=open(".token/MbfiX","w");anj.write(iw);anj.close()
				sistem("cd .,/MbfiX && python mbfix.py")
			else:
				animasi(u+" ["+m+"!"+u+"]"+m+" Token Invalid")
				exit()
			exit()

	elif yakan==3:
		ting()
		if mddosx==tok3:
			iklan()
			sistem("cd .,/MddosX && python mddosx.py")
		else:
			animasi(u+" ["+m+"!"+u+"]"+m+" Token Invalidx")
			iw=usup(mx+p+" Masukan Token : \x1b[0;00m")
			if iw==tok1:
				iklan()
				anj=open(".token/MbfX","w");anj.write(iw);anj.close()
				sistem("cd .,/MbfX && python mbfx.py")
			else:
				animasi(u+" ["+m+"!"+u+"]"+m+" Token Invalid")
				exit()
			exit()

		aw=usup(mx+p+" Run : ")
		sistem("cd .,/MddosX && "+aw)
	elif yakan==4:
		ting()
		if mspamx==tok4:
			iklan()
			sistem("cd .,/MspamX && python mspamx.py")
		else:
			animasi(u+" ["+m+"!"+u+"]"+m+" Token Invalid")
			iw=usup(mx+p+" Masukan Token : \x1b[0;00m")
			if iw==tok4:
				iklan()
				anj=open(".token/MspamX","w");anj.write(iw);anj.close()
				sistem("cd .,/MspamX && python mspamx.py")
			else:
				animasi(u+" ["+m+"!"+u+"]"+m+" Token Invalid")
				exit()
			exit()
	elif yakan==5:
		ting();iklan()
		sistem("cd .,/MbotX && python mbotx.py")
	elif yakan==6:
		ting();iklan()
		emill = usup(mx+p+" Play Musik "+b+"("+k+"y"+b+"/"+m+"g"+b+") : "+p)
		if emill == "y":
			try:
				sistem("mpv .sound/MsoundX.mp3")
			except:
				emil("ah")
		elif emill == "g":
			emil(mx+p+" Jadi Mau Lo Apa Tod?")
			time.sleep(2)
			emil(mx+p+" Dah Dah Balik Ke Menu Aja...");time.sleep(3)
			menu()
		else:
			emil(mx+k+" Input Salah...");time.sleep(2)
			menu()
	elif yakan==7:
		ting()
		iklan()
		Mcybear()
	else:
		emil(mx+p+" Pilihan "+m+yakan+" Gada di Menu Tod")
		time.sleep(3)
		menu()
def Mcybear():
	emil(u+" ["+k+"Info"+u+"]"+p+" Donasi via Wa 🙏")
	emil(u+" ["+m+"o1"+u+"]"+p+" Youtube me")
	emil(u+" ["+m+"o2"+u+"]"+p+" Whatsapp me")
	emil(u+" ["+m+"o3"+u+"]"+p+" Facebook me")
	emil(u+" ["+m+"o4"+u+"]"+p+" Instagram me")
	emil(sup)
	Emil = usup(mx+p+" No : "+m)
	if Emil=="1" or Emil=="01":
		ting()
		sistem("xdg-open https://cararegistrasi.com/VGWDEihZia")
	elif Emil=="2" or Emil=="02":
		ting()
		sistem("xdg-open https://cararegistrasi.com/Abu2QKwEO")
	elif Emil=="3" or Emil=="03":
		ting()
		sistem("xdg-open https://www.facebook.com/usup.mbew.7")
	else:
		emil(mx+p+" Pilihan "+m+Emil+" Input Invalid!!!")
		time.sleep(3)
		Mcybear()

if McybearX == "Usup_Ganteng":
#	sistem("play-audio .sound/MsoundX.mp3 & ")
	sistem("git pull")
	menu()

