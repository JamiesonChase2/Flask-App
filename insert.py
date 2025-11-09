from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
'''
Get route for simple rendering of template
Post route for processing form, and redirecting back to index.
'''

class Insert(MethodView):
    def get(self):
        return render_template('insert.html')
    def post(self):
        model = gbmodel.get_model() # insert form fields into our db model
        model.insert(request.form['title'], request.form['artist'], request.form['genre'],request.form['rating'])
        return redirect(url_for('index'))