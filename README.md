# climateChange_tickVirusDiversity
Climate factors showed stronger effect on the virome of H. longicornis. The most important climatic factors associated with the virome of H. longicornis were high temperature, and low relative humidity/precipitation, which increased the diversity, mainly the evenness of vertebrate associated viruses. In this study, we developed a deep learning model for prediction tick virus diversity by six cliamte factors (future climate data were downloaded from climate model of CMIP6).
![alt text](https://github.com/patience111/climateChange_tickVirusDiversity/blob/main/pics/3.jpg)</br>
**climate variables**<br>
*tas* : Near-Surface Air Temperature<br>
*tasmax* : Daily Maximum Near-Surface Air Temperature<br>
*psl (Pa)*: Sea Level Pressure<br>
*pr (kg m-2 s-1)*: Precipitation<br>
*hurs (%)*: Near-Surface Relative Humidity<br>
*sfcWind (m s-1)*: Near-Surface Wind Speed<br>
<br>
**scripts**<br>
Three scripts are provided in "scripts" folder:<br>
***CMIP6_data_process.py:*** for processing climate data from climate model<br>
***train_model.py:*** for training model<br>
***prediction.py:*** for prediction via inputting the six climate factors introduced above<br>
<br>
**datasets**<br>
In datasets folder:<br>
**CNRM-CM6-1-HR_sourceData** provides the link for downloading the source data of the climate model<br>
extratced data (for predition) after run CMIP6_data_process.py are in folder **climate_extract_byCMIP6_data_process**<br>
latitude and longitude information is in **latitude_and_longitude** folder<br>
the data need for training model are in **for_model_training**<br>

