from cgitb import text
from email.mime import image
from os import popen
from string import hexdigits
import tkinter as tk
from tkinter import ttk
from tkinter import CENTER, Image, Toplevel, font
import random
from tkinter import messagebox
from turtle import color, heading, left, width, window_width
from PIL    import Image
import time
import os
import webbrowser

HEIGHT=800
WIDTH=600

menu=tk.Tk()
menu.title("BilBakalım!")
menu.iconbitmap(bitmap="bbklm.ico")
menu.resizable(width=False, height=False)               #Ölceklendirmeyi kısıtladığım alan.

lowerc=tk.PhotoImage(file="lower.png")
upperc=tk.PhotoImage(file="upper.png")
correctc=tk.PhotoImage(file="correct.png")
num=[0]
zed=[1]

def nasiloynanir():
    global noynanir
    noynanir = Toplevel(menu)

    noynanir.title("Nasıl Oynanır ?")
    noynanir.iconbitmap(bitmap="bbklm.ico")
    noynanir.geometry("800x450")
    noynanir_label=tk.Label(noynanir,image=noynanir_bg)
    noynanir_label.place(x=-1,y=0)
    noynanirtext=tk.Label(noynanir,text="""Oyun 3 seviyeden oluşur. Seviyeye göre algoritma rastsal olarak\nbir sayı belirler ve sizin bu sayıyı tahmin etmenizi sağlar.\nSeviyeler aşağıdaki şekildedir:\n
    1-) Kolay: 0-100 arası tam sayılar.\n
    2-) Orta: 0-1000 arası tam sayılar.\n
    3-) Zor: 0-10000 arası tam sayılar.""",bg="#413F42",font=("Arial TUR",10,font.BOLD),fg="white",justify='left')
    noynanirtext.pack()
    noynanirtext.place(x=25,y=110)
    noynanir.resizable(width=False, height=False)

def hakkimda():
    global hakkimda1
    hakkimda1 = Toplevel(menu)

    hakkimda1.title("Nasıl Oynanır ?")
    hakkimda1.iconbitmap(bitmap="bbklm.ico")
    hakkimda1.geometry("800x450")
    hakkimda1_label=tk.Label(hakkimda1,image=hakkimda_bg)
    hakkimda1_label.place(x=0,y=0)
    hakkt=tk.Label(hakkimda1,text="Murat Serdar GURBETOĞLU",bg="black",font=("Arial TUR",20,font.BOLD),fg="white").place(x=40,y=70)
    hakkt2=tk.Label(hakkimda1,text="Hakkımda detaylı bilgiyi aşağıdaki linklerde bulabilirsiniz.",bg="black",font=("Arial TUR",10,font.BOLD),fg="white",justify="left")
    hakkt2.place(x=42,y=121)
    hakkimda1.resizable(width=False, height=False)
    btn_lnk=tk.Label(image=linkedin)
    linkedin_b = tk.Button(hakkimda1,image=linkedin,command=golink,borderwidth=1)  #Buton Eklemek icin
    linkedin_b.pack(pady=30)
    linkedin_b.place(x=260,y=300,width=60,height=60)
    btn_git=tk.Label(image=github)
    github_b = tk.Button(hakkimda1,image=github,command=gogit,borderwidth=1)  #Buton Eklemek icin
    github_b.pack(pady=30)
    github_b.place(x=100,y=300,width=60,height=60)

def emegigecen():
    global emegigecen1
    emegigecen1 = Toplevel(menu)

    emegigecen1.title("Emeği Geçenler")
    emegigecen1.iconbitmap(bitmap="bbklm.ico")
    emegigecen1.geometry("800x450")
    emegigecen1_label=tk.Label(emegigecen1,image=egecen_bg)
    emegigecen1_label.place(x=0,y=0)
    emektext=tk.Label(emegigecen1,text="Bu programın yapımında youtube üzerinden izlediğim yol gösterici videolar\nçok yardımcı oldu. Görsel dizayn ve methodların işlenmesi hususunda \neğitimlerimi bu videolar ile yaptım. Bununla birlikte google üzerinden \nyaptığım aramalarda git.hub,stackoverflow vb. alanlarında çok yön \ngösterici bilgiler de elde ettim.Ancak asıl perdenin arkasındaki kahramanlar;\nkodlama eğitimine başlamama sebep olandan her konuda soruma anında \ncevap verene, bu yolda bana eşlik edip bildiklerini paylaşanlara, benden \nhaberi bile olmasa yazdığı yazı veya çektiği videolarla bugünlere gelmeme \nilham olan aşağıda belirttiğim kişi ve kurumlardır.",bg="black",font=("Arial TUR",10,font.BOLD),fg="white",justify='left')
    emektext.pack()
    emektext.place(x=25,y=70)
    emektext2=tk.Label(emegigecen1,text="Ümit T..       Turan Burak Y……..       Serdar D…….\n\nCan D….       Selman K….       Anadolu Ü………..\n\nKübra B…..       Emre Ş…..       Patika.dev  ",bg="black",font=("Arial TUR",11,font.BOLD),fg="white")
    emektext2.pack()
    emektext2.place(x=25,y=250)
    emegigecen1.resizable(width=False, height=False)

def deneme():
    level= tk.Label(menu,text="Kolay seviyeyi seçtiniz.. Hadi Başlayalım !")
    level.pack()
    level.place(x=200,y=250)
    x=random.randint(1,100)
    num[0]=x

def deneme2():
    level= tk.Label(menu,text="Orta seviyeyi seçtiniz.. Hadi Başlayalım !")
    level.pack()
    level.place(x=200,y=250)
    x=random.randint(1,1000)
    num[0]=x

def deneme3():
    level= tk.Label(menu,text="Zor seviyeyi seçtiniz.. Hadi Başlayalım !")
    level.pack()
    level.place(x=200,y=250)
    x=random.randint(1,10000)
    num[0]=x

def sorgu1():
    sayac=len(zed)
    tahmin=int(tahmin4.get())
    x=num[0]
    sayac_bg=tk.Frame(menu,bg="darkcyan",bd=5)                             #Buton arka plan icin
    sayac_bg.place(x=360,y=400,width=200,height=40)
    sayac_mt=tk.Label(sayac_bg,text="Deneme Sayısı")
    sayac_mt.pack()
    sayac_mt.place(x=0,y=0,width=150,height=31)
    sayac_cl=tk.Label(sayac_bg,text=sayac)
    sayac_cl.pack()
    sayac_cl.place(x=154,y=0,width=38,height=31)

    if x==0:
        level= tk.Label(menu,text="Lütfen Oyun Seviyesini Seçin",font=("Arial TUR",11,font.BOLD),fg='red',bg="black")
        level.pack()
        level.place(x=200,y=250)

    elif tahmin==x:
        zed.append(1)
        mesaj= tk.Label(menu,text=("Tebrikler doğru tahmin."))
        mesaj.pack()
        mesaj.place(x=150,y=600,width=300,height=50)
        corrects=tk.Label(menu,image=correctc)
        corrects.pack()
        corrects.place(x=120,y=500,width=50,height=50)
        zed.clear()
        zed.append(1)
        num[0]=0

    elif tahmin>x:
        zed.append(1)
        """oldest.append(tahmin)"""
        mesaj= tk.Label(menu,text="Biraz düşür.")
        mesaj.pack()
        mesaj.place(x=250,y=600,width=100,height=50)
        lowers=tk.Label(menu,image=lowerc)
        lowers.pack()
        lowers.place(x=120,y=500,width=50,height=50)
        upperf=tk.Frame(menu,bd=1)
        upperf.place(x=145,y=480,width=50,height=30,anchor=CENTER)
        msg=tk.Label(upperf,text=tahmin)
        msg.pack()
        msg.place()

    elif tahmin<x:
        zed.append(1)
        """oldest.append(tahmin)"""
        mesaj= tk.Label(menu,text="Biraz yükselt.")
        mesaj.pack()
        mesaj.place(x=250,y=600,width=100,height=50)
        uppers=tk.Label(menu,image=upperc)
        uppers.pack()
        uppers.place(x=120,y=500,width=50,height=50)
        lowerf=tk.Frame(menu,bd=1)
        lowerf.place(x=145,y=571,width=50,height=30,anchor=CENTER)
        msg=tk.Label(lowerf,text=tahmin)
        msg.pack()
        msg.place()

def golink():
    webbrowser.open_new_tab("https://www.linkedin.com/in/mserdarg/")

def gogit():
    webbrowser.open_new_tab("https://github.com/MuratSerdarG")

canvas=tk.Canvas(menu, height=HEIGHT,width=WIDTH) # Pencere Boyutu icin
canvas.pack()

backround_image=tk.PhotoImage(file="bbklmback.png")
backround_label=tk.Label(menu,image=backround_image)
backround_label.place(x=0,y=0,relwidth=1,relheight=1)

noynanir_bg=tk.PhotoImage(file="nasiloynanir.png")
hakkimda_bg=tk.PhotoImage(file="hakkimda.png")
egecen_bg=tk.PhotoImage(file="egecen.png")
gonder2=tk.PhotoImage(file='gonder.png')
github=tk.PhotoImage(file='github.png')
linkedin=tk.PhotoImage(file='linkedin.png')

button = tk.Button(menu, text="Kolay",fg='white',bg="darkorchid",font=("Arial TUR",15,font.BOLD),command=deneme,borderwidth=1)  #Buton Eklemek icin
button.place(x=100,y=180,width=100,height=50)

button = tk.Button(menu, text="Orta",fg='white',bg="darkorchid",font=("Arial TUR",15,font.BOLD),command=deneme2,borderwidth=1)  #Buton Eklemek icin
button.place(x=250,y=180,width=100,height=50)

button = tk.Button(menu, text="Zor",fg='white',bg="darkorchid",font=("Arial TUR",15,font.BOLD),command=deneme3,borderwidth=1)  #Buton Eklemek icin
button.place(x=400,y=180,width=100,height=50)

button = tk.Button(menu, text="Nasıl Oynanır ?",bg="black",font=("Arial TUR",10),fg="white",command=nasiloynanir)  #Buton Eklemek icin
button.place(width=175,height=60)
button = tk.Button(menu, text="Hakkımda",bg="black",font=("Arial TUR",10),fg="white",command=hakkimda)  #Buton Eklemek icin
button.place(x=175,width=175,height=60)
button = tk.Button(menu, text="Emeği Geçenler",bg="black",font=("Arial TUR",10),fg="white",command=emegigecen)  #Buton Eklemek icin
button.place(x=350,width=175,height=60)
button = tk.Button(menu, text="Çıkış",bg="black",font=("Arial TUR",10,font.BOLD),fg="red",command=exit)  #Buton Eklemek icin
button.place(x=525,width=80,height=60)

tahmin4=tk.Entry(font=80)
tahmin4.pack()
tahmin4.place(x=200,y=500,width=200,height=50)

btn_lbl=tk.Label(image=gonder2)
gonder = tk.Button(menu,image=gonder2,command=sorgu1,borderwidth=1)  #Buton Eklemek icin
gonder.pack(pady=30)
gonder.place(x=420,y=500,width=160,height=50)

menu.mainloop()