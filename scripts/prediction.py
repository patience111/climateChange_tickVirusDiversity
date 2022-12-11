#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load deep learning model
model_075 = tf.keras.models.load_model('../models/6climates220502_128_3-256_lr0.001_b128e10000.best.h5') 

# read latitude and longitude and manipulate
with open('../datasets/latitude_and_longitude/lat.txt') as f:
    lat = f.read().splitlines()
lat = [float(ele) for ele in lat] 

with open('../datasets/latitude_and_longitude/lon.txt') as f:
    lon = f.read().splitlines()
lon = [float(ele) for ele in lon] 

lat_repeat720 = list(np.repeat(lat, 720))
lon_convert = [ele - 360 if ele >= 180 else ele for ele in lon]
lon_repeat360 = lon_convert * 360

def prediction_map(rcp):

'''predict global tick virus diversity under different rcps from year 2019-2030 
   via 4-year mean of each climate factor,
   the input is the rcp and return a 12-year prediction which store in a list of panda dataframe
'''
    plot_dfs = []
    meanT = []
    maxT = []
    for year in range(2016, 2028):
        mtemps = []
        maxtemps = []
        winds = []
        press = []
        precips = []
        hurs = []
        for idx in range(4):
            with open('../datasets/climate_extract_byCMIP6_data_process/tas_all_annual_' + rcp + str(year+idx) + '.txt') as f:
                mtemp = f.read().splitlines()
            mtemp = [float(ele) for ele in mtemp]
            mtemps.append(mtemp)

            with open('../datasets/climate_extract_byCMIP6_data_process/tasmax_all_annual_' + rcp + str(year+idx) + '.txt') as f:
                maxtemp = f.read().splitlines()
            maxtemp = [float(ele) for ele in maxtemp]
            maxtemps.append(maxtemp)

            with open('../datasets/climate_extract_byCMIP6_data_process/wind_all_annual_' + rcp +str(year+idx) + '.txt') as f:
                wind = f.read().splitlines()
            wind = [float(ele) for ele in wind]
            winds.append(wind)

            with open('../datasets/climate_extract_byCMIP6_data_process/pressure_all_annual_' + rcp + str(year+idx) + '.txt') as f:
                pres = f.read().splitlines()
            pres = [float(ele) for ele in pres]
            press.append(pres)

            with open('../datasets/climate_extract_byCMIP6_data_process/preci_all_annual_' + rcp + str(year+idx) + '.txt') as f:
                precip = f.read().splitlines()
            precip = [float(ele) for ele in precip]
            precips.append(precip)

            with open('../datasets/climate_extract_byCMIP6_data_process/humidity_all_annual_'+ rcp + str(year+idx) + '.txt') as f:
                hur = f.read().splitlines()
            hur = [float(ele) for ele in hur]
            hurs.append(hur)

        mtemps_array = np.array(mtemps)
        mtemps_array_mean = np.mean(mtemps_array, axis=0)

        maxtemps_array = np.array(maxtemps)
        maxtemps_array_mean = np.mean(maxtemps_array, axis=0)

        winds_array = np.array(winds)
        winds_array_mean = np.mean(winds_array, axis=0)

        press_array = np.array(press)
        press_array_mean = np.mean(press_array, axis=0)

        precips_array = np.array(precips)
        precips_array_mean = np.mean(precips_array, axis=0)

        hurs_array = np.array(hurs)
        hurs_array_mean = np.mean(hurs_array, axis=0)

        dict_pre = {'mtemp':mtemps_array_mean.tolist(), 'maxtemp':maxtemps_array_mean.tolist(),
               'winds':winds_array_mean.tolist(), 'press':press_array_mean.tolist(),
                 'precips':precips_array_mean.tolist(), 'hurs':hurs_array_mean.tolist()}
        df_pre = pd.DataFrame.from_dict(dict_pre)
        v_pre = model_075.predict(df_pre)
        v_pre_list = []
        v_pre = v_pre.tolist()
        for ele in v_pre:
            v_pre_list += ele
        plot_dict = {'lat': lat_repeat720, 'lon':lon_repeat360, 'virus':v_pre_list}
        plot_df = pd.DataFrame.from_dict(plot_dict)
        plot_dfs.append(plot_df)
        
    return plot_dfs

