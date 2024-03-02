# main.py

from flask import Flask, request, jsonify, render_template
from PIL import Image, ImageOps
import os

app = Flask(__name__)

chars = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]

def get_char_from_pixel(p):
    if p < 25:
        return chars[0]
    elif p < 51:
        return chars[1]
    elif p < 76:
        return chars[2]
    elif p < 102:
        return chars[3]
    elif p < 127:
        return chars[4]
    elif p < 153:
        return chars[5]
    elif p < 178:
        return chars[6]
    elif p < 204:
        return chars[7]
    elif p < 229:
        return chars[8]
    elif p <= 255:
        return chars[9]

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate_ascii', methods=['POST'])
def your_endpoint():
    try:
        file = request.files['file']
        scale_factor = float(request.form['scale_factor'])

        # Save the uploaded file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Generate ASCII art
        ascii_art = generate_ascii_art(file_path, scale_factor)

        return jsonify({'ascii_art': ascii_art})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

