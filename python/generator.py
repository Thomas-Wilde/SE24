import color as c
import io
from PIL import Image
from typing import List

##--------------------------------------------------------------------------##
def generate_image(size: List[int], palette: List[c.Color], file: io.StringIO):
    img = Image.new(mode="RGB", size=size)
    w = size[0]
    h = size[1]

    for y in range(h):
        line = file.readline().replace("\n", "")
        idxs = line.split()
        for x in range(w):
            idx = int(idxs[x])
            col = palette[idx]
            img.putpixel((x, y), (col.r, col.g, col.b))
    img.save("image.png")
