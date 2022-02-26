import pandas as pd
import numpy as np
from numpy import load
import tensorflow as tf

def load_and_predict():
    hn_model = tf.keras.models.load_model('Energy_model_divine-firebrand-59.h5')
    X_test = np.load('Classifier_X_test.npy', allow_pickle=True)
    X_fc_test = np.load('Classifier_X_fc_test.npy', allow_pickle=True)

    y_pred = hn_model.predict([X_test, X_fc_test], batch_size=1)
    y_pred = y_pred.round()
    return y_pred



#plot(X_val, X_fc_val, y_pred, y_val)
