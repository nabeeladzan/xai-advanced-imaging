
from PIL import Image, ImageEnhance


def average2x(input_image):
    width, height = input_image.size
    new_width = width * 2
    new_height = height * 2
    img = Image.new(mode="RGB", size=(new_width, new_height))
    pixel_map = img.load()
    tworatio = 2

    for i in range(width):
        for j in range(height):
            print(str(i) + " x " + str(j))
            # getting the RGB pixel value.
            r, g, b = input_image.getpixel((i, j))
            try:
                r2, g2, b2 = input_image.getpixel((i, j+1))
            except:
                pass
            try:
                r3, g3, b3 = input_image.getpixel((i+1, j))
            except:
                pass

            # Apply formula of grayscale:
            grayscale = (0.299*r + 0.587*g + 0.114*b)
            x = i * 2
            y = j * 2

            pixel_map[x, y] = (r, g, b)
            pixel_map[x, y+1] = (int(round((r+r2)/tworatio, 3)),
                                 int(round((g+g2)/tworatio, 3)), int(round((b+b2)/tworatio, 3)))
            pixel_map[x+1, y] = (int(round((r+r3)/tworatio, 3)),
                                 int(round((g+g3)/tworatio, 3)), int(round((b+b3)/tworatio, 3)))
            pixel_map[x+1, y+1] = (int(round((r+r2+r3)/3, 3)),
                                   int(round((g+g2+g3)/3, 3)), int(round((b+b2+b3)/3, 3)))

    img.save("originF.jpeg", format="jpeg")
    img.show()


def weighted2x(input_image):
    width, height = input_image.size
    new_width = width * 2
    new_height = height * 2
    img = Image.new(mode="RGB", size=(new_width, new_height))
    pixel_map = img.load()
    percentage = 0
    tworatio = 2
    threeratio = 3

    for i in range(width):
        for j in range(height):
            percent = round((i/width)*100, 0)
            if (percentage != percent):
                percentage = percent
                if (percentage % 5 == 0):
                    print(percentage)
            # getting the RGB pixel value.
            r, g, b = input_image.getpixel((i, j))
            sum = (r+g+b)/3
            try:
                r2, g2, b2 = input_image.getpixel((i, j+1))
                sum2 = (r2+g2+b2)/3
            except:
                pass
            try:
                r3, g3, b3 = input_image.getpixel((i+1, j))
                sum3 = (r3+g3+b3)/3
            except:
                pass

            # Apply formula of grayscale:
            grayscale = (0.299*r + 0.587*g + 0.114*b)
            x = i * 2
            y = j * 2

            pixel_map[x, y] = (r, g, b)
            if (sum*2 < sum2*0.8):
                pixel_map[x, y+1] = (int(round((r*1.2+r2)/tworatio, 3)), int(
                    round((g*1.2+g2)/tworatio, 3)), int(round((b*1.2+b2)/tworatio, 3)))
            elif (sum*2 > sum2*1.2):
                pixel_map[x, y+1] = (int(round((r2*0.8+r)/tworatio, 3)), int(
                    round((g2*0.8+g)/tworatio, 3)), int(round((b2*0.8+b)/tworatio, 3)))
            else:
                pixel_map[x, y+1] = (int(round((r+r2)/tworatio, 3)), int(
                    round((g+g2)/tworatio, 3)), int(round((b+b2)/tworatio, 3)))

            if (sum*2 < sum3*0.8):
                pixel_map[x+1, y] = (int(round((r*1.2+r3)/tworatio, 3)), int(
                    round((g*1.2+g3)/tworatio, 3)), int(round((b*1.2+b3)/tworatio, 3)))
            elif (sum*2 > sum3*1.2):
                pixel_map[x+1, y] = (int(round((r3*0.8+r)/tworatio, 3)), int(
                    round((g3*0.8+g)/tworatio, 3)), int(round((b3*0.8+b)/tworatio, 3)))
            else:
                pixel_map[x+1, y] = (int(round((r+r3)/tworatio, 3)), int(
                    round((g+g3)/tworatio, 3)), int(round((b+b3)/tworatio, 3)))

            if (sum > sum2*1.25 and sum > sum3*1.25):
                pixel_map[x+1, y+1] = (int(round((r*1.1+r2*0.95+r3*0.95)/3, 3)), int(
                    round((g*1.1+g2*0.95+g3*0.95)/3, 3)), int(round((b*1.1+b2*0.95+b3*0.95)/3, 3)))
            elif (sum2 > sum*1.25 and sum2 > sum3*1.25):
                pixel_map[x+1, y+1] = (int(round((r*0.95+r2*1.1+r3*0.95)/3, 3)), int(
                    round((g*0.95+g2*1.1+g3*0.95)/3, 3)), int(round((b*0.95+b2*1.1+b3*0.95)/3, 3)))
            elif (sum3 > sum*1.25 and sum3 > sum2*1.25):
                pixel_map[x+1, y+1] = (int(round((r*0.95+r2*0.95+r3*1.1)/3, 3)), int(
                    round((g*0.95+g2*0.95+g3*1.1)/3, 3)), int(round((b*0.95+b2*0.95+b3*1.1)/3, 3)))
            else:
                pixel_map[x+1, y+1] = ((int(round((r+r2+r3)/threeratio, 3)), int(
                    round((g+g2+g3)/threeratio, 3)), int(round((b+b2+b3)/threeratio, 3))))

    img.save("originW.jpeg", format="jpeg")
    img.show()


def grayscale(self, input_image):
    self.width, self.height = input_image.size
    self.new_width = self.width
    self.new_height = self.height
    self.img = Image.new(mode="RGB", size=(self.new_width, self.new_height))
    self.pixel_map = self.img.load()
    percentage = 0

    for i in range(self.width):
        for j in range(self.height):
            percent = round((i/self.width)*100, 0)
            if (percentage != percent):
                percentage = percent
                if (percentage % 5 == 0):
                    print(percentage)
            # getting the RGB pixel value.
            r, g, b = input_image.getpixel((i, j))

            # Apply formula of grayscale:
            grayscale = (0.299*r + 0.587*g + 0.114*b)

            # setting the pixel value.
            self.pixel_map[i, j] = (
                int(grayscale), int(grayscale), int(grayscale))

    return self.img


def XTS100(input_image):
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
                    print(percentage)
            # getting the RGB pixel value.
            r, g, b = filter3.getpixel((i, j))

            if(r > 200 and g > 200 and b > 200):
                pixel_map[i, j] = (int(r*0.925), int(g*0.9), int(b*0.875))
            elif (r > 50 and g > 50 and b > 50):
                pixel_map[i, j] = (int(r*1.075), int(g*1.05), int(b*1.025))
            else:
                pixel_map[i, j] = (int(r*1.025), int(g*1), int(b*0.975))

    img.save("originXTS100.jpeg", format="jpeg")
    img.show()
