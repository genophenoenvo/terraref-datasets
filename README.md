# TERRA-REF and related data for GenoPhenoEnvo research project


## Data Use, Licenses, and Preferred Citations

* TERRA-REF data from Season 4 and 6 contained in this repository are licensed under CC-0. Please cite LeBauer et al 2020 when using these data.
* KSU data is unpublished and should not be reused without permission from Geoff Morris.
* Clemson data are from Brenton et al (2016)
* This repository are licensed under MIT (see file LICENSE).

LeBauer, David et al. (2020), Data From: TERRA-REF, An open reference data set from high resolution genomics, phenomics, and imaging sensors, v6, Dryad, Dataset, https://doi.org/10.5061/dryad.4b8gtht99

Brenton, Zachary W., et al. "A genomic resource for the development, improvement, and exploitation of sorghum for bioenergy." Genetics 204.1 (2016): 21-33. https://doi.org/10.1534/genetics.115.183947

## Corresponding Author

David LeBauer, University of Arizona, dlebauer@arizona.edu

## Summary 
This repository contains source code for accessing and curating [TERRA-REF](https://terraref.org/bety/) data used to support the [GenoPhenoEnvo](https://github.com/genophenoenvo) project and machine learning research. This repository supports one of our goals to provide open data and reproducible code in order to follow [FAIR](https://www.go-fair.org/fair-principles/) data principles and contribute to open science.

This repository focuses on _Sorghum bicolor_ trait data collected from four experiments and the associated weather data for those locations, listed below.

- Maricopa Agricultural Center, University of Arizona, Season 4
    - Coordinates: 33.069, -111.972
    - Elevation: 362 meters
    - Planting: 2017-04-20, Day 110
    - Last Day of Harvest: 2017-09-16, Day 259
- Maricopa Agricultural Center, University of Arizona, Season 6
    - Coordinates: 33.068941, -111.972244
    - Elevation: 362 meters
    - Planting: 2018-04-25, Day 115
    - Harvest: 2018-08-01, Day 213
- Kansas State University, Ashland Bottoms
    - Coordinates: 39.126, -96.677
    - Elevation: 325 meters
    - Planting: 2016-06-17, Day 169
    - Harvest: 2016-10-21, Day 295
- Clemson University Pee Dee Research and Education Center, South Carolina
    - Coordinates: 34.289, -79.737 
    - Elevation: 42 meters
    - Planting: 2014-05-06, Day 126
    - Latest date in Clemson trait data: 2014-10-15, Day 288


## Trait Data

Trait data prepared for this analysis can be downloaded in `.csv` format from CyVerse.


**MAC Season 4**
- [`mac_season_4_aboveground_dry_biomass.csv`](https://de.cyverse.org/dl/d/015BB53B-0B1D-4653-95B7-2FF9A04A0C1F/mac_season_4_aboveground_dry_biomass.csv)
- [`mac_season_4_canopy_height_manual.csv`](https://de.cyverse.org/dl/d/41DC8F3F-A72F-4EB9-A1C0-9352DCAAFB75/mac_season_4_canopy_height_manual.csv)
- [`mac_season_4_days_gdd_to_flowering.csv`](https://de.cyverse.org/dl/d/BFF25218-4D3B-4A5A-9C05-A232255E12F6/mac_season_4_days_gdd_to_flowering.csv)
- [`mac_season_4_days_gdd_to_flag_leaf_emergence.csv`](https://de.cyverse.org/dl/d/8F2835BF-48C9-418F-9BDA-66E66F1B34BD/mac_season_4_days_gdd_to_flag_leaf_emergence.csv)

**MAC Season 6**
- [`mac_season_6_aboveground_dry_biomass.csv`](https://de.cyverse.org/dl/d/C1F477C1-63A7-4FE8-991F-1CA4DA0A69ED/mac_season_6_aboveground_dry_biomass.csv)
- [`mac_season_6_canopy_height_sensor.csv`](https://de.cyverse.org/dl/d/BEC5B164-EC6F-45E5-8E64-FC0E63D9A059/mac_season_6_canopy_height_sensor.csv)

**KSU**
- [`ksu_canopy_heights.csv`](https://de.cyverse.org/dl/d/52A1FDEE-C95F-4BC7-8001-027A6ED2AA09/ksu_canopy_height.csv)
- [`ksu_days_gdd_to_flowering.csv`](https://de.cyverse.org/dl/d/88020A6C-6430-4B1E-BFDC-69C42E7E335C/ksu_days_gdd_to_flowering.csv)

**Clemson**
- [`clemson_days_gdd_to_flowering.csv`](https://de.cyverse.org/dl/d/A463AD0E-7BB5-451F-83AE-DAFD7939616C/clemson_days_gdd_to_flowering.csv)
- [`clemson_plant_height.csv`](https://de.cyverse.org/dl/d/A3E4CE55-C615-451A-B71E-49A92E17500F/clemson_plant_height.csv)
- [`clemson_aboveground_dry_biomass.csv`](https://de.cyverse.org/dl/d/6814725D-C10F-45D3-8148-A2A598A2AB91/clemson_aboveground_dry_biomass.csv)



### Content of trait data CSV files

These tables have the following structure ...


### Data Processing

The following traits and units were selected from the raw data for analysis, with the sites that collected those phenotypes. The calculation used for growing degree days (gdd) can be found [here](https://mrcc.illinois.edu/gismaps/info/gddinfo.htm#:~:text=To%20calculate%20GDDs%2C%20you%20must,Degree%20Day%20value%20is%20zero).

- `days_to_flowering`: `days`, `gdd`
    - **MAC Season 4, KSU, Clemson**
- `days_to_flag_leaf_emergence`: `days`, `gdd`
    - **MAC Season 4**
- `canopy_height`: `cm`
    - **MAC Season 4, MAC Season 6, KSU, Clemson**
- `aboveground_dry_biomass`: `kg/ha`
    - **MAC Season 4, MAC Season 6, Clemson**

#### The following Jupyter notebooks contain code to process the raw trait data

- [`mac_season_4_data_cleaning.ipynb`](https://de.cyverse.org/dl/d/AA24FF46-8521-473F-9F82-BF08385053B4/mac_season_4_data_cleaning.ipynb)
- [`mac_season_6_data_cleaning.ipynb`](https://de.cyverse.org/dl/d/ABBF955A-43ED-4811-8554-3C0F2C66A9AE/mac_season_6_data_cleaning.ipynb)
- [`ksu_data_cleaning.ipynb`](https://de.cyverse.org/dl/d/CE4BF004-1C6C-4954-A93E-7A388EC846D2/ksu_data_cleaning.ipynb)
- [`clemson_data_cleaning.ipynb`](https://de.cyverse.org/dl/d/C70855EF-37B6-4DFE-98B3-02B8904E5127/clemson_data_cleaning.ipynb)


## Weather Data

Contains the weather data during season dates for sorghum experiments at these locations

### Parameters and Units

- Date: YYYY-MM-DD format
- Day of year
- Minimum temperature: Celsius
- Maximum temperature: Celsius
- Mean temperature: Celsius
- Accumulated growing degree days (gdd): heat units
    - 10 degrees Celsius is base temperature for sorghum
    - Daily gdd value = ``((max temp + min temp) / 2) - 10 (base temperature)``
    - Accumulated growing degree days = cumulative sum of daily gdd values
- Minimum relative humidity: percentage
- Maximum relative humidity: percentage
- Mean relative humidity: percentage
- Vapor pressure deficit: Kilopascals
    ```
    es = (6.11 * np.exp((2500000/461) * (1/273 - 1/(273 + temp_avg))))
    vpd = (((100 - rh_avg)/1000) * es)
    ```
- Precipitation: millimeters
- Cumulative precipitation: millimeters
- First water deficit treatment: boolean value
    - `True` values only found in MAC Season 4
- Second water deficit treatment: boolean value
    - `True` values only found in MAC Season 4

Information about MAC season 4 water deficit treatments can be found [here](https://terraref.org/bety/api/v1/experiments?name=~MAC+Season+4:+All+BAP+With+Late+Season+Drought)


### Weather data sources

- [Maricopa (Arizona) Agricultural Center](https://cals.arizona.edu/azmet/06.htm)
- [Kansas Mesonet](http://mesonet.k-state.edu/)
- NASA [Daymet](https://daymet.ornl.gov/) - can search by coordinates
- [Climate Engine](http://climateengine.org/data) - can search by coordinates

### Data Processing

- Weather data that could not be found in all four seasons were dropped during processing, but can be accessed in the raw data 
- The Python3 code used to process weather data can be found in `src/weather_data_cleaning.py`. This script will produce the following output data: 
    - `mac_season_4_weather.csv`
    - `mac_season_6_weather.csv`
    - `ksu_weather.csv`
    - `clemson_weather.csv`

## Folder and file structure

---

Project Organization
------------

### Data on CyVerse

### Code in Repository



TODO: what does this refer to?

    ├── LICENSE
    |
    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    |    
    ├── scripts             <- Source code for use in this project.


