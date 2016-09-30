"""
Két teknős, lali és ili, bolyong véletlenszerűen a teknősvilágban.

Változások az eredeti változathoz képest:

- A bolyongás elején a bolyong_adott_tavolsagig függvény visszaviszi
  a tekit a kiindulópontba.
  teki.home() hazaviszi tekit, a tollat közben fel kell emeltetni.
 
- A bolyongás többször fut le, és a lépésszámok átlagolódnak.
  A sum függvény egy lista elemeit összegzi.
"""

import turtle
import random

szinek = ["pink", "blue", "red", "yellow", "gold", "brown", "cyan", "black", "green", "magenta"]

lali = turtle.Turtle()
ili = turtle.Turtle()
ili.speed(0)  # Leggyorsabb

def bolyong_adott_lepest(lepes=20):
    szin = random.choice(szinek)
    teki.color(szin)
    for i in range(lepes):
        lepes2(lali)
        lepes2(ili, 15)

def bolyong_adott_tavolsagig(tavolsag, teki):
    teki.up()
    teki.home()
    teki.down()

    szin = random.choice(szinek)
    teki.color(szin)
    lepes = 0
    while teki.distance(0,0) < tavolsag:
        lepes = lepes + 1
        lepes2(teki, 15)
    teki.stamp() # Ottmarad a teki jele ahol megállt
    return lepes

def hegycsucs(lepesszam=20, ili=ili, lali=lali):
    lali.right(3)
    for i in range(1,lepesszam+1):
        ili.color("green")
        ili.forward(3*i)
        ili.right(89.5)
        lali.color("blue")
        lali.forward(4*i)
        lali.right(89.5)

hegycsucs(90)
