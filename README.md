# What is ItsInMyHead

ItsInMyHead is a data generator that takes input parameters as a relation schema and generates output as a set of realistic data from selected domains. This tool is unique in providing realistic data obtained from sources including Google Maps (for addresses), using Luhn’s algorithm and referencing authentic Credit Card Prefixes (for Credit Card numbers) among many others.

This tool allows users to generate tables with realistic data such as first and last names of person by country of origin or race or gender, countries, race, addresses by country and credit card numbers by credit card companies. The functionalities of this tool will be explored in greater detail in the following sections. Additional features envisioned by the team are also outlined in the development roadmap provided.

This system is easily extensible if new domains and data for these domains become available. Instructions on how this can be done are provided under Scalability. Existing or new data can be correlated as required by the developer, from extending or utilising the existing database schema.

## Software Used
* Bitnami Django Stack 1.10.5
* Python 2.7.12 (default installation from django stack)
* Pgadmin3

# Setting up your environment

The instructions on how to setup the development environment is given below. Any software installation required has been appended to the instructions for your convenience.

## Installing Bitnami

1. Download Bitnami Django From https://bitnami.com/stack/django/installer
2. Install the files locally (henceforth known as installation directory)
3. IMPORTANT! Select postgres as the database to be used and use the following parameters
    - Port number: <code>5432</code>
    - Database name: <code>postgres</code>
    - User: <code>postgres</code>
    - Password: <code>postgres</code>
4. Complete the rest of the installation

## Clone the project
1. Fork the project from our repository: https://github.com/XYLau/ItsInMyHead
2. Clone the forked repository into local directory henceforth known as project directory

## Configuration
### ItsInMyHead/settings.py

1. Open <code>settings.py</code>
2. Update timezone in TIME_ZONE tab ensure that declaration is changed to your laptop respective acceptable value. if you're using Mac, change the value to <code>'Asia/Singapore'</code>. Otherwise, use <code>'SG'</code>.
<pre>TIME_ZONE = **value**</pre>
3. Update the directory under DATABASES tab to the local directory that you've installed django's postgres. An example has been provided in the source code.
<pre>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'HOST': '**your drive**\Bitnami\djangostack-1.10.5-0\postgresql',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': '**your bitami postgres password**
    }
}</pre>

## Setup the database
1. Open Bitnami Django Stack and navigate to the project directory
2. Setup the database by running the command <kbd>python manage.py migrate</kbd>
3. Create a superuser by running the command <kbd>python manage.py createsuperuser</kbd> using the following credentials:
    - Username: admin
    - Email address: admin@example.com
    - Password: postgres
4. Check that it works by running the project using this command <kbd>python manage.py runserver</kbd>
5. Open a browser and go to this link: <kbd>http://127.0.0.1:8000/DataGenerator/</kbd> and you should not see any errors appearing
6. Download Pgadmin3 from https://www.pgadmin.org/download/. Do not attempt to use Pgadmin4 provided in the bitnami installation because there are fundamental compatibility issues. Tried and proven.
7. Add a new connection to a server using the following credentials:
    - Host: <code>&lt;installation_directory\postgresql&gt;</code>
    - Port: <code>5432</code>
    - Maintenance DB: <code>postgres</code>
    - Username: <code>postgres</code>
    - Password: <code>postgres</code>
8. Click on Database > postgres and go to the navigation bar at the top and click onto Execute arbitrary SQL queries
9. Select and run Setup.sql from &lt;project_directory&gt;\ItsInMyHead\Scripts
10. Go back to Bitnami Stack and update database environment variables by running this command python manage.py shell
11. Close the shell by typing <code>exit()</code> or <code>Ctrl-Z-Enter</code>
12. Run the server again using this command <kbd>python manage.py runserver</kbd>
13. Open a browser and go to this link: <kbd>http://127.0.0.1:8000/DataGenerator</kbd> and you should not see any errors appearing

# Directory Structure

![directorydetail](https://cloud.githubusercontent.com/assets/14009738/24761068/f61222fa-1b1c-11e7-8bc5-bfcee8fedb3b.png)

# Scalability

The project has been restructured to allow minimal additions when scaling up its functionalities. Developers new to Django should complete the tutorials provided at https://docs.djangoproject.com/en/1.10/intro/tutorial01/.

# Running the project

1. Open Bitnami Django Stack and navigate to the project directory
    <blockquote>$ cd <kbd>&lt;directory&gt;</kbd></blockquote>
2. Run the project
    <blockquote>$ <kbd>python manage.py runserver</kbd></blockquote>
3. Open a browser and go to this link:
    <blockquote><kbd>http://127.0.0.1:8000/DataGenerator/</kbd></blockquote>

# Modifying the database

Sample scripts have been provided in the Scripts folder in the Scripts directory. Developers unfamiliar with PostgreSQL should refer to other sources of information as required.
1. Write the sql script that implements the modifications that you need to make or update the Setup.sql script if you wish to modify the default configurations upon installation
2. Open Pgadmin3 and run the script
3. Re-run the project by referring to the instructions given in the sub-section above.
