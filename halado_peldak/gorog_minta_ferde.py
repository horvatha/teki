import turtle
lali=turtle.Turtle()
lali.up()
lali.backward(200)
lali.down()


def gorog (oldalhossz=100,tav=60):
    lali.left(60)
    lali.forward(oldalhossz)
    lali.right (60)
    lali.forward (40)
    lali.right (120)
    lali.forward (oldalhossz/4)
    lali.right (60)
    lali.forward (20)
    lali.left(60)
    lali.forward(oldalhossz-oldalhossz/4)
    lali.left (120)
    lali.forward(tav)
    
def gorogsorozat(n=4):
    for i in range(n):
        gorog()

gorogsorozat()        


