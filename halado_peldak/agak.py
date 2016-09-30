import turtle
import random

teki=turtle.Turtle()


def lanc(oldalhossz):
    szin=random.choice(["green","blue","purple","red","pink"])
    teki.color(szin)
    m=0
    m=m+1
    teki.forward(m*oldalhossz)
    teki.right(90)
    teki.forward(m*oldalhossz)
    teki.left(90)
    m=m+1
    teki.forward(m*oldalhossz)
    teki.left(90)
    teki.forward(m*oldalhossz)
    teki.right(90)
    m=m+1
    teki.forward(m*oldalhossz)
    teki.right(90)
    teki.forward(m*oldalhossz)
    teki.left(90)
    m=m+1
    teki.forward(m*oldalhossz)
    teki.left(90)
    teki.forward(m*oldalhossz)
    teki.up()
    teki.home()
    teki.down()


" lanc(20)"


def lancsor(oldalhossz):
        lanc(oldalhossz)
        teki.left(90)
        lanc(oldalhossz)
        teki.left(180)
        lanc(oldalhossz)
        teki.left(270)
        lanc(oldalhossz)

lancsor(30)
