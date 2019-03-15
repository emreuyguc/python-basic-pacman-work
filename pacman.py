from Tkinter import *
import tkMessageBox
import random

liste = []

for i in range(2,44):
    z = i * 5
    liste.append(z)
    random.shuffle(liste)
    
a = 10
b = 10
c = 40
d = 40
start = 385
extent = 300

p = random.randint(4,40)
x = liste[p]
h = random.randint(4,40)
y = liste[h]

puan = 0

def baslat():
    yemek()
    puang = str(puan)
    label.config(text="Puanınız : "+puang)
def yemek():
    global x,y
    top2 = x, y, x+30, y+30
    ark2 = canvas.create_arc(top2, start=180, extent=359, fill="black")
    ciz()
def ciz():
    global a,b,c,d,start,extent
    top = a,b,c,d
    ark = canvas.create_arc(top, start=start, extent=extent, fill="white")
def sifirla():
    global a,b,c,d,start,extent,x,y,puan
    canvas.delete('all')
    a = 10
    b = 10
    c = 40
    d = 40
    start = 385
    extent = 300
    puan = 0
    label.config(text="Hoşgeldiniz!")
def temizle():
    canvas.delete('all')
def hata():
    tkMessageBox.showinfo("Game Over!", "Eyvahhh! Çarptın be ya!")
    sifirla()
def sag(event=None):
    global a,b,c,d,start,extent,x,y,liste,puan
    temizle()
    start = start + 270
    a = a + 5
    c = c + 5
    ciz()
    yemek()
    if a>=230:
        hata()
    elif a==x and b==y:
        p = random.randint(1,37)
        x = liste[p-1]
        h = random.randint(1,37)
        y = liste[h-1]
        ciz()
        yemek()
        puan = puan + 7
        puang = str(puan)
        label.config(text="Puanınız : "+puang)
def sol(event=None):
    global a,b,c,d,start,extent,x,y,liste,puan
    temizle()
    start = start - 270
    a = a - 5
    c = c - 5
    ciz()
    yemek()
    if a<=5:
        hata()
    elif a==x and b==y:
        p = random.randint(1,37)
        x = liste[p-1]
        h = random.randint(1,37)
        y = liste[h-1]
        ciz()
        yemek()
        puan = puan + 7
        puang = str(puan)
        label.config(text="Puanınız : "+puang)
def asagi(event=None):
    global a,b,c,d,start,extent,x,y,liste,puan
    temizle()
    start = start + 270
    b = b + 5
    d = d + 5
    ciz()
    yemek()
    if b>=220:
        hata()
    elif a==x and b==y:
        p = random.randint(1,37)
        x = liste[p-1]
        h = random.randint(1,37)
        y = liste[h-1]
        ciz()
        yemek()
        puan = puan + 7
        puang = str(puan)
        label.config(text="Puanınız : "+puang)
def yukari(event=None):
    global a,b,c,d,start,extent,x,y,liste,puan
    temizle()
    start = start - 270
    b = b - 5
    d = d - 5
    ciz()
    yemek()
    if b<=5:
        hata()
    elif a==x and b==y:
        p = random.randint(1,37)
        x = liste[p-1]
        h = random.randint(1,37)
        y = liste[h-1]
        ciz()
        yemek()
        puan = puan + 7
        puang = str(puan)
        label.config(text="Puanınız : "+puang)

tk = Tk()
tk.title("Pacman")

buton = Button(tk, text="Başlat", command = baslat)
buton2 = Button(tk, text="Sıfırla", command = sifirla)

label = Label(tk, text="Hoşgeldiniz!")
label2 = Label(tk, text="Ok tuşları ile oynayabilirsiniz!")
canvas = Canvas(tk, bd=5, width = 250, height=250, bg="yellow")

tk.bind("<Left>", sol)
tk.bind("<Right>", sag)
tk.bind("<Up>", yukari)
tk.bind("<Down>", asagi)

buton.pack()
buton2.pack()
label.pack()
label2.pack()


canvas.pack()
mainloop()
