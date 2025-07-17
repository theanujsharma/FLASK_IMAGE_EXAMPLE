from flask import Flask, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Ensure the upload folder exists

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    uploaded_img = None
    if request.method == "POST":
        if 'pic' in request.files:
            img = request.files['pic']
            if img.filename != "":
                filename = secure_filename(img.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                img.save(file_path)
                uploaded_img = filename
    return render_template('index.html', uploaded_img=uploaded_img)

if __name__ == '__main__':
    app.run(debug=True)