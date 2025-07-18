from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

latest_data = {
    'filename': None,
    'image_bytes': None,
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
        latest_data['filename'] = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")
        latest_data['image_bytes'] = image.read()  # Store image in memory (bytes)
        latest_data['text'] = text

    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
