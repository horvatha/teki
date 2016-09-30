from teki import *

speed(4)


def tortvonal(darab, szog, hossz=20):
    for i in range(darab):
        forward(hossz)
        right(szog)


def csillag1():
    color("blue")
    for i in range(5):
        forward(130)
        right(144)  # 180-36 = 144
