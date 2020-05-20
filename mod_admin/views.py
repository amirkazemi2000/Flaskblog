from flask import session
from . import admin 


@admin.route('/admin/')
def index():
    return 'Hello from admin index'

@admin.route('/login/')
def login():
    session['name'] = 'amir'
    print(session)
    return '1'