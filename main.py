import pgzrun
import pygame.display
from ctypes import windll

WIDTH = 800
HEIGHT = 600
hwnd = pygame.display.get_wm_info()["window"]
windll.user32.MoveWindow(hwnd, 550, 230, WIDTH, HEIGHT, False)

pgzrun.go()
