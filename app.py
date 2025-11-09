'''
Chase Jamieson
HW 2 Toy Flask Application

'/': Implements default landing page displaying entries in db and link to insert page
'/insert': Implements page for inserting new entries into db
'''
import flask
from index import Index
from insert import Insert

app = flask.Flask(__name__)
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET'])

app.add_url_rule('/insert',
                 view_func=Insert.as_view('insert'),
                 methods=['GET','POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
