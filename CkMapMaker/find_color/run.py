from PIL import Image

color = (4, 0, 33)
img = Image.open("provinces.png")

width, height = img.size
for x in range(0, width):
    for y in range(0, height):
        if img.getpixel((x, y)) == color:
            print(x, " ", y)
