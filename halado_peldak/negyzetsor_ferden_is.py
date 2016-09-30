import turtle
import random
toll=turtle.Turtle()

def negyzet(oldalhossz):
    for i in range(4):
        toll.forward(oldalhossz)
        toll.right(90)

def negyzetsor(oldalhossz,oszlop):
    for i in range(oszlop):
        szin=random.choice(["red","gold","purple","green","blue","brown"])
        toll.color(szin)
        negyzet(oldalhossz)
        toll.up()
        toll.forward(oldalhossz)
        toll.down()
    toll.up()
    toll.backward(oldalhossz*oszlop)
    toll.right(90)
    toll.forward(oldalhossz)
    toll.left(90)
    toll.down()

def tabla(oldalhossz,oszlop,sor):
    for i in range(sor):
        negyzetsor(oldalhossz,oszlop)
    toll.up()
    toll.left(90)
    toll.forward(sor*oldalhossz)
    toll.right(90)
    toll.down()

def feladat(oldalhossz,oszlop,sor,szög):
    tabla(oldalhossz,oszlop,sor)
    toll.right(szög)
    tabla(oldalhossz,oszlop,sor)
    toll.left(szög)
    

toll.speed(7)
toll.up()
toll.left(90)
toll.forward(250)
toll.left(90)
toll.forward(100)
toll.left(180)
toll.down()

feladat(40,7,5,30)

"""
A feladat megadása paraméterekkel:
(négyzetek oldalhossza,oszlopok száma,sorok száma, elfordulás szöge)
"""








    


        
        

