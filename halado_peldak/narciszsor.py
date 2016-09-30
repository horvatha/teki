import turtle
import random
dudi=turtle.Turtle()

def negyzet(oldalhossz):
    for i in range(4):
        dudi.forward(oldalhossz)
        dudi.right(90)

def belsonegyzet(oldalhossz):
    szin=random.choice(["red", "blue", "green", "purple"])
    dudi.color(szin)
    for i in range(4):
        negyzet(oldalhossz)
        dudi.right(90)

def kulsonegyzet(oldalhossz):
    szin=random.choice(["red", "blue", "green", "purple"])
    dudi.color(szin)
    for i in range(4):
        negyzet(oldalhossz*2**0.5)
        dudi.right(90)


def narcisz(oldalhossz):
    belsonegyzet(oldalhossz)
    dudi.right(45)
    kulsonegyzet(oldalhossz)


def narciszsor(oldalhossz,darab):
    for i in range(darab):
        narcisz(oldalhossz)
        dudi.left(45)
        dudi.up()
        dudi.forward(oldalhossz*4)
        dudi.down()

dudi.speed(0)
narciszsor(10,4)
