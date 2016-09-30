import turtle
import random
toll=turtle.Turtle()
szin = random.choice([ "black", "blue", "red", "purple", "darkgreen"])

def hullam(oldalhossz):
    toll.left(60)
    toll.forward(oldalhossz)
    toll.right(120)
    toll.forward(oldalhossz)
    toll.left(60)



def hullamsor(oldalhossz, darab):
    szin = random.choice([ "black", "blue", "red", "purple", "darkgreen"])
    toll.color(szin)
    for i in range(darab):
        hullam(oldalhossz)
    toll.up()
    toll.backward(darab*oldalhossz)
    toll.right(90)
    toll.forward(oldalhossz*2)
    toll.left(90)
    toll.down()


def feladat(oldalhossz,darab):
    hullamsor(oldalhossz,darab)
    hullamsor(oldalhossz*2,darab)
    hullamsor(oldalhossz*3,darab)
    hullamsor(oldalhossz*4,darab)

feladat(25,5)
