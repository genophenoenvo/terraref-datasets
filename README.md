# [TERRA-REF Data](https://www.terraref.org/)

This repository contains source code for accessing and curating [TERRA-REF](https://terraref.ncsa.illinois.edu/bety/) data used to support the [GenoPhenoEnvo](https://github.com/genophenoenvo) project and machine learning research. This repository supports one of our goals to provide open data and reproducible code in order to follow [FAIR](https://www.go-fair.org/fair-principles/) data principles and contribute to open science.

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
    
### Licenses
TERRA-REF data and other documents are licensed under CC-By. All software is licensed under MIT.

### Contacts
Please contact these individuals with any questions

- Todd Mockler, Project/Genomics Lead (email: tmockler@danforthcenter.org)
- David LeBauer, Computing Pipeline Lead (email: dlebauer@email.arizona.edu)
- Nadia Shakoor, Project Director (email: nshakoor@danforthcenter.org)

### Citations

#### Dryad Data 

Maricopa Agricultural Center (MAC) data from the TERRA-REF project seasons four and six have been published with Dryad and can be downloaded [here](https://doi.org/10.5061/dryad.4b8gtht99).

**LeBauer, David et al. (2020), Data From: TERRA-REF, An open reference data set from high resolution genomics, phenomics, and imaging sensors, v6, Dryad, Dataset, https://doi.org/10.5061/dryad.4b8gtht99**

---

### A. Trait Data

Raw trait data can be accessed in several ways:
- [TERRA-REF, An open reference data set from high resolution genomics, phenomics, and imaging sensors](https://doi.org/10.5061/dryad.4b8gtht99)
    - Data paper for MAC seasons 4 and 6
    - **Citation**
LeBauer, David et al. (2020), Data From: TERRA-REF, An open reference data set from high resolution genomics, phenomics, and imaging sensors, Dryad, Dataset, https://doi.org/10.5061/dryad.4b8gtht99
- Connecting to betydb directly via Docker using [these instructions](https://github.com/terraref/brapi)
- The `R` `traits` [package](https://docs.ropensci.org/traits/)
- Downloading data in `.csv` format from CyVerse
    - [MAC Season 4](https://de.cyverse.org/dl/d/D3168AC5-82BE-436E-B8B5-AB8DD78CAF28/mac_season_four_2020-04-22.csv)
    - [MAC Season 6](https://de.cyverse.org/dl/d/C14BF1DE-9FD3-4559-AC3E-7858CE392E3A/mac_season_six_2020-04-22.csv)
    - [KSU](https://de.cyverse.org/dl/d/018B11DA-28E7-46B8-88D9-4481904FFBA7/ksu_data_2020-06-11.csv) 
    - [Clemson](https://de.cyverse.org/dl/d/E5B8AC50-B1D1-4254-932D-F04CA0D1DF3E/clemson_data_2020-06-01.csv)
- Querying betydb API endpoints
    - `Managements` [example](https://terraref.ncsa.illinois.edu/bety/api/v1/managements?)

#### Raw trait data contain the following columns. If a column has only one value in the dataset, that will be indicated after the column name and colon.

- `checked`: `0`
- `result_type`: `traits`
- `id`
- `citation_id`
- `site_id`
- `sitename`
- `city`
- `lat` 
- `lon`
- `scientificname`: `Sorghum bicolor`
- `commonname`: `sorghum`
- `genus`: `Sorghum`
- `species_id`: `2588`
- `cultivar_id`
- `author`
- `citation_year`
- `treatment`
- `date`
- `time`
- `raw_date`
- `month`
- `year`
- `dateloc`
- `trait`
- `trait_description`
- `mean` (the value for the trait)
- `units` 
- `n`: `NA`
- `statname`: `null`
- `stat`: `NA`
- `notes`
- `access_level` (used before the data was published)
- `cultivar`
- `entity`: `NA`
- `method_name`
- `method_description` (not in every dataset)
- `view_url`
- `edit_url`

#### The following traits and units were selected from the raw data for analysis, with the sites that collected those phenotypes. The calculation used for growing degree days (gdd) can be found [here](https://mrcc.illinois.edu/gismaps/info/gddinfo.htm#:~:text=To%20calculate%20GDDs%2C%20you%20must,Degree%20Day%20value%20is%20zero).

- `days_to_flowering`: `days`, `gdd`
    - **MAC Season 4, KSU, Clemson**
- `days_to_flag_leaf_emergence`: `days`, `gdd`
    - **MAC Season 4**
- `canopy_height`: `cm`
    - **MAC Season 4, MAC Season 6, KSU, Clemson**
- `aboveground_dry_biomass`: `kg/ha`
    - **MAC Season 4, MAC Season 6, Clemson**

#### Table comparing cultivars with available traits and genomic data

- < name of file >

#### The following Jupyter notebooks contain code to process the raw trait data

- `mac_season_4_data_cleaning.ipynb`
- `mac_season_6_data_cleaning.ipynb`
- `ksu_data_cleaning.ipynb`
- `clemson_data_cleaning.ipynb`

---

### B. Weather Data

Contains the weather data during season dates for sorghum experiments at these locations

#### Parameters and Units

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

Information about MAC season 4 water deficit treatments can be found [here](https://terraref.ncsa.illinois.edu/bety/api/v1/experiments?name=~MAC+Season+4:+All+BAP+With+Late+Season+Drought)

#### Raw weather data CyVerse downloads

These urls will start an **automatic** download, which were used in the weather data cleaning code

- [MAC season 4 weather](https://de.cyverse.org/dl/d/7D6C8FD6-EF77-437C-89E6-412EA8C3EEC6/mac_weather_station_raw_daily_2017.csv)
- [MAC season 6 weather](https://de.cyverse.org/dl/d/233C21D5-1306-4028-9CF9-FF4AF0EAC405/mac_weather_station_raw_daily_2018.csv)
- [KSU hourly weather](https://de.cyverse.org/dl/d/D80C07D7-5F68-4C86-B15A-9BAAF472D3A4/ksu_hourly_weather.csv)
- [KSU daily weather](https://de.cyverse.org/dl/d/64805E3B-0460-4AA1-8D8A-2D7246E05B35/ashland_bottoms_daily_weather_2016.csv)
- [Clemson daily temperatures](https://de.cyverse.org/dl/d/19836AB5-9223-4CBA-B56E-46272CACF5A3/clemson_temps_daily.csv)
- [Clemson daily relative humidity](https://de.cyverse.org/dl/d/353F5386-4D88-45A9-A4F6-6FC66C64C7E8/clemson_rh_daily.csv)

#### Raw weather data sources
- [Maricopa (Arizona) Agricultural Center](https://cals.arizona.edu/azmet/06.htm)
- [Kansas Mesonet](http://mesonet.k-state.edu/)
- NASA [Daymet](https://daymet.ornl.gov/) - can search by coordinates
- [Climate Engine](http://climateengine.org/data) - can search by coordinates

#### Data Processing

- Weather data that could not be found in all four seasons were dropped during processing, but can be accessed in the raw data 
- The Python3 code used to process weather data can be found in `src/weather_data_cleaning.py`. This script will produce the following output data: 
    - `mac_season_4_weather.csv`
    - `mac_season_6_weather.csv`
    - `ksu_weather.csv`
    - `clemson_weather.csv`

#### Folder and file structure

---

Project Organization
------------

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
    ├── src                <- Source code for use in this project.

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
