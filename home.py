import flask
from flask import request, jsonify
import pyodbc
import os
import helper
from helper import validate_token
import constants
from constants import response_400, response_401

app = flask.Flask(__name__)
app.config["DEBUG"] = True
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.\sqlexpress;'
                      'Database=chatapp;'
                      'Trusted_Connection=yes;')

def clear_console(func_name):
  os.system('cls')
  print(func_name)

cursor = conn.cursor()

@app.route('/api/home/identity_login_request', methods=['POST'])
def identity_login_request():
  print('request.data =', request.data)

  return {

  }

@app.route('/api/home/get_all_conversations_and_load_default_conversation/<id>', methods=['GET'])
def get_all_conversations_and_load_default_conversation(id):
  try:
    uid = int(id)
  except:
    return response_400
  clear_console('get_all_conversations_and_load_default_conversation')
  if ('Authorization' in request.headers):
    requestHeader = request.headers['Authorization']
    claims = validate_token(requestHeader)
  else:
    return response_401
  sql = "{ CALL sp_GetAllUserConversationAndLoadDefault (uid=?) }"
  params = (uid)
  # cursor.execute(sql, params)
  



  return {
    
  }

@app.route('/api/home', methods=['GET'])
def get_by_id():
  return {}

app.run()
