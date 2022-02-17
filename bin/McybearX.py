import os,random,time
#os.system("touch .iklan")
open(".iklan","w").write("?")
iklaninGak=open(".iklan","r").read()
ikan = [ "xdg-open https://cararegistrasi.com/VGWDEihZia", "xdg-open https://mcybearx.bligspot.com", "xdg-open https://youtube.com/c/MBEWLEGS", "xdg-open https://mcybearx.000webhostapp.com" ]
def iklan():
        iklan_gak=[]
        kan = iklan_gak.append(random.choice(['y', 'g']))
        if "y" in iklan_gak:
                os.system(random.choice(ikan))
        elif "g" in iklan_gak:
                pass
if iklaninGak=="?":
	iklan()
