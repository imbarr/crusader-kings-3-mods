from PIL import Image

color = (35, 35, 35)
img = Image.open("provinces.png").convert("RGB")

width, height = img.size
for x in range(0, width):
    for y in range(0, height):
        r, g, b = img.getpixel((x, y))
        if img.getpixel((x, y)) == color:
            print(x, " ", y)
