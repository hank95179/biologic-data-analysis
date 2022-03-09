
# Python program to demonstrate
# spiral circle drawing
  
  
import turtle
    
t = turtle.Turtle()
  
# taking radius of initial radius
r = 5
  
# Loop for printing spiral circle
for i in range(40):
    t.circle(r + 2*i, 45)