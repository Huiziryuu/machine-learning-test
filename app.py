#####################################################
#
# Running model as web service on Flask
#
#####################################################

import sklearn
from sklearn import linear_model
import pickle
import numpy as np
from flask import Flask, request, jsonify
app = Flask(__name__)

model = pickle.load( open( "model.pickle", "rb" ) )


@app.route('/q', methods=['POST'])
def hello():   
    resp = []
    resp.append(int(request.json['q1']))
    resp.append(int(request.json['q2']))
    resp.append(int(request.json['q3']))
    resp.append(int(request.json['q4']))
    resp.append(int(request.json['q5']))
    resp.append(int(request.json['q6']))
    return  jsonify(np.array2string(model.predict(np.array(resp).reshape(1, -1))))
