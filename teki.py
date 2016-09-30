"""
Alapfüggvények importálása
"""

from turtle import forward, right, left
from turtle import speed, color, up, down
from turtle import position, distance, home, stamp, clear
import turtle
from random import choice, random

szinek = "red green blue cyan yellow magenta black orange brown".split()


def haza():
    up()
    home()
    down()


def veletlen_szin():
    return choice(szinek)
