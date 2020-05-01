#!/usr/bin/env python3

import csv
from pathlib import Path
from statistics import mean
import logging

# Files
data_dir = Path('/media/kshefchek/data')
big_file = data_dir / 'mac_season_four_2020-04-22.csv'
flowering_time = data_dir / 'days_gdd_to_flowering_season_4.csv'
flag_leaf_emergence_time = data_dir / 'days_gdd_to_flag_leaf_emergence_season_4.csv'
canopy_height = data_dir / 'canopy_height_time_series_season_4.csv'
aboveground_dry_biomass = data_dir / 'aboveground_dry_biomass_season_4.csv'
output = 'short_format_traits_season_4.tsv'

def main():

    multi_field = {
        'flowering_time': flowering_time,
        'flag_leaf_emergence_time': flag_leaf_emergence_time,
        'canopy_height': canopy_height,
        'aboveground_dry_biomass': aboveground_dry_biomass,
    }

    # We sum these values instead of avg
    binary_traits = {
        'leaf_desiccation_present',
        'lodging_present',
    }

    # {cultivar: {trait1: value, trait2: value, ...}, ...}
    data_map = {}

    with open(big_file, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, quotechar='"')

        for row in csvreader:
            cultivar = row['cultivar']
            trait = row['trait']
            value = row['mean']
            if trait not in get_fields() or trait in multi_field.keys():
                continue
            if cultivar in data_map:
                if trait in data_map[cultivar]:
                    data_map[cultivar][trait].append(float(value))
                else:
                    data_map[cultivar][trait] = [float(value)]
            else:
                data_map[cultivar] = {trait: [float(value)]}
                data_map[cultivar]['<Trait>'] = cultivar

    for trait, filepath in multi_field.items():
        with open(filepath, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile, quotechar='"')

            value_field = 'value'
            if 'canopy_height_time' in filepath.name:
                value_field = 'avg_canopy_height'

            for row in csvreader:
                cultivar = row['cultivar']
                value = row[value_field]

                # some odd parsing for aboveground_dry_biomass
                if value.startswith('PI') or value.startswith('Big_Kahuna'):
                    cultivar = row['value']
                    value = row['units']

                if trait in data_map[cultivar]:
                    data_map[cultivar][trait].append(float(value))
                else:
                    data_map[cultivar][trait] = [float(value)]

    # average values, convert to string, NaN for empty
    for cultivar, data in data_map.items():
        for col in get_fields():
            if col == '<Trait>':
                continue
            if col not in data:
                data[col] = "NaN"
            elif col in binary_traits:
                if len(col) > 1:
                    #logging.warning(
                    #    "More than one value for binary trait, %s %s" %
                    #    (cultivar, col)
                    #)

                    # Take the sum
                    data[col] = str(sum(data[col]))

                data[col] = str(data[col][0])
            else:
                data[col] = "%.4f" % mean(data[col])

    with open(output, 'w', newline='') as csv_outfile:
        csvwriter = csv.DictWriter(
            csv_outfile, fieldnames = get_fields(), delimiter='\t')
        csvwriter.writeheader()
        csvwriter.writerows([row for row in data_map.values()])


def get_fields():
    return [
        '<Trait>',
        # 'stalk_diameter_fixed_height',  # n = 18
        # 'SPAD_605',  # n = 6
        # 'leaf_temperature',  # n = 12
        'leaf_length',  # n = 351
        # 'light_intensity_PAR',  # n = 6
        'panicle_height',  # n = 70
        # 'flavonol_index',  # n = 4
        'panicle_count',  # n = 210
        # 'absorbance_940',  # n = 6
        'leaf_angle_beta',  # n = 351
        'flowering_time',  # n = 71
        #  'plant_basal_tiller_number',  # n = 18
        #  'Phi2',  # n = 6
        #  'leaf_thickness',  # n = 6
        #  'pitch',  # n = 6
        #  'SPAD_530',  # n = 6
        'aboveground_biomass_moisture',  # n = 317
        'leaf_angle_mean',  # n = 351
        'flag_leaf_emergence_time',  # n = 78
        'leaf_desiccation_present',  # n = 334
        'lodging_present',  # n = 323
        # 'SPAD_880',  # n = 6
        # 'proximal_air_temperature',  # n = 6
        # 'emergence_count',  # n = 35
        # 'relative_chlorophyll',  # n = 6
        # 'Fs',  # n = 6
        # 'FmPrime',  # n = 6
        'aboveground_fresh_biomass',  # n = 302
        # 'grain_stage_time',  # n = 65
        'aboveground_dry_biomass',  # n = 324
        # 'absorbance_530',  # n = 6
        # 'PhiNO',  # n = 6
        # 'leaf_angle_clamp_position',  # n = 6
        # 'qL',  # n = 6
        'harvest_lodging_rating',  # n = 330
        # 'anthocyanin_index',  # n = 4
        # 'absorbance_880',  # n = 6
        'dry_matter_fraction',  # n = 325
        # 'chlorophyll_index',  # n = 4
        'stand_count',  # n = 343
        # 'leaf_stomatal_conductance',  # n = 6
        # 'stalk_diameter_major_axis',  # n = 18
        # 'ambient_humidity',  # n = 6
        # 'SPAD_850',  # n = 6
        # 'SPAD_420',  # n = 6
        # 'stalk_diameter_minor_axis',  # n = 18
        # 'stem_elongated_internodes_number',  # n = 18
        # 'absorbance_730',  # n = 6
        # 'RFd',  # n = 6
        'panicle_volume',  # n = 210
        # 'PhiNPQ',  # n = 6
        # 'roll',  # n = 6
        # 'qP',  # n = 6
        # 'LEF',  # n = 6
        # 'SPAD_730',  # n = 6
        'panicle_surface_area',  # n = 210
        'leaf_width',  # n = 351
        'canopy_cover',  # n = 351
        'leaf_angle_chi',  # n = 351
        # 'seedling_emergence_rate',  # n = 35
        'leaf_angle_alpha',  # n = 351
        # 'ECSt',  # n = 6
        # 'NBI_nitrogen_balance_index',  # n = 4
        # 'FoPrime',  # n = 6
        # 'absorbance_650',  # n = 6
        # 'absorbance_420',  # n = 5
        # 'FvP/FmP',  # n = 6
        # 'SPAD_650',  # n = 6
        'planter_seed_drop',  #  n = 343
        # 'vH+',  # n = 6
        # 'absorbance_850',  # n = 6
        # 'leaf_temperature_differential',  # n = 6
        'canopy_height',  # n = 351
        # 'gH+',  # n = 6
        # 'absorbance_605',  # n = 6
        # 'NPQt',  # n = 6
    ]


if __name__ == "__main__":
    main()
