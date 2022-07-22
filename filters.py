from audioop import avg
from PIL import Image, ImageEnhance


def grayscale(input_image):
    width, height = input_image.size
    new_width = width
    new_height = height
    img = Image.new(mode="RGB", size=(new_width, new_height))
    pixel_map = img.load()
    percentage = 0

    for i in range(width):
        for j in range(height):
            percent = round((i/width)*100, 0)
            if (percentage != percent):
                percentage = percent
                if (percentage % 5 == 0):
                    pass
            # getting the RGB pixel value.
            r, g, b = input_image.getpixel((i, j))

            # Apply formula of grayscale:
            grayscale = (0.299*r + 0.587*g + 0.114*b)

            # setting the pixel value.
            pixel_map[i, j] = (
                int(grayscale), int(grayscale), int(grayscale))

    img.save("display.jpeg", format="jpeg")


def filmic(input_image):
    width, height = input_image.size
    img = Image.new(mode="RGB", size=(width, height))

    percentage = 0
    contrast = ImageEnhance.Contrast(input_image)
    filter1 = contrast.enhance(1.1)
    sharpness = ImageEnhance.Sharpness(filter1)
    filter2 = sharpness.enhance(1.2)
    color = ImageEnhance.Color(filter2)
    filter3 = color.enhance(1.2)
    pixel_map = img.load()

    for i in range(width):
        for j in range(height):
            percent = round((i/width)*100, 0)
            if (percentage != percent):
                percentage = percent
                if (percentage % 5 == 0):
                    pass
            # getting the RGB pixel value.
            r, g, b = filter3.getpixel((i, j))

            pixel_map[i, j] = (int(r*0.925), int(g*0.9), int(b*0.875))

    img.save("display.jpeg", format="jpeg")


def desat(input_image):
    width, height = input_image.size
    img = Image.new(mode="RGB", size=(width, height))

    percentage = 0
    contrast = ImageEnhance.Contrast(input_image)
    filter1 = contrast.enhance(0.9)
    sharpness = ImageEnhance.Sharpness(filter1)
    filter2 = sharpness.enhance(1.2)
    color = ImageEnhance.Color(filter2)
    filter3 = color.enhance(0.9)
    pixel_map = img.load()

    for i in range(width):
        for j in range(height):
            percent = round((i/width)*100, 0)
            if (percentage != percent):
                percentage = percent
                if (percentage % 5 == 0):
                    pass
            # getting the RGB pixel value.
            r, g, b = filter3.getpixel((i, j))
            avg = (r+g+b)/3

            pixel_map[i, j] = (int((avg+r)/2), int((avg+g)/2), int((avg+b)/2))

    img.save("display.jpeg", format="jpeg")
