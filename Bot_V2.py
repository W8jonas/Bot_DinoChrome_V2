import pygame, sys, os
from pygame.locals import *

from PIL import ImageGrab
import pyautogui
import time

# (83, 83, 83) -- Cacto      (247, 247, 247)  -- Fundo

X = 550.0
Y1 = 415
Y2 = 385
Y3 = 340

Pontos = 0


def print_tela():
    Print = ImageGrab.grab()
    return Print


def ler_tela(screen):
    pixel_color_1 = screen.getpixel((int(X), Y1))
    pixel_color_2 = screen.getpixel((int(X), Y2))
    pixel_color_3 = screen.getpixel((int(X), Y3))

    if pixel_color_1 == (83, 83, 83):
        return 0
    elif pixel_color_2 == (83, 83, 83):
        return 1
    elif pixel_color_3 == (83, 83, 83):
        return 2
    else:
        return 3


print("Iniciando em 1 segundo")
time.sleep(1)
Contador_img = 0

while True:
    screen = print_tela()
    if ler_tela(screen) != 3:

        if ler_tela(screen) == 0:
            pyautogui.press("up")
            print("Em baixo")

        elif ler_tela(screen) == 1:
            pyautogui.press("down")
            print("No meio")

        elif ler_tela(screen) == 2:
            pyautogui.press("down")
            print("Em cima")

        Pontos += 1
        X += 0.5
        print(Pontos)
