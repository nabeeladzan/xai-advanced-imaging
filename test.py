from PIL import Image
from methods import *

input_image = Image.open("origin.jpg")

active = 4



if (active == 0):
    average2x(input_image)
    weighted2x(input_image)
elif (active == 1):
    average2x(input_image)
elif (active == 2):
    weighted2x(input_image)
elif (active == 3):
    grayscale(input_image)
elif (active == 4):
    XTS100(input_image)