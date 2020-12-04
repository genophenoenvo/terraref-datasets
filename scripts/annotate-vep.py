#!/usr/bin/env python3

"""
Annotate VEP hits with GO terms using the Monarch API, which queries the
Amigo solr instance - http://amigo.geneontology.org/amigo

Note there is an official VEP plugin to do this:
https://uswest.ensembl.org/info/docs/tools/vep/script/vep_plugins.html
but this does not return any GO terms

TODO replace the go api portion with calling Gramene
https://www.gramene.org/

In lieu of a requirements file:
python3.7 -m venv venv
source venv/bin/activate
pip install requests
"""

import csv
from typing import List

import requests


def fetch_go_terms(proteins: List[str]) -> List[str]:
    # http://api.geneontology.org/api/bioentity/gene/UniProtKB%3AC5Z7Z4/function?rows=100&start=0
    go_terms = []
    go_api = 'http://api.geneontology.org/api/'
    go_gene = go_api + 'bioentity/gene/'

    for prot in proteins:

        params = {
            'rows': 100,
            'start': 0
        }

        api_call = go_gene + prot + '/function'
        count = 1

        while params['start'] < count:
            go_req = requests.get(api_call, params=params)
            go_resp = go_req.json()
            count = go_resp['numFound']
            for assoc in go_resp['associations']:
                go_terms.append(assoc['object']['id'])
            params['start'] += params['rows']

    return go_terms


def main():

    csvfile = open('vep_plus_go.tsv', 'w')

    vep = 'https://data.monarchinitiative.org/genophenoenvo/tassel5/season4/vep_v2.tsv'

    response = requests.get(vep)

    tsv_lines = [
        line for line in response.content.decode('utf-8').splitlines()
        if not line.startswith('##')
    ]
    dict_reader = csv.DictReader(tsv_lines, delimiter='\t')
    new_fields: List[str] = list(dict_reader.fieldnames)
    new_fields.append('Go_terms')
    writer = csv.DictWriter(csvfile, delimiter='\t', fieldnames=new_fields)

    writer.writeheader()

    for row in dict_reader:
        extras = row['Extra'].split(';')
        extra_fields = {
            field.split('=')[0] : field.split('=')[1].split(',')
            for field in extras
        }
        if 'TREMBL' in extra_fields:
            row['Go_terms'] = "|".join(fetch_go_terms(extra_fields['TREMBL']))
        else:
            row['Go_terms'] = ''
        writer.writerow(row)


if __name__ == "__main__":
    main()
