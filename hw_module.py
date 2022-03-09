import math
import turtle
import random
import time
# import hw_function
def draw(t1,length,rotation):
    t1.pencolor('red')
    for i in range(4):
        t1.fd(length)
        t1.lt(rotation)
def Polygon(t1,n,l):
    d = 360 / n
    n//=2
    for i in range(n):
        t1.fd(l)
        t1.lt(d)
def ConPolygon(t1,n,l):
    d = 360 / n
    n//=2
    for i in range(n):
        t1.fd(l)
        t1.rt(d)
def Circle(t,r):
    n = 360
    d = 180/n
    l = r*math.sin(math.radians(180/n))*2
    Polygon(t,n,l)
def ConCircle(t,r):
    n = 36
    d = 180/n
    l = r*math.sin(math.radians(180/n))*2
    ConPolygon(t,n,l)
def CCircle(t,r):
    t.pu()
    t.goto(0,-r)
    t.pd()
    t.circle(r)
    t.pu()
    t.goto(0,0)
    t.pd()
def StarOdd(t,n,r):
    theta = 360/n
    theta/=2
    for i in range(n):
        t.fd(r)
        t.rt(180-theta)
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
def Spiral(t):
    move = 5
    for i in range(42):
        t.pencolor(random.random(),random.random(),random.random())
        t.circle(2*i+move,45)

def ellipse(t1,rad,seth,sharp):
    t1.seth(seth)
    for i in range(2):
        t1.circle(rad,90)
        t1.circle(rad//sharp,90)


def ToyotaLogo(t,r):
    ellipse(t,r,-45,3)
    t.pu()
    t.goto(r/1.3,-r/3.8)
    t.pd()
    ellipse(t,r/1.4,45,10)
    t.pu()
    t.goto(r/8,r/2.5)
    t.pd()
    ellipse(t,r/1.2,-45,10)
def SineWave(t,s,e,a):
    t.pu()
    for angle in range(s,e):
        y = math.sin(math.radians(angle))
        t.goto(angle,y*a)  
        t.pd()

t1 = turtle.Turtle()
# t1.speed(10)
StarOdd(t1,5,300)
time.sleep(1)
t1.reset()
TaiChi(t1,180)
time.sleep(1)
t1.reset()
SineWave(t1,-360,360,180)
time.sleep(1)
t1.reset()
Spiral(t1)
time.sleep(1)
t1.reset()
ToyotaLogo(t1,300)
turtle.exitonclick()