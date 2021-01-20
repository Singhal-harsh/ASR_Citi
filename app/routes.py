from app import app
from flask import render_template, request
from sqlalchemy.sql import func
from app.models import Query



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Index")


@app.route('/record', methods=['POST', 'GET'])
def record():
    # print(dir(request))
    # print(request.method)
    # print(request.files)
    query = None
    query = Query.query.order_by(func.random()).first()
    query_id = query.id
    query_string = query.query_string
    if request.method == "POST":
        print("test")
        # print(dir(request))
        # print(request.form)
        # print(request.data)
        f = request.files['audio_data']
        with open(f'audio_{query_id}.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('record.html', request="POST", title="Record", query=query_string)
    else:
        return render_template("record.html", title="Record", query=query_string)


@app.route('/record_random')
def record_random(name=None):
    return render_template('record-random.html', name=name)


@app.route('/record_select')
def record_select(name=None):
    return render_template('record-select.html', name=name)


@app.route('/view_samples')
def view_samples(name=None):
    return render_template('view-samples.html', name=name)


@app.route('/add_new_query' , methods=['POST', 'GET'])
def add_new_query(name=None):
    print("testing hello")
    # print("testing" + text)
    if request.method == 'POST':
        text = (request.form.get('sentence'))
    
    return render_template('add-new-query.html', name=name)
   
#    else:
#     return render_template('add-new-query.html', name=name)
      
    

# Query.query.options(load_only('id')).offsset(func.floor(func.random() * db.session.query(func.count(Query.id)))).limit(1).first()
#
# db.session.query(Query).order_by(func.random()).first()
# Query.query.order_by(func.random()).first()
