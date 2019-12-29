from flask import Flask, render_template, request, redirect, url_for
import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for
from AddReq import new_request

UPLOAD_FOLDER = 'upload'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        project = request.form['project']
        name = request.form['name']
        phone = request.form['phone']
        service = request.form['service']
        env = request.form['env']
        budget = request.form['budget']
        message = request.form['message']
        f = open("newsubs.txt", "a")
        f.write('\n'+project+'\n'+name+'\n'+phone+'\n'+service+'\n'+env+'\n'+budget+'\n'+message+'\n')
        f.close()
        f = request.files['file']
        f.save('upload/'+f.filename)
        return render_template('m.html', project=project)
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)

