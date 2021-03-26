from app import app, db
from flask import render_template, request, session, url_for, redirect
from sqlalchemy.sql import func
from app.models import Query, QueryWAV
import os
from STT_H import predict_text
from wer import score

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Index")


@app.route('/record', methods=['POST', 'GET'])
def record():
    audios_dir = "data/audios"
    os.makedirs(audios_dir, exist_ok=True)
    # print(dir(request))
    # print(request.method)
    # print(request.files)
    # query = None
    allowed_soeids = app.config.get("ALLOWED_SOEIDS")
    query_id = session.get("query_id")
    if query_id:
        query = Query.query.filter(Query.id==query_id).all()[0]
    else:
        query = Query.query.order_by(func.random()).first()
    posted_query_id = session.get("query_id")
    query_id = query.id
    query_string = query.query_string
    soeid = session.get("soeid", "")
    session["query_id"] = query_id
    true_text = session.get("true_text", None)
    predicted_text = session.get("predicted_text", None)
    accuracy_score = session.get("accuracy_score", None)


    if request.method == "POST":
        soeid = request.form.get("soeid")
        session["soeid"] = soeid
        # print('soeid:', soeid)
        if soeid in allowed_soeids:
            f = request.files['audio_data']
            filepath = f'{audios_dir}/{soeid}_audio_{query_id}.wav'
            with open(filepath, 'wb') as audio:
                f.save(audio)
            print('file uploaded successfully')
            wav = QueryWAV(query_id=posted_query_id, wav_location=filepath)
            db.session.add(wav)
            db.session.commit()
            predicted_text = predict_text(filepath)
            true_text = Query.query.filter(Query.id == posted_query_id).one().query_string
            print(predicted_text)
            print(true_text)
            accuracy_score = score(true_text, predicted_text)
            print(accuracy_score)
            session["true_text"]= true_text
            session["predicted_text"]= predicted_text
            session["accuracy_score"]= accuracy_score
            

        return render_template('record.html', request="POST", title="Record", query=query_string, soeid=soeid,
                               true_text=true_text, predicted_text=predicted_text, accuracy_score=accuracy_score)
    
    else:

        return render_template('record.html', title="Record", query=query_string, soeid=soeid,
                               true_text=true_text, predicted_text=predicted_text, accuracy_score=accuracy_score)

@app.route('/record_random')
def record_random(name=None):
    return render_template('record-random.html', name=name)


@app.route('/record_select')
def record_select(name=None):
    return render_template('record-select.html', name=name)


@app.route('/view_samples')
def view_samples():
    recordings = QueryWAV.query.join(Query, Query.id == QueryWAV.query_id).add_columns(QueryWAV.id,
                                                                                       QueryWAV.wav_location,
                                                                                       Query.query_string).all()

    return render_template('view-samples.html', recordings=recordings)


@app.route('/add_new_query', methods=['POST', 'GET'])
def add_new_query(name=None):
    if request.method == 'POST':
        text = (request.form.get('sentence')).lower()
        db_query = Query.query.filter(Query.query_string==text).all()
        if db_query:
            db_query = db_query[0]
            session["query_id"] = db_query.id
        else:
            new_id = db.session.query(Query, func.max(Query.id)).one()[0].id + 1
            new_query = Query(id=new_id, query_string=text)
            db.session.add(new_query)
            db.session.commit()
            print("Sentence added is: " + text)
            with open("data/queries.txt", "a+") as file_object:
                file_object.write("\n")
                file_object.write(text)

            os.system('python Generate_lm_H.py')
            session["query_id"] = new_id
        return redirect(url_for('record'))
    return render_template('add-new-query.html', name=name)

#    else:
#     return render_template('add-new-query.html', name=name)


# Query.query.options(load_only('id')).offsset(func.floor(func.random() * db.session.query(func.count(Query.id)))).limit(1).first()
#
# db.session.query(Query).order_by(func.random()).first()
# Query.query.order_by(func.random()).first()
