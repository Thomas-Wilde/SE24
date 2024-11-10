import color as c
import logger as log
import generator as g
import io
from typing import List

##--------------------------------------------------------------------------##
def check_type(file: io.StringIO, type: str) -> bool:
    log.msgl("check filetype: ")
    file_type = file.readline().replace("\n", "")
    if file_type == type:
        log.msg("correct")
        return True
    log.msg("wrong")
    return False


##--------------------------------------------------------------------------##
def load_size(file: io.StringIO, size: List[int]) -> bool:
    log.msgl("extract size: ")
    width = -1
    height = -1
    try:
        line = file.readline().replace("\n", "")
        width = int(line)
        line = file.readline().replace("\n", "")
        height = int(line)
    except:
        log.msg("failed")
        return False
    log.msg("successful")
    size.append(width)
    size.append(height)
    return True


##--------------------------------------------------------------------------##
def load_palette(file: io.StringIO, palette: List[c.Color]) -> bool:
    log.msgl("extract color palette: ")
    palette.clear()
    line = file.readline().replace("\n", "")
    try:
        count = int(line)
        for _ in range(count):
            line = file.readline().replace("\n", "")
            rgb = line.split()
            color = c.Color(int(rgb[0]), int(rgb[1]), int(rgb[2]))
            palette.append(color)
    except:
        log.msg("failed")
        return False
    log.msg("successful")
    log.msg("extracted " + str(count) + " colors")
    return True


##--------------------------------------------------------------------------##
def main():
    log.start_info()
    size = []
    palette = []
    file = open("data.dat", "r")

    if check_type(file, "indeximage") == False:
        return
    if load_size(file, size) == False:
        return
    if load_palette(file, palette) == False:
        return
    log.msg("generate and save image")
    g.generate_image(size, palette, file)
    log.msg("finished")


##--------------------------------------------------------------------------##
if __name__ == "__main__":
    main()
