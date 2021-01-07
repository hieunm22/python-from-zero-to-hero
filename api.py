import flask
from flask import request, jsonify
import pyodbc
import codecs
# import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.\sqlexpress;'
                      'Database=chatapp;'
                      'Trusted_Connection=yes;')
# clear = lambda: os.system('cls')

cursor = conn.cursor()
sql = "select * from [user]"

@app.errorhandler(401)
def page_forbidden(e):
    f = codecs.open('html/401.html', 'r')
    return f.read()

@app.errorhandler(404)
def page_not_found(e):
    f = codecs.open('html/404.html', 'r')
    return f.read()

def getUserFromResponseRow(row):
    if row is not None:
        return {
            "id": row[0],
            "username": row[1],
            "password": row[2],
            "email": row[3],
            "alias": row[4],
            "phone": row[5],
            "gender": row[6],
            "avatar": row[7],
            "status": row[10],
        }
    else:
        return {}

def getall():
    cursor.execute(sql)
    
    array = []
    for row in cursor:
        user = getUserFromResponseRow(row)
        array.append(user)
    return array

@app.route('/accounts', methods=['GET'])
def get_all_accounts():
    # clear()
    all = getall()
    return jsonify(all)

@app.route('/account', methods=['GET'])
def get_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    # clear()
    print('request = ')
    if ('Authorization' in request.headers):
        print(request.headers['Authorization'])

    cursor.execute(sql)

    for row in cursor:
        if row[0] == id:
            return getUserFromResponseRow(row)

    return {}

app.run()