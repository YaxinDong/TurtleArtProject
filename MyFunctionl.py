#myFunction

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def home(t):
    t.penup()
    t.home()
    t.pendown()

def petalAB(t,c1):
    t.color(c1)
    for times in range(6):
        t.right(times*60)
        for times in range(122):
            t.forward(2)
            t.left(1)
        home(t)
    for times in range(6):
        t.left(times*60)
        for times in range(122):
            t.forward(2)
            t.right(1)
        home(t)

def petalC(t,c1,c2):
    for times in range(6):
        t.pencolor(c1)
        t.right(times*60)
        for times in range(110):
            t.forward(2)
            t.left(1)
        t.pencolor(c2)
        t.right(135)
        for times in range(9):
            t.forward(8)
            t.left(3)
        for times in range(5):
            t.forward(10)
            t.left(2)
        t.right(135)
        for times in range(6):
            t.forward(10)
            t.left(2)
        for times in range(10):
            t.forward(8)
            t.left(3)
        home(t)

def petalD(t,c1,c2,c3):
    for times in range(6):
        t.pencolor(c1)
        t.right(times*60)
        for times in range(110):
            t.forward(2)
            t.left(1)
        t.pencolor(c2)
        t.right(135)
        for times in range(9):
            t.forward(8)
            t.left(3)
        for times in range(1):
            t.forward(5)
            t.left(1)
        t.left(90)
        t.pencolor(c3)
        t.forward(170)
        t.left(110)
        t.forward(182)
        home(t)
