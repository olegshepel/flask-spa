"""
AUTH
"""

from flask import jsonify, request, make_response
from app import app

@app.route('/unprotected')
def unprotected():
    return ''

@app.route('/protected')
def protected():
    return ''

@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login page'
    # auth = request.authorization
    # if auth and auth.password == 'password':
    #     #
    #     return ''
    # return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})
