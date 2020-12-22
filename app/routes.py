from app import app
from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/record', methods=['POST', 'GET'])
def record():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('record.html', request="POST")
    else:
        return render_template("record.html")


@app.route('/record_random')
def record_random(name=None):
    return render_template('record-random.html', name=name)


@app.route('/record_select')
def record_select(name=None):
    return render_template('record-select.html', name=name)


@app.route('/view_samples')
def view_samples(name=None):
    return render_template('view-samples.html', name=name)


@app.route('/add_new_query')
def add_new_query(name=None):
    return render_template('add-new-query.html', name=name)
