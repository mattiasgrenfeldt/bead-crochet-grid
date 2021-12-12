#!/usr/bin/env python3
from PIL import Image, ImageDraw

WIDTH = 1000
HEIGHT = 1000
CELL_SIZE = 10
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
GRID_WIDTH = 1

img = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
draw = ImageDraw.Draw(img)

# horizontal lines
for y in range(0, HEIGHT, CELL_SIZE):
    p0 = (0, y)
    p1 = (WIDTH - 1, y)
    draw.line((p0, p1), fill=GRID_COLOR, width=GRID_WIDTH)

# vertical lines
for (i, y) in enumerate(range(0, HEIGHT, CELL_SIZE)):
    offset = (i % 2)*CELL_SIZE//2
    for x in range(offset, WIDTH, CELL_SIZE):
        p0 = (x, y)
        p1 = (x, y + CELL_SIZE)
        draw.line((p0, p1), fill=GRID_COLOR, width=GRID_WIDTH)

img.save("grid.png")
