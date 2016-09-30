import turtle
pen=turtle.Turtle()
import random
szin=random.choice(["green","blue","black","yellow","purple","pink"])

def negyzet(oldalhossz):
    for i in  range(4):
        pen.forward(oldalhossz)
        pen.right(90)

def negyzetek(oldalhossz):
    negyzet(oldalhossz)
    pen.up()
    pen.forward(oldalhossz*1/5)
    pen.right(90)
    pen.forward(oldalhossz*1/5)
    pen.left(90)
    pen.down()
    negyzet(oldalhossz*3/5)
    pen.up()
    pen.forward(oldalhossz*1/5)
    pen.right(90)
    pen.forward(oldalhossz*1/5)
    pen.left(90)
    pen.down()
    negyzet(oldalhossz*1/5)
    pen.up()
    pen.right(90)
    pen.forward(oldalhossz*4/5)
    pen.left(90)
    pen.forward(oldalhossz*4/5)
    pen.down()

def feladat(oldalhossz,darab):
    for i in range(darab):
        szin=random.choice(["green","blue","black","yellow","purple","pink"])
        pen.color(szin)
        negyzetek(oldalhossz)

feladat(60,3)

