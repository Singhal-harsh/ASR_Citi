from app import app, db
from app.models import Query, QueryWAV

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Query': Query, 'QueryWAV': QueryWAV}
