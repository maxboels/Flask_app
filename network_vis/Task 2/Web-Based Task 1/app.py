from flask import Flask, request 
from data_visualization import visualize_network


app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/calculate', methods=['POST'])


