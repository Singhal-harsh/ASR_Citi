import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


def add_queries_from_txt(txt_path):
    queries = []
    batch_counter = 0
    with open(txt_path, 'r') as file:
        query = file.readline()
        while query != "":
            queries_committed = False
            query = query.strip()
            if query != "":
                queries.append(models.Query(query_string=query))
                batch_counter += 1
            if batch_counter % batch_size == 0:
                db.session.add_all(queries)
                db.session.commit()
                batch_counter = 0
                queries_committed = True
                queries = []
            query = file.readline()
        if queries != [] and not queries_committed:
            db.session.add_all(queries)
            db.session.commit()


batch_size = 100000
if not models.Query.query.count():
    if os.path.isfile(app.config.get("QUERIES_TXT_FILE")):
        add_queries_from_txt(app.config.get("QUERIES_TXT_FILE"))

    elif os.path.isfile("data/vocab-tagged.xlsx"):
        os.system("python query_generation.py")
        add_queries_from_txt(app.config.get("QUERIES_TXT_FILE"))
