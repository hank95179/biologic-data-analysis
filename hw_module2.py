import math
import turtle
import random
import time
def RoundCircle(t,time,r):

    for i in range(time):
        t.circle(r)
        t.lt(360/time)
def Goto(t,x,y):
    t.goto(x,y)
def ThreeLeaf(t, l):
    t.pensize(5)
    t.pencolor(0,1,0)
    t.circle(l,120)
    t.lt(120)
    t.circle(l,120)
    t.lt(120)
    t.circle(l,120)
    t.lt(120)
    
def Hexagon(t,l):
    for i in range(6):
        t.fd(l)
        t.lt(120)
        t.fd(l)
        t.lt(120)
        t.fd(l)
        t.lt(60)
def ellipse(t,a,b,shiftx,shifty):
    t.pu()
    Goto(t,a,0+shiftx)
    for i in range(361):
        if i == 1:
            t.pd()
        x = a*math.cos(math.radians(i))
        y = b*math.sin(math.radians(i))
        Goto(t,y+shifty,x+shiftx)
    t.pu()
def pencolor(t,r):
    t.pu()
    Goto(t,r,0)
    for i in range(361):
        if i == 1:
            t.pd()
        x = r*math.cos(math.radians(i))
        y = r*math.sin(math.radians(i))
        t.pencolor((x+r)/(2*r),(y+r)/(2*r),(abs(x*y)/r/r))
        Goto(t,y,x)
    t.pu()
def Spiral(t):
    
    t.pensize(5)
    t.pu()
    # Goto(t,r,0)
    start = 90
    r = 5
    for i in range(360*5+1):
        if i == 1:
            t.pd()
        x = r*math.cos(math.radians(i))
        y = r*math.sin(math.radians(i))
        t.pencolor((x+r)/(2*r),(y+r)/(2*r),i/(360*5+1))
        Goto(t,x,y)
        r+=0.05
    t.pu()
def TaiChi(t1,r):
    t1.fillcolor('black')
    t1.begin_fill()
    t1.circle(r,180)
    t1.lt(180)
    t1.circle(-r/2,180)
    t1.circle(r/2,180)
    t1.end_fill()
    t1.lt(180)
    t1.circle(-r,180)
    t1.pu()
    t1.goto(0,(r*3)/2-(r/10))
    t1.pd()
    t1.begin_fill()
    t1.circle(r/10)
    t1.end_fill()

    t1.fillcolor('white')
    t1.pu()
    t1.goto(0,r/2-(r/10))
    t1.pd()
    t1.begin_fill()
    t1.circle(r/10)
    t1.end_fill()
def ToyotaLogo(t):
    t.pensize(10)
    ellipse(t,100,180,0,0)
    Goto(t,0,0)
    ellipse(t,90,30,0,0)
    Goto(t,70,0)
    ellipse(t,30,110,70,0)
t1 = turtle.Turtle()
t1.speed(10)
Hexagon(t1,100)
time.sleep(1)
t1.reset()
RoundCircle(t1,24,100)
time.sleep(1)
t1.reset()
ThreeLeaf(t1,100)
time.sleep(1)
t1.reset()
TaiChi(t1,180)
time.sleep(1)
t1.reset()
ToyotaLogo(t1)
time.sleep(1)
t1.reset()
Spiral(t1)
turtle.exitonclick()