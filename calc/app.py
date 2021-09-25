from flask import Flask
from flask import request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def addition():
    """Adds a and b together"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a, b))


@app.route('/sub')
def subtract():
    """Subtract b from a"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a, b))


@app.route('/mult')
def multiply():
    """Multiply a and b"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a, b))


@app.route('/div')
def divide():
    """Divide a by b"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a, b))


operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}


@app.route('/math/<operation>')
def execute_operation(operation):
    """Execute the passed in math operation with a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operators[operation](a, b))
