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

#lali = turtle.Turtle()
ili = turtle.Turtle()
ili.speed(0)  # Leggyorsabb

def lepes1(teki, hossz=20, maxszog=120):
    teki.forward(hossz)
    szog = random.random() * 2*maxszog - maxszog  # -szog és +szog között véletlen szög
    teki.right(szog)

def lepes2(teki, hossz=20):
    teki.forward(hossz)
    irany = random.choice([teki.right, teki.left])
    irany(90)

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
        lepes1(teki, 15)
    teki.stamp() # Ottmarad a teki jele ahol megállt
    return lepes

lepesek= []
for i in range(20):
    lepes = bolyong_adott_tavolsagig(150, ili)
    lepesek.append(lepes)
    print("Az eddigi lépésszámok:", lepesek)
    print("Az átlagos lépésszám:", sum(lepesek)/len(lepesek))

