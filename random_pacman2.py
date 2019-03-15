import Tkinter
#from PIL import ImageTk
global x0,x1,y0,y1
import time
import random
pnc = Tkinter.Tk()
x0=50
x1=50
y0=120
y1=120
ss=10
se=350
def ciz():
    global x0,x1,y0,y1,ss,se
    c.delete("all")
    c.create_line(10, 10, 490, 10,fill='green')
    c.create_line(10, 10, 10, 390,fill='green')
    c.create_line(490, 10, 490, 390,fill='green')
    c.create_line(490, 390, 9, 390,fill='green')
    coord = x0,x1,y0,y1
    c.create_arc(coord,start=ss,extent=se,fill="orange")
    
def sola():
    global x0,x1,y0,y1,ss,se
    x0 -= 10
    y0 -= 10
    ciz()
    pnc.update()

def yukariya():
    global x0,x1,y0,y1,ss,se
    x1 -= 10
    y1 -= 10
    ciz()
    pnc.update()
def asagiya():
    global x0,x1,y0,y1,ss,se
    x1 += 10
    y1 += 10
    ciz()
    pnc.update()
def saga():
    global x0,x1,y0,y1,ss,se
    x0 += 10
    y0 += 10
    ciz()
    pnc.update()
    
def oyna(event):
    yns = ["Up","Down","Left","Right"]
    rast = random.choice(yns)
    rastgele()
    """
    tus = event.keysym
    while True:
        if tus=="Left":
            sola()
        elif tus=="Right":
            saga()
        elif tus=="Up":
            yukariya()
        elif tus=="Down":
            asagiya()
        time.sleep(0.10)
        print x0,y0,x1,y1
        kontrol()
    """
def rastgele():
    yns = ["Up","Down","Left","Right"]
    while True:
        rast = random.choice(yns)
        oto(rast)
        
def oto(ben):
    tus = ben
    x=0
    while True:
        if tus=="Left":
            sola()
        elif tus=="Right":
            saga()
        elif tus=="Up":
            yukariya()
        elif tus=="Down":
            asagiya()
        time.sleep(0.10)
        print x0,y0,x1,y1
        kontrol()
        x += 1
        if x >=10:
            x=0
            rastgele()
            
        
def kontrol():
    global x0,x1,y0,y1
    if x0<=10:
        oto("Right")
    elif x0>=420:
        oto("Left")
    elif x1<=10:
        oto("Down")
    elif x1>=320:
        oto("Up")


cizdir = Tkinter.Button(text="basla",command=rastgele)
cizdir.pack()

c = Tkinter.Canvas(pnc,bg="blue",height=400,width=500)
c.pack()


Tkinter.mainloop()
