import pyautogui
from PIL import ImageGrab
import time

print(pyautogui.position())
# Point(x=692, y=390) - dinosaur
# Point(x=786, y=389) - close to dino
# Point(x=1194, y=476) - background
dino = ImageGrab.grab()
dino_color = dino.getpixel((726, 390))

background = ImageGrab.grab()
background_color = background.getpixel((1194, 476))

while True:
    terrain = ImageGrab.grab()
    terrain_color_pixels = [i for i in range(741, 848)]
    # print(terrain_color_pixels)
    # terrain_color = terrain.getpixel((810, 385))
    # if background_color != terrain_color:
    #     pyautogui.press('up')

    for element in terrain_color_pixels:
        terrain_color = terrain.getpixel((element, 388))
        if dino_color == terrain_color:
            pyautogui.press('up')
            break