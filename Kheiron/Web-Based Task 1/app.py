from flask import Flask, request 
from CheckIfoperandisnumber import is_operand
from EvaluationFunction import evaluate
from Datapreprocessing import preprocess

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/calculate', methods=['POST'])
def show_post():
    formula = request.data.decode()
    formula = preprocess(formula)
    result = evaluate(formula)
    print(result)
    return str(result)
