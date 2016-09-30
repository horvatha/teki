import turtle
import random
david=turtle.Turtle()

david.forward(30)
def kezdojobb():
    david.left(90)
    david.forward(20)
    david.right(90)
    david.forward(10)
    david.right(90)
    david.forward(20)

def kozepso():
    david.left(90)
    david.forward(10)
    david.left(90)
    david.forward(20)
    david.right(90)
    david.forward(10)
    david.right(90)
    david.forward(20)

def visszateres():
    david.right(90)
    david.forward(50)
    david.right(90)
    david.forward(20)
    david.right(90)
    david.forward(50)
    david.right(90)
    david.forward(10)
    david.right(90)
    david.forward(50)
    david.left(90)
    david.forward(10)
    david.right(90)

def indulas():
    david.goto(0,0)
    david.right(90)
    david.forward(20)

for i in range(4):
    kezdojobb()
    for i in range(2):
        kozepso()
    visszateres()
    indulas()

david.back(20)

