import math
import turtle
import random
import time
def multicircle(t,r,time):

    for i in range(time):
        t.circle(r)
        t.lt(360/time)
def Goto(t,x,y):
    t.goto(x,y)
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
def spiarl(t):
    t.pu()
    # Goto(t,r,0)
    r = 5
    for i in range(360*5+1):
        if i == 1:
            t.pd()
        x = r*math.cos(math.radians(i))
        y = r*math.sin(math.radians(i))
        t.pencolor((x+r)/(2*r),(y+r)/(2*r),i/(360*5+1))
        Goto(t,y,x)
        r+=0.05
    t.pu()
def ToyotaLogo(t):
    ellipse(t,100,180,0,0)
    Goto(t,0,0)
    ellipse(t,90,30,0,0)
    Goto(t,70,0)
    ellipse(t,30,110,70,0)
t1 = turtle.Turtle()
t1.pensize(18)
t1.speed(10)
# multicircle(t1,50,40)
# ToyotaLogo(t1)
# pencolor(t1,100)
spiarl(t1)
turtle.exitonclick()