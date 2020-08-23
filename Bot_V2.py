import time

from PIL import ImageGrab
import pyautogui

X = 450.0  # X2 = X + 90
Y1 = 380
Y2 = 410

def print_tela():
    screen = ImageGrab.grab()
    return screen

def ler_tela(screen):
    aux_color = screen.getpixel((int(X), Y1))
    for x in range(int(X), int(X+90)):
        for y in range(Y1, Y2):
            color = screen.getpixel((x, y))
            if color != aux_color:
                return True
            else:
                aux_color = color

print("Iniciando em 3 segundos")
time.sleep(3)

while True:
    screen = print_tela()
    if ler_tela(screen):
        pyautogui.press("up")
        X += 0.5
