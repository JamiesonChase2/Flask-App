from flask import render_template
from flask.views import MethodView
import gbmodel
'''
Selects rows from database and passes into template
'''
class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        songs = [dict(title=r[0], artist=r[1], genre=r[2], rating=r[3]) for r in model.select()]
        return render_template('index.html',songs=songs)
