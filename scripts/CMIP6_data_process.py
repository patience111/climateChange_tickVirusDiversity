#!/usr/bin/env python
import netCDF4 as nc
import numpy as np
import os

vars = ['hurs', 'pr', 'psl', 'sfcWind', 'tas', 'tasmax']

def extratct(source_path, var, year, rcp, dest_path):
    file = nc.Dataset(source_path + var + '_Amon_CNRM-CM6-1-HR_' + rcp + '_r1i1p1f2_gr_201501-210012.nc')
    var_extract = file.variables[var][:]
    var_extract_year = var_extract[12 + 12 * (year - 2016): 24 + 12 * (year - 2016) :]
    print(12 + 12 * (year - 2016))
    #if year == 2019:
     #   var_extract_year = var_extract[48:60:]
    #if year ==
    #if year == 2030:
     #   var_extract_year = var_extract[180:192:]
        
    if var == 'tas' or var == 'tasmax':
        var_extract_year_mean = np.mean(var_extract_year, axis=0)
        var_extract_year_mean_c = var_extract_year_mean - 273.5
        with open(dest_path + var + '_' + str(year) + '_mean_' + rcp + '.txt', 'w') as f:
            for ele in var_extract_year_mean_c.flatten():
                f.write(str(ele) + '\n') 
    
    if var == 'psl':
        var_extract_year_mean = np.mean(var_extract_year, axis=0)
        var_extract_year_mean_hpa = var_extract_year_mean / 100
        with open(dest_path + var + '_' + str(year) + '_mean_' + rcp + '.txt', 'w') as f:
            for ele in var_extract_year_mean_hpa.flatten():
                f.write(str(ele) + '\n')
    
    if var == "hurs" or  var == 'sfcWind':
        var_extract_year_mean = np.mean(var_extract_year, axis=0)
        with open(dest_path + var + '_' + str(year) + '_mean_' + rcp + '.txt', 'w') as f:
            for ele in var_extract_year_mean.flatten():
                f.write(str(ele) + '\n')
    
    if var == 'pr':
        var_extract_year_mean = np.mean(var_extract_year, axis=0)
        var_extract_year_mean_ml = var_extract_year_mean * 86400
        with open(dest_path + var + '_' + str(year) + '_mean_' + rcp + '.txt', 'w') as f:
            for ele in var_extract_year_mean_ml.flatten():
                f.write(str(ele) + '\n')


#extratct 2016 - 2030, rcp2.6, rcp4.5, rcp8.5
for var in vars:
    for year in range(2016, 2031):
        extratct(source_path, var, year, 'ssp126', dest_path) # rcps: ssp126, ssp245, ssp585
