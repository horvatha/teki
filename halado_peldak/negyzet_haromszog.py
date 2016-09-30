import turtle
rozi=turtle.Turtle()

rozi.speed(0)

def negyzet(oldalhossz):
    for i in range(4):
        rozi.forward(oldalhossz)
        rozi.right(90)

    
       

def haromszog(oldalhossz):
    rozi.up()
    rozi.right(90)
    rozi.forward(oldalhossz)
    rozi.left(90)
    rozi.down()
    for i in range(3):
        rozi.forward(oldalhossz)
        rozi.left(120)
    rozi.left(90)
    rozi.up()
    rozi.forward(oldalhossz)
    rozi.down()
    rozi.right(90)
    

def sor1 (oldalhossz,m):
    for i in range(m):
        negyzet(oldalhossz)
        rozi.up()
        rozi.forward(oldalhossz+oldalhossz/4)
        rozi.down()
        haromszog(oldalhossz)
        rozi.up()
        rozi.forward(oldalhossz+oldalhossz/4)
        rozi.down()

def sor2(oldalhossz,m):
    for i in range(m):
        negyzet(oldalhossz)
        rozi.up()
        rozi.forward(oldalhossz+oldalhossz/4)
        rozi.down()
        for i in range (2):
            haromszog(oldalhossz)
            rozi.up()
            rozi.forward(oldalhossz+oldalhossz/4)
            rozi.down()

def sor3(oldalhossz,m):
    for i in range(m):
        negyzet(oldalhossz)
        rozi.up()
        rozi.forward(oldalhossz+oldalhossz/4)
        rozi.down()
        for i in range (3):
            haromszog(oldalhossz)
            rozi.up()
            rozi.forward(oldalhossz+oldalhossz/4)
            rozi.down()


def feladat(oldalhossz,m):
    sor1(oldalhossz,m)
    rozi.up()
    rozi.home()
    rozi.right(90)
    rozi.forward(2*oldalhossz+oldalhossz/4)
    rozi.down()
    rozi.left(90)
    sor2(oldalhossz,m)
    rozi.up()
    rozi.home()
    rozi.right(90)
    rozi.forward(2*(2*oldalhossz+oldalhossz/4))
    rozi.down()
    rozi.left(90)
    sor3(oldalhossz,m)
    rozi.up()
    rozi.home()
    rozi.down()


feladat(15,5)


    




