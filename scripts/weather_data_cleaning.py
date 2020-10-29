#!/usr/bin/env python
# coding: utf-8

import numpy as np
import os
import pandas as pd
import requests


def read_in_csv(url, folder_name, file_name):
    response = requests.get(url)
    with open(os.path.join(folder_name, file_name), 'wb') as f:
        f.write(response.content)
    df = pd.read_csv(folder_name + '/' + file_name)
    return df


def calculate_vpd(temp_avg, rh_avg):
    es = (6.11 * np.exp((2500000/461) * (1/273 - 1/(273 + temp_avg))))
    vpd = (((100 - rh_avg)/1000) * es)
    return vpd


def save_to_csv(list_of_dfs, list_of_output_filenames):
    for i,j in zip(list_of_dfs, list_of_output_filenames):
        i.to_csv(j, index=False)


s4_url = 'https://de.cyverse.org/dl/d/7D6C8FD6-EF77-437C-89E6-412EA8C3EEC6/mac_weather_station_raw_daily_2017.csv'
s6_url = 'https://de.cyverse.org/dl/d/233C21D5-1306-4028-9CF9-FF4AF0EAC405/mac_weather_station_raw_daily_2018.csv'
ksu_hourly_url = 'https://de.cyverse.org/dl/d/D80C07D7-5F68-4C86-B15A-9BAAF472D3A4/ksu_hourly_weather.csv'
ksu_daily_url = 'https://de.cyverse.org/dl/d/64805E3B-0460-4AA1-8D8A-2D7246E05B35/ashland_bottoms_daily_weather_2016.csv' 
clemson_temps_url = 'https://de.cyverse.org/dl/d/19836AB5-9223-4CBA-B56E-46272CACF5A3/clemson_temps_daily.csv'
clemson_rh_url = 'https://de.cyverse.org/dl/d/353F5386-4D88-45A9-A4F6-6FC66C64C7E8/clemson_rh_daily.csv'

s4_filename = "mac_weather_station_raw_daily_2017.csv"
s6_filename = "mac_weather_station_raw_daily_2018.csv"
ksu_hourly_filename = "ksu_hourly_weather.csv"
ksu_daily_filename = "ashland_bottoms_daily_weather_2016.csv" 
clemson_temps_filename = "clemson_temps_daily.csv"
clemson_rh_filename = "clemson_rh_daily.csv"

folder_name = 'data'

# MAC Season 4

s4_0 = read_in_csv(s4_url, folder_name=folder_name, file_name=s4_filename)
s4_1 = s4_0.loc[(s4_0.day_of_year >= 110) & (s4_0.day_of_year <= 259)]
season_4_date_range = pd.date_range(start='2017-04-20', end='2017-09-16')
s4_2 = s4_1.copy()
s4_2['date'] = season_4_date_range

s4_3 = s4_2.copy()
s4_3['daily_gdd'] = (((s4_3['air_temp_max'] + s4_3['air_temp_min'])) / 2) - 10
s4_4 = s4_3.copy()
s4_4['gdd'] = np.rint(np.cumsum(s4_4['daily_gdd']))
s4_5 = s4_4.drop(labels='daily_gdd', axis=1)

s4_6 = s4_5.copy()
s4_6['cum_precip'] = np.cumsum(s4_6.precip_total)

first_treatment_dates = pd.date_range(start='2017-08-01', end='2017-08-14')
second_treatment_dates = pd.date_range(start='2017-08-15', end='2017-08-30')
season_dates = s4_6.date.values

first_treatment_col = []
for d in season_dates:
    if d in first_treatment_dates:
        first_treatment_col.append(True)    
    else: 
        first_treatment_col.append(False)

second_treatment_col = []
for d in season_dates:
    if d in second_treatment_dates:
        second_treatment_col.append(True)
    else:
        second_treatment_col.append(False)

s4_7 = s4_6.copy()
s4_7['first_water_deficit_treatment'] = first_treatment_col
s4_7['second_water_deficit_treatment'] = second_treatment_col

s4_cols_to_keep = ['day_of_year', 'air_temp_max', 'air_temp_min', 'air_temp_mean', 'rh_max', 'rh_min', 'rh_mean', 'vpd_mean', 
                'precip_total', 'date', 'gdd', 'cum_precip', 'first_water_deficit_treatment', 
                'second_water_deficit_treatment']
s4_8 = pd.DataFrame(data=s4_7, columns=s4_cols_to_keep)

s4_new_col_names = ['day_of_year', 'temp_max', 'temp_min', 'temp_mean', 'rh_max', 'rh_min', 'rh_mean', 'vpd_mean',
                   'precip', 'date', 'gdd', 'precip_cumulative', 'first_water_deficit_treatment', 'second_water_deficit_treatment']
s4_9 = s4_8.copy()
s4_9.columns = s4_new_col_names

s4_new_col_order = ['date', 'day_of_year', 'temp_min', 'temp_max', 'temp_mean', 'gdd', 'rh_min', 'rh_max', 'rh_mean', 
                    'vpd_mean', 'precip', 'precip_cumulative', 'first_water_deficit_treatment', 'second_water_deficit_treatment']
s4_10 = s4_9[s4_new_col_order]

s4_cols_to_round = ['temp_min', 'temp_max', 'temp_mean', 'rh_min', 'rh_max', 'rh_mean', 'vpd_mean', 'precip',
                    'precip_cumulative']
s4_11 = s4_10.copy()
s4_11[s4_cols_to_round] = s4_10[s4_cols_to_round].round(2)


# MAC Season 6

s6_0 = read_in_csv(url=s6_url, folder_name=folder_name, file_name=s6_filename)
s6_1 = s6_0.loc[(s6_0.day_of_year >= 115) & (s6_0.day_of_year <= 213)]
season_6_date_range = pd.date_range(start='2018-04-25', end='2018-08-01')

s6_2 = s6_1.copy()
s6_2['date'] = season_6_date_range

s6_3 = s6_2.copy()
s6_3['daily_gdd'] = (((s6_3['air_temp_max'] + s6_3['air_temp_min'])) / 2) - 10

s6_4 = s6_3.copy()
s6_4['gdd'] = np.rint(np.cumsum(s6_4['daily_gdd']))

s6_5 = s6_4.drop(labels='daily_gdd', axis=1)

s6_6 = s6_5.copy()
s6_6['cum_precip'] = np.cumsum(s6_6.precip_total)

# For all seasons other than MAC Season 4, the water deficit treatment columns will be False. 

s6_7 = s6_6.copy()
s6_7['first_water_deficit_treatment'] = False
s6_7['second_water_deficit_treatment'] = False

s6_cols_to_keep = ['day_of_year', 'air_temp_max', 'air_temp_min', 'air_temp_mean', 'rh_max', 'rh_min', 'rh_mean', 'vpd_mean', 
                   'precip_total', 'date', 'gdd', 'cum_precip', 'first_water_deficit_treatment', 
                   'second_water_deficit_treatment']
s6_8 = pd.DataFrame(data=s6_7, columns=s6_cols_to_keep)

s6_new_col_names = ['day_of_year', 'temp_max', 'temp_min', 'temp_mean', 'rh_max', 'rh_min', 'rh_mean', 'vpd_mean',
                   'precip', 'date', 'gdd', 'precip_cumulative', 'first_water_deficit_treatment', 'second_water_deficit_treatment']

s6_9 = s6_8.copy()
s6_9.columns = s6_new_col_names

s6_new_col_order = ['date', 'day_of_year', 'temp_min', 'temp_max', 'temp_mean', 'gdd', 'rh_min', 'rh_max', 'rh_mean', 
                    'vpd_mean', 'precip', 'precip_cumulative', 'first_water_deficit_treatment', 'second_water_deficit_treatment']
s6_10 = s6_9[s6_new_col_order]

s6_cols_to_round = ['temp_min', 'temp_max', 'temp_mean', 'rh_min', 'rh_max', 'rh_mean', 'vpd_mean', 'precip',
                    'precip_cumulative']
s6_11 = s6_10.copy()
s6_11[s6_cols_to_round] = s6_10[s6_cols_to_round].round(2)


# # KSU Hourly - to calculate daily vapor pressure deficit mean values

kh_0 = read_in_csv(url=ksu_hourly_url, folder_name=folder_name, file_name=ksu_hourly_filename)
kh_1 = kh_0.iloc[2:]

kh_2 = kh_1.copy()
kh_2['AirTemperature'] = pd.to_numeric(kh_2['AirTemperature'], errors='coerce')

kh_3 = kh_2.copy()
kh_3['RelativeHumidity'] = pd.to_numeric(kh_3['RelativeHumidity'], errors='coerce')

kh_4 = kh_3.copy()
kh_4['vpd_mean'] = calculate_vpd(kh_4['AirTemperature'], kh_4['RelativeHumidity'])

kh_5 = kh_4.dropna(how='any', axis=0)

just_dates = []
for timestamp in kh_5['Timestamp'].values:
    date = timestamp[:10]
    just_dates.append(date)

kh_6 = kh_5.copy()
kh_6['date'] = just_dates

kh_7 = kh_6.groupby(['date'], as_index=False)['vpd_mean'].mean()

kh_8 = kh_6.groupby(['date']).agg(rh_min=('RelativeHumidity', 'min'), rh_max=('RelativeHumidity', 'max')).reset_index()

kh_9 = kh_7.merge(kh_8, how='left', left_on='date', right_on='date')


# KSU Daily

ksu_0 = read_in_csv(url=ksu_daily_url, folder_name=folder_name, file_name=ksu_daily_filename)
ksu_1 = ksu_0.iloc[2:]
ksu_2 = ksu_1.merge(kh_9, how='left', left_on='Timestamp', right_on='date')

ksu_numeric_cols = ['AirTemperature', 'AirTemperature.1', 'RelativeHumidity', 'Precipitation']
ksu_3 = ksu_2.copy()
ksu_3[ksu_numeric_cols] = ksu_3[ksu_numeric_cols].apply(pd.to_numeric, errors='coerce')

ksu_4 = ksu_3.copy()
ksu_4['daily_gdd'] = (((ksu_4['AirTemperature'] + ksu_4['AirTemperature.1'])) / 2) - 10

ksu_5 = ksu_4.copy()
ksu_5['gdd'] = np.rint(np.cumsum(ksu_5['daily_gdd']))
ksu_6 = ksu_5.drop(labels='daily_gdd', axis=1)

ksu_7 = ksu_6.copy()
ksu_7['precip_cumulative'] = np.cumsum(ksu_7['Precipitation'])

ksu_8 = ksu_7.copy()
ksu_8['first_water_deficit_treatment'] = False
ksu_8['second_water_deficit_treatment'] = False

ksu_cols_to_keep = ['AirTemperature', 'AirTemperature.1', 'RelativeHumidity', 'Precipitation', 'date', 'vpd_mean', 
                    'rh_min', 'rh_max', 'gdd', 'precip_cumulative', 'first_water_deficit_treatment', 
                    'second_water_deficit_treatment']
ksu_9 = pd.DataFrame(data=ksu_8, columns=ksu_cols_to_keep)

days_of_year = [i for i in range(169, 296)]
ksu_10 = ksu_9.copy()
ksu_10['day_of_year'] = days_of_year

ksu_11 = ksu_10.copy()
ksu_11['temp_mean'] = ksu_11[['AirTemperature', 'AirTemperature.1']].mean(axis=1)

ksu_new_col_names = ['temp_max', 'temp_min', 'rh_mean', 'precip', 'date', 'vpd_mean', 'rh_min', 'rh_max', 'gdd',
                    'precip_cumulative', 'first_water_deficit_treatment', 'second_water_deficit_treatment',
                    'day_of_year', 'temp_mean']
ksu_12 = ksu_11.copy()
ksu_12.columns = ksu_new_col_names

ksu_new_col_order = ['date', 'day_of_year', 'temp_min', 'temp_max', 'temp_mean', 'gdd', 'rh_min', 'rh_max', 'rh_mean', 
                    'vpd_mean', 'precip', 'precip_cumulative', 'first_water_deficit_treatment', 'second_water_deficit_treatment']
ksu_13 = ksu_12[ksu_new_col_order]

ksu_cols_to_round = ['temp_min', 'temp_max', 'temp_mean', 'rh_min', 'rh_max', 'rh_mean', 'vpd_mean', 'precip',
                    'precip_cumulative']
ksu_14 = ksu_13.copy()
ksu_14[ksu_cols_to_round] = ksu_14[ksu_cols_to_round].round(2)


# Clemson

clemson_0 = read_in_csv(url=clemson_temps_url, folder_name=folder_name, file_name=clemson_temps_filename)
clemson_1 = read_in_csv(url=clemson_rh_url, folder_name=folder_name, file_name=clemson_rh_filename)

dates_2014 = clemson_1['DateTime'].values
clemson_2 = clemson_0.copy()
clemson_2['date'] = dates_2014

clemson_3 = clemson_2.merge(clemson_1, how='left', left_on='date', right_on='DateTime')
clemson_4 = clemson_3.loc[(clemson_3['yday'] >= 126) & (clemson_3['yday'] <= 288)]

clemson_5 = clemson_4.copy()
clemson_5['daily_gdd'] = (((clemson_5['tmax (deg c)'] + clemson_5['tmin (deg c)'])) / 2) - 10

clemson_6 = clemson_5.copy()
clemson_6['gdd'] = np.rint(np.cumsum(clemson_6['daily_gdd']))
clemson_7 = clemson_6.drop(labels='daily_gdd', axis=1)

clemson_8 = clemson_7.copy()
clemson_8['precip_cumulative'] = np.cumsum(clemson_8['prcp (mm/day)'])

clemson_9 = clemson_8.copy()
clemson_9['first_water_deficit_treatment'] = False
clemson_9['second_water_deficit_treatment'] = False

clemson_cols_to_keep = ['yday', 'prcp (mm/day)', 'tmax (deg c)', 'tmin (deg c)', 'date', '(%) Min Rel. Humidity (gridMET), -79.7370E,34.2890N ,2014-01-01 to 2014-12-31', 
                        '(%) Max Rel. Humidity (gridMET), -79.7370E,34.2890N ,2014-01-01 to 2014-12-31', 'gdd', 
                        'precip_cumulative', 'first_water_deficit_treatment', 'second_water_deficit_treatment']
clemson_10 = pd.DataFrame(data=clemson_9, columns=clemson_cols_to_keep)

clemson_11 = clemson_10.rename({'yday': 'day_of_year', 'prcp (mm/day)': 'precip', 'tmax (deg c)': 'temp_max', 
                                'tmin (deg c)': 'temp_min', '(%) Min Rel. Humidity (gridMET), -79.7370E,34.2890N ,2014-01-01 to 2014-12-31': 'rh_min', 
                                '(%) Max Rel. Humidity (gridMET), -79.7370E,34.2890N ,2014-01-01 to 2014-12-31': 'rh_max',}, axis=1)

clemson_12 = clemson_11.copy()
clemson_12['temp_mean'] = clemson_12[['temp_max', 'temp_min']].mean(axis=1)
clemson_13 = clemson_12.copy()
clemson_13['rh_mean'] = clemson_13[['rh_max', 'rh_min']].mean(axis=1)
clemson_14 = clemson_13.copy()
clemson_14['vpd_mean'] = calculate_vpd(clemson_14['temp_mean'], clemson_14['rh_mean'])

clemson_new_col_order = ['date', 'day_of_year', 'temp_min', 'temp_max', 'temp_mean', 'gdd', 'rh_min', 'rh_max', 'rh_mean', 
                         'vpd_mean', 'precip', 'precip_cumulative', 'first_water_deficit_treatment', 'second_water_deficit_treatment']
clemson_15 = clemson_14[clemson_new_col_order]

clemson_cols_to_round = ['temp_min', 'temp_max', 'temp_mean', 'rh_min', 'rh_max', 'rh_mean', 'vpd_mean', 'precip', 
                         'precip_cumulative']
clemson_16 = clemson_15.copy()
clemson_16[clemson_cols_to_round] = clemson_16[clemson_cols_to_round].round(2)


list_of_dfs = [s4_11, s6_11, ksu_14, clemson_16]
list_of_output_filenames = ['mac_season_4_weather.csv', 'mac_season_6_weather.csv', 'ksu_weather.csv', 'clemson_weather.csv']

save_to_csv(list_of_dfs, list_of_output_filenames)

