import turtle
import random
lali=turtle.Turtle()
def minta(a,szin):
    b=a/2 # Ez kint volt.
    lali.color(szin)
    for i in range(2):
        lali.forward(a)
        lali.left(90)
    lali.forward(b)
    lali.left(90)
    for i in range(2):
        lali.forward(b)
        lali.right(90)
    lali.forward(a)
    lali.right(90)
    lali.forward(1.5*a)
    lali.right(90)
    lali.forward(1.5*a)
    lali.left(90)
    lali.forward(b)

for i in range(6):
    szin=random.choice(["pink","red","blue","black","orange","purple"])
    a=20 + random.random()*40 # Kicsit módosítottam.
    # beleszúrt rész
    lali.up()
    lali.home()
    lali.backward(200)
    lali.right(90)
    lali.forward(i*70-140)
    lali.left(90)
    lali.down()

    for i in range(5):
        minta(a,szin)
    print (szin)
