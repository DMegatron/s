from flask import Flask, request, render_template, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

latest_data = {
    'filename': None,
    'text': ''
}

@app.route('/')
def index():
    return render_template('index.html', data=latest_data)

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files.get('image')
    text = request.form.get('text')

    if image:
        filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        image.save(filepath)
        latest_data['filename'] = filename
        latest_data['text'] = text

    return 'OK'

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
