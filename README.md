# README Metadata

### [Structured metadata]

## General Information
### I. Title: TERRA-REF Seasons 4 and 6 Machine Learning Dataset

Phenotype, genotype, and environmental data for _Sorghum bicolor_

### II. Research Group
* Michigan State University
* Oregon State University
* Tufts University
* University of Arizona 
* Utrecht University
### III. Date Ranges of Data Collection
* **Season 4**: 2017-04-20 (planting date) - 2017-09-16 (last day of harvest) 
* **Season 6**: 2018-04-25 (planting date) - 2018-08-01 (last day of harvest)
### IV. Geographic Location of Data Collection 
* Maricopa Agricultural Center, Maricopa, AZ, 85138, USA
* Pinal County
* Elevation : 362 meters
* Coordinates : 33.068941, -111.972244
* USGS Map : Sacaton Butte 7.5' Series Map

## Data and File Overview

* [Google Drive Directory](https://drive.google.com/drive/folders/1B9Hmj2Xwu0J9arTfhFiFZqkEktSeag63?usp=sharing)

### I. MAC Season 4
#### A. Environmental
* **weather_station_season_4_timestamp.csv**
    #### Columns - information from [Weather Station](https://cals.arizona.edu/azmet/raw2003.htm)
    * date: year-month-day format
    * day of year - information from [NOAA](https://www.esrl.noaa.gov/gmd/grad/neubrew/Calendar.jsp?view=DOY&year=2017&col=4)
    * air_temp_max: degrees, Celsius
    * air_temp_min: degrees, Celsius
    * air_temp_mean: degrees, Celsius
    * rh_max: relative humidity, percentage
    * rh_min: relative humidity, percentage
    * rh_mean: relative humidity, percentage
    * precip_total: precipitation total, mm
    * wind_speed_mean: m/s, meters per second
    * wind_vector_magnitude: m/s, meters per second, calculation using direction and speed
    * wind_vector_direction: degrees
        * wind blowing from the north = 0&deg;/360&deg;
        * wind blowing from the east = 90&deg;
        * wind blowing from the south = 180&deg;
        * wind blowing from the west = 270&deg;
    * wind_direction_std: wind direction standard deviation, degrees
    * max_wind_speed: m/s, meters per second
    * gdd: cumulative growing degree days, using a base/threshold temperature of 10&deg;C 
    * cum_precip: cumulative precipitation, mm
#### B. Phenotypes
* **canopy_heights_end_of_season_4_timestamp.csv**
    #### Columns
    * sitename: location-based identifier, MAC Field Scanner Season 4 Range x Column y
    * range: extracted from sitename
    * column: extracted from sitename
    * lat: latitude
    * lon: longitude
    * date: year-month-day format
    * cultivar: sorghum variety
    * canopy_height: cm
        * Note: the latest measurement taken in the season may not necessarily be the end-of-season or maximum canopy height for that sitename and cultivar

* **canopy_heights_season_4_by_date_timestamp.csv**
    #### Columns
    * date: year-month-day format
    * sitename: location-based identifier, MAC Field Scanner Season 4 Range x Column y
    * range: extracted from sitename
    * column: extracted from sitename
    * lat: latitude
    * lon: longitude
    * cultivar: sorghum variety
    * canopy_height: cm

* **tall_format_traits_season_4_timestamp.csv**
    #### Columns
    * date: year-month-day format
    * sitename: location-based identifier, MAC Field Scanner Season 4 Range x Column y
    * range: extracted from sitename
    * column: extracted from sitename
    * lat: latitude
    * lon: longitude
    * cultivar: sorghum variety
    * trait: value
        * flowering_time: days from planting to flowering
        * flag_leaf_emergence: days from planting to flag leaf emergence
        * light_intensity_PAR: photosynthetically active radiation, fraction of incoming light (400 - 700 nm) which can be intercepted by leaf
        *  aboveground_dry_biomass: kg/ha, kilogram per hectare, whole aboveground biomass at harvest

* **days_gdd_to_flag_leaf_season_4_timestamp.csv**
    #### Columns
    * sitename: location-based identifier, MAC Field Scanner Season 4 Range x Column y
    * range: extracted from sitename
    * column: extracted from sitename
    * cultivar: sorghum variety
    * date_of_flag_leaf_emergence: year-month-day format
    * days_to_flag_leaf_emergence: days from planting to flag leaf emergence
    * gdd_to_flag_leaf_emergence: cumulative growing degree days to flag leaf emergence

* **days_gdd_to_flowering_season_4_timestamp.csv**
    #### Columns
    * sitename: location-based identifier, MAC Field Scanner Season 4 Range x Column y
    * range: extracted from sitename
    * column: extracted from sitename
    * cultivar: sorghum variety
    * date_of_flowering: year-month-day format
    * days_to_flowering: days from planting to flowering
    * gdd_to_flowering: cumulative growing degree days to flowering

### II. MAC Season 6
#### A. Environmental 
* **weather_station_season_6_timestamp.csv**
    #### Columns - information from [Weather Station](https://cals.arizona.edu/azmet/raw2003.htm)
    * date: year-month-day format
    * day of year - information from [NOAA](https://www.esrl.noaa.gov/gmd/grad/neubrew/Calendar.jsp?view=DOY&year=2017&col=4)
    * air_temp_max: degrees, Celsius
    * air_temp_min: degrees, Celsius
    * air_temp_mean: degrees, Celsius
    * rh_max: relative humidity, percentage
    * rh_min: relative humidity, percentage
    * rh_mean: relative humidity, percentage
    * precip_total: precipitation total, mm
    * wind_speed_mean: m/s, meters per second
    * wind_vec_mag: wind vector magnitude in m/s, meters per second, calculation using direction and speed
    * wind_vec_dir: wind vector direction, degrees
        * wind blowing from the north = 0&deg;/360&deg;
        * wind blowing from the east = 90&deg;
        * wind blowing from the south = 180&deg;
        * wind blowing from the west = 270&deg;
    * wind_dir_std: wind direction standard deviation, degrees
    * max_wind_speed: m/s, meters per second
    * gdd: cumulative growing degree days, using a base/threshold temperature of 10&deg;C 
    * cum_precip: cumulative precipitation, mm
#### B. Phenotypes
* **tall_format_traits_season_6_timestamp.csv**
    #### Columns
    * date: year-month-day format
    * sitename: location-based identifier, MAC Field Scanner Season 4 Range x Column y
    * range: extracted from sitename
    * column: extracted from sitename
    * lat: latitude
    * lon: longitude
    * cultivar: sorghum variety
    * trait: value
        * canopy_height: cm
        * aboveground_dry_biomass: kg/ha, kilogram per hectare, whole aboveground biomass at harvest 

## Sharing and Access Information
TERRA-REF Data Use [Policy](https://docs.terraref.org/user-manual/data-use-policy)

## Methodological Information

### I. Data Collected By: 
### II. Data Collection Methods:
* [Manual Field Data Protocols](https://docs.terraref.org/protocols/manual-field-data-protocols) from TERRA-REF docs

### III. Data Curation: 

* Trait data queried from [betydb](https://terraref.ncsa.illinois.edu/bety/) in `R` using this [tutorial](https://terraref.github.io/tutorials/accessing-trait-data-in-r.html)
* Raw weather data downloaded from [MAC Weather Station](https://cals.arizona.edu/azmet/06.htm)
* Geostreams weather data queried from [Clowder](https://pecanproject.github.io/modules/data.atmosphere/docs/reference/download.Geostreams.html) in `R` using this [tutorial](https://terraref.github.io/tutorials/accessing-weather-data-in-r.html)
### IV. Data Transformation
* Python code for data cleaning and transformation can be found within Jupyter notebooks [here] 
* In-browser executable notebooks: [ ]

## Data-specific Information

Please see [Google Drive](https://drive.google.com/drive/folders/1B9Hmj2Xwu0J9arTfhFiFZqkEktSeag63?usp=sharing) for ontology annotations

### Season 4

#### Dates of Managements
Please see metadata [notes](https://terraref.ncsa.illinois.edu/bety/api/v1/managements) for more details

* **Tillage**: 2017-04-10, 2017-04-11
* **Planting**: 2017-04-20
* **Harvest**: 2017-09-11, 2017-09-12, 2017-09-15, 2017-09-16
* **Plant thinning**: 2017-05-10, 2017-05-11, 2017-05-12
* **Pesticide**: 2017-05-12
* **Weed Control**
    * Mechanical weed control: 2017-05-15
    * Manual weed removal: 2017-05-18, 2017-05-19, 2017-05-26
* **Fertilizer Treatments**
    * Pre-planting: 2017-04-13
    * Through drip irrigation: 2017-06-11, 2017-06-22, 2017-07-18
* **Irrigation**
    * First sprinkler irrigation after planting: 2017-04-21
    * Final sprinkler irrigation to facilitate seedling emergence: 2017-05-04
    * Final full-field: 2017-07-30
    * Irrigation terminated across whole field: 2017-08-30
    * Water-deficit experiments: 2017-08-01, 2017-08-15

### Season 6
#### Dates of Managements
Please see metadata [notes](https://terraref.ncsa.illinois.edu/bety/api/v1/managements) for more details

* **Planting**: 2018-04-25
* **Soil moisture probes**: 2018-04-26
* **First sprinkler irrigation**: 2018-04-26
* **Plant thinning**: 2018-05-16
* **Pesticide**: 2018-05-21
* **Fertilizer treatment through drip irrigation**: 2018-06-15
* **Harvest**: 2018-07-31, 2018-08-01
    

## References
[Cornell Guide to Writing README style Metadata](https://data.research.cornell.edu/content/readme#fileoverview)

## Related Sites
* TERRA-REF [main](https://terraref.org/) 
* TERRA-REF [docs](https://docs.terraref.org/)
* TERRA-REF [tutorials](https://terraref.github.io/tutorials/index.html)
* [GenoPhenoEnvo](https://genophenoenvo.github.io/)
