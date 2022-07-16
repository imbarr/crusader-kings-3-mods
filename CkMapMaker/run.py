from PIL import Image
import random

WHITE = (255, 255, 255, 255)
SPECIAL_COLORS = (WHITE, (255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255))

used_colors = []


def transform(image):
    width, height = image.size
    for x in range(0, width):
        for y in range(0, height):
            print("Checking ", x, " ", y, "\n")
            if image.getpixel((x, y)) == WHITE:
                print("Filled\n")
                fill(image, x, y)

    remove_borders(image)


def remove_borders(image):
    painted = []
    width, height = image.size
    found = False
    for x in range(width):
        for y in range(height):
            print("Checking2 ", x, " ", y, "\n")
            if image.getpixel((x, y)) in SPECIAL_COLORS:
                found = True
                neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                min_neighbor = None
                for n in neighbors:
                    if 0 <= n[0] <= width-1\
                            and 0 <= n[1] <= height-1\
                            and image.getpixel(n) not in SPECIAL_COLORS\
                            and n not in painted:
                        if min_neighbor is None or less(image.getpixel(n), image.getpixel(min_neighbor)):
                            min_neighbor = n

                if min_neighbor is not None:
                    image.putpixel((x, y), image.getpixel(min_neighbor))
                    painted.append((x, y))

    if found:
        remove_borders(image)


def less(color1, color2):
    return sum(color1) < sum(color2)


def fill(image, x, y):
    width, height = image.size
    seen = []
    stack = [(x, y)]
    new_color = gen_random_color()
    while stack:
        node = stack.pop()
        seen.append(node)
        color = image.getpixel(node)
        if color == WHITE:
            image.putpixel(node, new_color)
            x1, y1 = node
            neighbors = [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1)]
            for n in neighbors:
                if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                    if n not in seen and image.getpixel(n) == WHITE:
                        stack.append(n)


def gen_random_color():
    color = (random.randrange(256), random.randrange(256), random.randrange(256), 255)
    if color in SPECIAL_COLORS or color in used_colors:
        return gen_random_color()

    used_colors.append(color)
    return color


img = Image.open("Map.png")
transform(img)
img.save("GenMap.png")
