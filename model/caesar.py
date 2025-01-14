# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:34:47 2019

@author: patri AND PETER
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #some visuals, dont need in program

def main():

    dataPath = "caepairs.csv"
    train(dataPath)

def train(dataPath):
    percent = 0.8
    data = pd.read_csv(dataPath).values
    labels = []
    datas = []
    #formatting
    for i in range(0,len(data)):
        labels.append((data[i][0]-1)%26)
        datas.append(data[i][1:])
    #normalize to [0,1] frequencies
    for i in range(0,len(data)):
        datas[i] = np.true_divide(datas[i], np.sum(datas[i]))
    #create model
    model = keras.Sequential()
    model.add(keras.layers.Dense(26, activation=tf.nn.sigmoid))
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    numTest = round(len(datas)*percent)
    trial_data = datas[:numTest]
    test_data = datas[numTest:]

    trial_labels = labels[:numTest]
    test_labels = labels[numTest:]
    #8523 in caepairs.csv
    #test it, first 6000 5 times through, test around 2500
    model.fit(np.array(trial_data), np.array(trial_labels), epochs=10, batch_size = 32)
    dfsdf = model.evaluate(np.array(test_data),np.array(test_labels))
    print(dfsdf)

if __name__ == "__main__":
    main()
