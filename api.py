import flask
from flask import request, jsonify
import pyodbc
import codecs
import json
from string import Template

app = flask.Flask(__name__)
app.config["DEBUG"] = True
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.\sqlexpress;'
                      'Database=chatapp;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

@app.errorhandler(401)
def page_forbidden(e):
    f = codecs.open('html/401.html', 'r')
    return f.read()

@app.errorhandler(404)
def page_not_found(e):
    f = codecs.open('html/404.html', 'r')
    return f.read()

@app.route('/accounts', methods=['GET'])
def get_all_accounts():
    cursor.execute('SELECT * FROM [user]')
    array = []
    for row in cursor:
        user = {
            "id": row[0],
            "username": row[1],
            # "password": row[2],
            "email": row[3],
            "alias": row[4],
            "phone": row[5],
            "gender": 'Male' if row[6] is True else 'Female',
        }
        array.append(user)
    return jsonify(array)

@app.route('/account', methods=['GET'])
def get_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    users = get_all_accounts()
    results = []

    # for user in users:
    #     if user['id'] == id:
    #         results.append(user)

    # return json.dumps(users)

    return users

app.run()
