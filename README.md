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
    - Username: <code>admin</code>
    - Email address: <code>admin@example.com</code>
    - Password: <code>postgres</code>
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

# System Diagram

![systemdiagram](https://cloud.githubusercontent.com/assets/14009738/24766354/8a343922-1b2d-11e7-8b97-dfa3141df5a1.jpeg)

The architecture used in Django can be explained using the Model-View-Controller (MVC) design methodology. It separates an application into three main logical components: the model, the view, and the controller and each of these components are built to handle specific development aspects of an application. In Dangjo the following can be related:
- Models.py - [ Model ]
- Template - [ View ]
- Views.py - [ Controller ]

## High-level Architecture

![highlevelarch](https://cloud.githubusercontent.com/assets/14009738/24774251/d46d3a3a-1b4a-11e7-9dc8-350ab1434e71.png)

## Low-level Architecture

![lowlevelarch](https://cloud.githubusercontent.com/assets/14009738/24774270/e225cade-1b4a-11e7-8006-fe2194ba6959.png)

- Upon clicking the Submit Button, the Processor handles the request and fetches data from the Database then redirects back to the user window.
- Within the Processor, Parser acts as the controller then forwards to the Query Builder to build the relative SQL. Next, the Processor will execute the SQL to retrieve data from the Database.

# Database Design

![erdiagram](https://cloud.githubusercontent.com/assets/14009738/24766375/965b858e-1b2d-11e7-9372-3f02b85cbc94.png)

The following outlines an overview of the relations involved:

- Address - Stores realistic address information of different countries
- Country - Stores real Country name and code
- Race - Stores a set of available Race
- FirstName - Stores first name of individuals of different Gender and Race
- LastName - Stores last name of individuals of different Gender and Race
- Gender - Stores the different type of Gender
- CCCompany - Stores credit card relevant information

# Implementation

Developers new to Django should complete the tutorials provided at  https://docs.djangoproject.com/en/1.10/intro/tutorial01/.

## Running the project

1. Open Bitnami Django Stack and navigate to the project directory
    <blockquote>$ <kbd>cd &lt;directory&gt;</kbd></blockquote>
2. Run the project
    <blockquote>$ <kbd>python manage.py runserver</kbd></blockquote>
3. Open a browser and go to this link:
    <blockquote><kbd>http://127.0.0.1:8000/DataGenerator/</kbd></blockquote>

## Modifying the database

Sample scripts have been provided in the Scripts folder in the Scripts directory. Developers unfamiliar with PostgreSQL should refer to other sources of information as required.
1. Write the sql script that implements the modifications that you need to make or update the Setup.sql script if you wish to modify the default configurations upon installation
2. Open Pgadmin3 and run the script
3. Re-run the project by referring to the instructions given in the sub-section above.

# Future Expansions

The project has been restructured to allow minimal additions when scaling up its functionalities.

## Data Classifications

To ease future additions of new types of data, we defined three key data classifications given below. The description of each are supplemented with examples of existing and possible applications.

### Fixed Data

This classification refers to data which are obtained and stored into the database. These data are typically obtained from external sources which are then cleaned, organised and stored into the database. For information that are unlikely to change (static), this would be the recommended classification to store the data into. This is currently implemented for the following data types: Country, Race, Names, Gender, Address and Credit Card Company (CCCompany). The general process of processing these type of data will include building the queries as required in the Search module and executing the respective queries generated.

### Automated Data

This classification refers to data which do not require cleaning or processing and can be directly obtained either via algorithms or external APIs. This is currently implemented in part in generating the number sequences and check digits for Credit Card numbers. The process to generate this type of data would be to run the algorithm generation instead of the query generator. More details on integrating algorithms can be referenced in our source code. Unfortunately, this tool does not currently support integrating with external APIs. However, this is one of our priorities which will be highlighted in the next section (Roadmap).

### Automated from Fixed Data

This classification refers to a combination of the 2 abovementioned classifications. This is fully implemented in generating Credit Card numbers. The process of generating Credit Card numbers involves parsing and query generation in obtaining the prefixes of the respective credit card companies selected. Following which, a random string of numbers are created in accordance to the card number length. This string appended with the prefix obtained earlier will then be run through a verification algorithm, Luhn’s algorithm, which is commonly used in the market to verify Credit Card numbers, to obtain the check digit. Finally, the entire string is pieced together to form the Credit Card number.

## Roadmap

![roadmap](https://cloud.githubusercontent.com/assets/14009738/24774446/7bcdf5bc-1b4b-11e7-9a91-f1d65bc0f5fb.jpeg)
