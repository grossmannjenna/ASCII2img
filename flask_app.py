# main.py

from flask import Flask, request, jsonify, render_template
from asciify import generate_ascii_art
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

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

        file.close()
        os.remove(file_path)

        return jsonify({'ascii_art': ascii_art})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

