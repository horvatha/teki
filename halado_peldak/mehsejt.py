import turtle
import random
szin=random.choice(["red","purple","green","blue","brown"])
teki=turtle.Turtle()
teki.speed(0)

def hatszog(oldalhossz):
    teki.left(90)
    for i in range(6):
        teki.forward(oldalhossz)
        teki.right(60)
    teki.right(120)
    teki.forward(oldalhossz)
    teki.left(60)
    teki.forward(oldalhossz)
    teki.right(30)
    

def hatszogsor(oldalhossz, darab):
    for i in range(darab):
        hatszog(oldalhossz)
    teki.right(150)
    teki.up()
    for i in range(darab):
        teki.forward(oldalhossz)
        teki.right(60)
        teki.forward(oldalhossz)
        teki.left(60)
    teki.left(120)
    teki.forward(oldalhossz)
    teki.right(60)
    teki.forward(oldalhossz)
    teki.left(90)
    teki.down()

def feladat(oldalhossz, darab, sor):
    for i in range(sor):
        szin=random.choice(["red","purple","green","blue","brown","orange"])
        teki.color(szin)
        hatszogsor(oldalhossz,darab)

feladat(15,5,4)



