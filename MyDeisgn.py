import turtle
bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)
from MyFunctionl import*

#sky-background
turtle.bgcolor(3,1,22) #sky
from random import*    #use random function and jump to creat the stars 
for times in range(150):
    x=randint(-800,800)
    y=randint(-800,800)
    c=(248,249,202)
    jump(bob,x,y)
    bob.begin_fill() 
    bob.color(c)
    bob.circle(1)
    bob.end_fill
    
home(bob)
#color of the petal
c1=(0,233,255)
c2=(252,0,75)
c3=(167,82,255)

#bring in the layer
petalAB(bob,c1)
petalC(bob,c1,c2)
petalD(bob,c1,c2,c3)

#center
for times in range(360):
    c=(242,255,7)
    bob.color(c)
    bob.forward(15)
    home(bob)
    bob.left(times+2)
home(bob)

#spiral of the corner
jump(bob,-500,300)
for times in range(255):
    c=(0,times,times)
    bob.color(c)
    bob.forward(times/2)
    bob.left(75)

jump(bob,500,-300)
for times in range(255):
    c=(0,times,times)
    bob.color(c)
    bob.forward(times/2)
    bob.left(75)

jump(bob,500,300)
for times in range(255):
    c=(255,255,255-times)
    bob.color(c)
    bob.circle(times/4)
    bob.left(45)
    
jump(bob,-500,-300)

for times in range(255):
    c=(255,255,255-times)
    bob.color(c)
    bob.circle(times/4)
    bob.left(45)
bob.bgcolor(0,0,0)

bob.done()
