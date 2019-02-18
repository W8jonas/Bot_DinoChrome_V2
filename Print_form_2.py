import pygame, sys, os
from pygame.locals import *

from PIL import ImageGrab
import pyautogui
import time


def print_tela():
    Print = ImageGrab.grab(bbox=(350, 150, 990, 500))  # X1,Y1,X2,Y2
    print(Print.show())
    Print.save(f"print_XX.jpeg")


print_tela()


