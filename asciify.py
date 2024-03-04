from PIL import Image, ImageOps
import os

chars = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]

def get_char_from_pixel(p):
    if p < 25:
        return chars[9]
    elif p < 51:
        return chars[8]
    elif p < 76:
        return chars[7]
    elif p < 102:
        return chars[6]
    elif p < 127:
        return chars[5]
    elif p < 153:
        return chars[4]
    elif p < 178:
        return chars[3]
    elif p < 204:
        return chars[2]
    elif p < 229:
        return chars[1]
    elif p <= 255:
        return chars[0]

def generate_ascii_art(file_path, scale_factor):
    try:
        im = Image.open(file_path)
        fileName = os.path.basename(file_path).split(".")[0]

        x_dimension, y_dimension = im.size[0], im.size[1]
        im = ImageOps.grayscale(im)


        ascii_str = ""

        im = im.resize((int(x_dimension / scale_factor), int(y_dimension / scale_factor)), resample=Image.LANCZOS)
        x_dimension, y_dimension = im.size[0], im.size[1]

        for i in range(0, y_dimension):
            ascii_str += "\n"
            for j in range(0, x_dimension):
                ascii_str += str(get_char_from_pixel(im.getpixel((j, i))))

        return ascii_str
    except Exception as e:
        return str(e)
