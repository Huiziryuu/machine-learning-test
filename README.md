# machine-learning-test
a technique research sample

A simple techinique reaserch sample.
Mainly used open source libs inlude:
1. scikit-learn: machine learning lib
   http://scikit-learn.org/stable/index.html
2. flask: hold web service
   http://flask.pocoo.org/
3. pandas: process data
   https://pandas.pydata.org/
   
Prepare:
install scikit-learn, flask, pandas through pip or anaconda

Setup:
1. compile the module create_model.py:
   python create_model.py
2. launch flask webservice:
   export FLASK_APP=app.py
   flask run
   
Test the protocol:

curl -X POST http://localhost:5000/q -H "Content-Type: application/json" -d '{ "q1" : 1, "q2" : 5, "q3" : 5, "q4" : 3, "q5" : 5, "q6" : 5 }'
