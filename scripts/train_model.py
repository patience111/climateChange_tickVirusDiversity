#!/usr/bin/env python
# coding: utf-8
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/for_model_training/Metadata_fullname_updated_v6_HL_3.tsv', sep='\t') # path is the dir which store data for training & test

factor_y = data[['meanpres','meanwind', 'meantemp', 'meanhum1', 'ssd', 'meanmaxtem', 'maxprec','meanmintem', 
                 'meanprec', 'OTU_new_Shannon_verfam1']] # extract the variables need to train the model

factor_y_shuffle = factor_y.reindex(np.random.permutation(factor_y.index))
train = factor_y_shuffle.iloc[:200,:]
test = factor_y_shuffle.iloc[200:,:]
train_x = train[['meanpres', 'meanwind', 'meantemp','meanhum1', 'meanprec', 'meanmaxtem']]# the six climate factors selected to train the model
train_y = train[['OTU_new_Shannon_verfam1']]
test_x = test[['meanpres', 'meanwind', 'meantemp','meanhum1', 'meanprec', 'meanmaxtem']]
test_y = test[['OTU_new_Shannon_verfam1']]

#model structure
def build_model():
'''the model structure'''
    model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, kernel_initializer='normal', activation='relu',input_shape=[6]),
    tf.keras.layers.Dense(256, kernel_initializer='normal', activation='relu'),
    tf.keras.layers.Dense(256, kernel_initializer='normal', activation='relu'),
    tf.keras.layers.Dense(256, kernel_initializer='normal', activation='relu'),
    tf.keras.layers.Dense(1, kernel_initializer='normal', activation='linear')
  ])

    optimizer = tf.keras.optimizers.Adam(0.001)
    #optimizer = tf.keras.optimizers.RMSprop(0.001)
    #model.compile(loss='mse', optimizer=optimizer, metrics=['mae', 'mse'])
    model.compile(loss='mean_absolute_error', optimizer=optimizer, metrics=['mean_absolute_error'])
    return model

#train the model, could set the device as GPUs if available or CPUs
with tf.device("cpu:0"):
    model = build_model()
    filepath = path + "6climates220502_128_3-256_lr0.001_b128e10000.best.h5"# the path and the names for saving models
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, 
                                 save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    history = model.fit(train_x, train_y, epochs=10000, callbacks=callbacks_list, batch_size=128) # model training
    
    model.save(path + '6climates220502_128_3-256_lr0.001_b128e10000.h5')
#training process plot
fig = plt.gcf()
plt.plot(history.history['loss'])
fig.savefig(path + '6climates220502_128_3-256_lr0.001_b128e10000_trainingv2.pdf')
