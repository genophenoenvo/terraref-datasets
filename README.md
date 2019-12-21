# README Metadata

### [Structured metadata]

## General Information
### I. Title: TERRA-REF Seasons 4 and 6 Machine Learning Dataset
### II. Research Group
* University of Arizona 
* Tufts University
* Michigan State University
* Oregon State University
* Utrecht University
### III. Date Ranges of Data Collection
* Season 4: 2017-04-20 (planting date) - [ ] 
* Season 6: 2018-04-25 (planting date) - [ ]
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
* weather_station_season_4_timestamp.csv
#### B. Phenotypes
* canopy_heights_end_of_season_4_timestamp.csv
* canopy_heights_season_4_by_date_timestamp.csv
* tall_format_traits_season_4_timestamp.csv

### II. MAC Season 6
#### A. Environmental 
* weather_station_season_6_timestamp.csv
#### B. Phenotypes
* tall_format_traits_season_6_timestamp.csv

## Sharing and Access Information
TERRA-REF Data Use [Policy](https://docs.terraref.org/user-manual/data-use-policy)

## Methodological Information

### I. Data Collected By: 
### II. Data Collection Methods:
* [Manual Field Data Protocols](https://docs.terraref.org/protocols/manual-field-data-protocols)
* [protocols.io]
* Canopy Height
    * 3D scanner to 98th quantile height
    * manual
* Aboveground Dry Biomass
* Light Intensity PAR - MultispeQ v1.0 field measurements of fluorescence-based and absorbance-based parameters
* Seedling Emergence Rate 
* Flag Leaf Emergence Time
* Flowering Time
### III. Derived Datasets Curated By: Emily J. Cain, University of Arizona
* Trait data queried from [betydb](https://terraref.ncsa.illinois.edu/bety/) using this [tutorial](https://terraref.github.io/tutorials/accessing-trait-data-in-r.html)
* Raw weather data downloaded from [MAC Weather Station](https://cals.arizona.edu/azmet/06.htm)
### IV. Data Transformation
* Python code for data cleaning and transformation can be found within Jupyter notebooks [here] 
* In-browser executable notebooks: [ ]

## Data-specific Information

### I. Season Dates
#### A. Planting Date for Season 4: 2017-04-20
#### B. Harvest Dates for Season 4
* Day One: 2017-09-11
* Day Two: 2017-09-12
* Day Three: 2017-09-15
* Day Four: 2017-09-16
#### C. Planting Date for Season 6: 2018-04-25
#### D. Harvest Dates for Season 6
* Day One: 2018-07-31
* Day Two: 2018-08-01
### II. Phenotypes - Units
* Canopy Height - cm
* Aboveground Dry Biomass - kg / ha
* Light Intensity PAR 
* Seedling Emergence Rate
* Flag Leaf Emergence Time - days
* Flowering Time - days
### IV. Environmental - Units
* Temperature - Degrees in Celsius



## References
[Cornell Guide to Writing README style Metadata](https://data.research.cornell.edu/content/readme#fileoverview)

## Related Information
* TERRA-REF [main](https://terraref.org/) 
* TERRA-REF [docs](https://docs.terraref.org/)
* TERRA-REF [tutorials](https://terraref.github.io/tutorials/index.html)
* [GenoPhenoEnvo](https://genophenoenvo.github.io/)
