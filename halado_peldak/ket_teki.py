import turtle
lali = turtle.Turtle()
ili = turtle.Turtle()
ili.color("red")

def negyzet(oldalhossz):
    oldalhossz2 = oldalhossz*2**0.5/2
    ili.color("red")
    lali.color("blue")
    ili.right(45)
    for i in range(4):
            lali.forward(oldalhossz)
            lali.right(90)
            ili.forward(oldalhossz2)
            ili.right(90)
    ili.left(45)
    ili.up()
    ili.forward(oldalhossz)
    ili.down()
    lali.up()
    lali.forward(oldalhossz)
    lali.down()

def negyzetsor(oldalhossz,darab):
   for i in range(darab):
            negyzet(oldalhossz)

def negyzetcella(oldalhossz, sor):
    ili.speed(6)
    lali.speed(6)
    ili.up()
    lali.up()
    ili.backward(260)
    lali.backward(260)
    ili.left(90)
    lali.left(90)
    ili.forward(280)
    lali.forward(280)
    ili.right(90)
    lali.right(90)
    ili.down()
    lali.down()
    darab=0
    for i in range(sor):
        darab=darab+1
        negyzetsor(oldalhossz, darab)
        ili.up()
        lali.up()
        ili.backward(oldalhossz*darab)
        lali.backward(oldalhossz*darab)
        ili.right(90)
        lali.right(90)
        ili.forward(oldalhossz*1.5)
        lali.forward(oldalhossz*1.5)
        ili.left(90)
        lali.left(90)
        ili.down()
        lali.down()

negyzetcella(40,7)
