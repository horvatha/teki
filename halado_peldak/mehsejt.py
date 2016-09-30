import turtle
import random
szin=random.choice(["red","purple","green","blue","brown"])
toll=turtle.Turtle()
toll.speed(0)

def hatszog(oldalhossz):
    toll.left(90)
    for i in range(6):
        toll.forward(oldalhossz)
        toll.right(60)
    toll.right(120)
    toll.forward(oldalhossz)
    toll.left(60)
    toll.forward(oldalhossz)
    toll.right(30)
    

def hatszogsor(oldalhossz,darab):
    for i in range(darab):
        hatszog(oldalhossz)
    toll.right(150)
    toll.up()
    for i in range(darab):
        toll.forward(oldalhossz)
        toll.right(60)
        toll.forward(oldalhossz)
        toll.left(60)
    toll.left(120)
    toll.forward(oldalhossz)
    toll.right(60)
    toll.forward(oldalhossz)
    toll.left(90)
    toll.down()

def feladat(oldalhossz,darab,sor):
    for i in range(sor):
        szin=random.choice(["red","purple","green","blue","brown","orange"])
        toll.color(szin)
        hatszogsor(oldalhossz,darab)

feladat(15,5,4)



