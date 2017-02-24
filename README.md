# ItsInMyHead

## Topic 2: Relational Data Generator - Realistic Data

The goal of this project is to implement a data generator that takes as input a relation schema and provides as output a set of realistic data from selected domains for this relation. Users should be able to control the statistical distribution of the selectivity of columns if possible. The tool allows users to generate tables with realistic data such as rst and last names of personby nationality or ethnic background, addresses, telephone numbers, and credit card numbers. The system should be easily extensible if new domains and data for these domains become available. Data should be correlated if required by the user. For instance, German names may be required to have German address and telephone numbers. Users should be able to control the statistical distribution of the data. For instance, a user can require 10% European names, 10% Japanese names, 70% Chinese names, and 10% other names.

## Software Used
* Bitnami Django Stack 1.10.5
* Python 2.7.12 (default installation from django stack)
* Pgadmin3

## To Run
1. Open Settings.py in ItsInMyHead/
2. Under database, replace the following under DATABASES:

<code> 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'HOST': '**your drive**\Bitnami\djangostack-1.10.5-0\postgresql',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': '**your bitami postgres password**
    }
}
</code>
