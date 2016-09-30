#!/usr/bin/env python3
# coding: utf-8

from turtle import *


def negyzet(oldalhossz):
    "Négyzetet rajzol."
    for i in range(4):
        teki.forward(oldalhossz)
        teki.right(90)


def negyzetsor(oldalhossz, darab):
    "Négyzetsort rajzol."
    for i in range(darab):
        negyzet(oldalhossz)
        up()
        forward(oldalhossz*2)
        down()

negyzetsor(5, 20)


def spiral():
    "Spirálvonal"
    for hossz in range(10, 101, 10):
        lali.forward(hossz)
        lali.right(90)
