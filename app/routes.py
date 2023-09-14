from flask import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/add')
def add():
    data = request.args.get('data', None)
    
    if not data:
        return "No data provided!", 400
    
    try:
        _list = list(map(int, data.split(',')))
        total = calculate_sum(_list)
    except Exception as e:
        return f"Error occurred: {e}", 500

    return 'Result= ' + str(total)

def calculate_sum(arg):
    total = 0
    try:
        for val in arg:
            total += val
    except TypeError as te:
        # if arg is not iterable or contains unsupported types
        return ("Internal Server Error", 500)
    return total
