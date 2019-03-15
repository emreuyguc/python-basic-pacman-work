from Tkinter import *
import random

a = 10
b = 10
c = 40
d = 40
start = 385
extent = 300

basla = True

def baslat():
    global a,b,c,d,start,extent,basla
    top = a,b,c,d
    ark = canvas.create_arc(top, start=start, extent=extent, fill="white")
    git()
def git():
    x = random.randint(1,4)
    if x == 1:
        sag()
    elif x==2:
        sol()
    elif x==3:
        yukari()
    elif x==4:
        asagi()
def ciz():
    global a,b,c,d,start,extent
    top = a,b,c,d
    ark = canvas.create_arc(top, start=start, extent=extent, fill="white")
def temizle():
    canvas.delete('all')


def sag():
    global a,b,c,d,start,extent,x,y,basla
    basla = True
    temizle()
    song = random.randint(10,220)
    a = a + 5
    c = c + 5
    temizle()
    ciz()
    if a<song and basla==True:
        canvas.after(150, lambda:sag())
    elif a>220:
        basla = False
        sol()
    elif a>=song:
        basla = False
        git()



def sol():
    global a,b,c,d,start,extent,basla
    basla = True
    temizle()
    song = random.randint(10,220)
    a = a - 5
    c = c - 5
    temizle()
    ciz()
    if a>song and basla==True:
        canvas.after(150, lambda:sol())
    elif a<=5:
        basla = False
        sag()
    elif a<=song:
        basla = False
        git()

def asagi():
    global a,b,c,d,start,extent,basla
    basla = True
    temizle()
    song = random.randint(10,220)
    b = b + 5
    d = d + 5
    temizle()
    ciz()
    if b<song and basla==True:
        canvas.after(150, lambda:asagi())
    elif b>=song:
        basla = False
        yukari()
    elif b<=5:
        basla = False
        git()

        
    

def yukari():
    global a,b,c,d,start,extent,basla
    basla = True
    temizle()
    song = random.randint(10,220)
    b = b - 5
    d = d - 5
    temizle()
    ciz()
    if b>song and basla==True:
        canvas.after(150, lambda:yukari())
    elif b<=5:
        basla = False
        asagi()
    elif b<=song:
        basla = False
        git()

    

tk = Tk()
tk.title("Pacman v2")

buton = Button(tk, text="Başlat", command = baslat)

canvas = Canvas(tk, bd=5, width = 250, height=250, bg="yellow")


buton.pack()


canvas.pack()
mainloop()
