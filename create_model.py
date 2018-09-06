#####################################################
#
# A sample program for machine learning by using
# open source library scikit-learn.
#
#####################################################

import sklearn
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import pickle

# load test data
data = pd.read_csv( "test.csv" )

# load 
print(data)
Y = data.values[:, 7]
X = data.values[:,1:7]
print( Y )
print( X )

# split data into radom training data
X_train, X_test, Y_train, Y_test = train_test_split( X, Y )

# Logistic regression data analyze on test data
model = LogisticRegression()
model.fit( X_train, Y_train )

score = model.score( X_test, Y_test )

print( 'Estimate of generalization performance: ', score )

# treaming result
pickle.dump( model, open( "model.pickle", "wb" ) )
