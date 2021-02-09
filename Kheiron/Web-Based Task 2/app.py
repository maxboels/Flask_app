from evaluatexpression import evaluate
from flask import Flask, request 
app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/calculate', methods=['POST'])
def show_post():
    formula = request.data.decode()
    formula=formula.split()
    result=(evaluate(formula))
    if(result.is_integer()==True):
        result=int(result)
    return str(result)

