from teki import *
import random
speed(0)


def lepes_kis_kanyarral(hossz=20):
    forward(hossz)
    szog = random.random() * 90 - 45  # -45 és +45 fok között véletlen szög
    right(szog)


def meroleges_lepes(hossz=20):
    forward(hossz)
    irany = random.choice([right, left])
    irany(90)


def bolyong_adott_lepest(lepes=20):
    szin = random.choice(szinek)
    color(szin)
    for i in range(lepes):
        meroleges_lepes(15)
    tavolsag = distance(0, 0)
    haza()
    return tavolsag


def sokbolyongas_elmozdulas(bolyongasszam=20, lepesszam=15):
    elmozdulasok = []
    for i in range(bolyongasszam):
        elmozdulas = bolyong_adott_lepest(lepesszam)
        elmozdulasok.append(elmozdulas)
    return elmozdulasok


def bolyong_adott_tavolsagig(tavolsag):
    szin = random.choice(szinek)
    color(szin)
    lepesszam = 0
    while distance(0, 0) < tavolsag:
        lepesszam = lepesszam + 1
        lepes2(15)
    haza()
    return lepesszam


def sokbolyongas_lepesszam(bolyongasszam=20, tavolsag=150):
    lepesszamok = []
    for i in range(bolyongasszam):
        lepesszam = bolyong_adott_tavolsagig(tavolsag)
        lepesszamok.append(lepesszam)
