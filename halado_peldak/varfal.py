import turtle
kata=turtle.Turtle()

def kigyo(oldalhossz,kata):
    for i in range(4):
        kata.forward(oldalhossz)
        kata.left(90)
        kata.forward(oldalhossz)
        kata.right(90)
        kata.forward(oldalhossz)
        kata.right(90)
        kata.forward(oldalhossz)
        kata.left(90)



def hullamsor(oldalhossz,darab,kata):
    for i in range(darab):
        kigyo(oldalhossz, kata)

kata.speed(0)
hullamsor(10,4,kata)
