# CxAddCustomCategory ![Checkmarx](images/checkmarx.png)

[![Tests](https://github.com/miguelfreitas93/CxAddCustomCategory/workflows/Checkmarx%20Add%20Custom%20Category/badge.svg)](https://github.com/miguelfreitas93/CxAddCustomCategory/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python script to add custom Category to Checkmarx SAST

# Inputs

For using this script, there is a set of inputs that are required to be passed as argument to it, such as:

| Flag | Arg. Value (Example) | Description | Type | Is Required* |
| ------------- | ------------- | ------------- |------------- | ------------- |
| -dbu,--dbuser | miguel | Checkmarx MSSQL DB Username | String | Yes* |
| -dbp,--dbpassword | ****** | Checkmarx MSSQL DB Password | Secure String | Yes* |
| -dbs,--dbserver | MIGUEL\CHECKMARX | Checkmarx MSSQL DB Server URL | String | Yes* |
| -fg,--file_groups | **groups.json** | Categories and Queries Mapping File | String | Yes* |
| -h,--help |  | Access Help Manual |  | No |

**groups.json** content is also considered as an input, which requires to contain the following structure:

```json
{
    "category": {
        "name": "My Custom Category",
        "groups": [
            {
                "name": "Category Critical",
                "queryIds": [
                    3717,
                    2277,
                    1678,
                    3885
                ]
            },
            {
                "name": "Category High",
                "queryIds": [
                    1670,
                    1672,
                    630,
                    633
                ]
            },
            {
                "name": "Category Medium",
                "queryIds": [
                    628,
                    4593,
                    5370,
                    639
                ]
            },
            {
                "name": "Category Low",
                "queryIds": [
                    1671,
                    627,
                    3896,
                    3771
                ]
            }
        ]
    }
}
```

# Dependencies

This Python script contains some dependencies that you can find in **"requirements.txt"** file:

```txt
pyodbc==4.0.28
```

Before executing the Python script is required to install the dependencies, with following command:

```sh
pip install -r requirements.txt
```

# Execution

Command Help Example:

```sh
> python add_custom_category.py -h
usage: add_custom_category.py [-h] -dbu DBUSER -dbp DBPASSWORD -dbs DBSERVER -fg FILE_GROUPS

Add Custom Category to CxDB

optional arguments:
  -h, --help            show this help message and exit
  -dbu DBUSER, --dbuser DBUSER
                        Checkmarx MSSQL DB Username
  -dbp DBPASSWORD, --dbpassword DBPASSWORD
                        Checkmarx MSSQL DB Password
  -dbs DBSERVER, --dbserver DBSERVER
                        Checkmarx MSSQL DB Server URL
  -fg FILE_GROUPS, --file_groups FILE_GROUPS
                        Categories and Queries Mapping File
```


Command Execution Example:

```sh
python add_custom_category.py -dbu miguel -dbp ****** -dbs MIGUELFR-LAPTOP\CHECKMARX -fg groups.json
```

Command Output Generated:

```log
Connection to CxDB success
Category Type  My Custom Category  does not exist.
Creating category type : My Custom Category - ID: 9
Clearing old data...

New Category Inserted :  (307, 'Category Critical', 9)
Category Critical : 4 queries to change
Inserting Query 1678 ... 0.0 %
Inserting Query 2277 ... 25.0 %
Inserting Query 3717 ... 50.0 %
Inserting Query 3885 ... 75.0 %

New Category Inserted :  (308, 'Category High', 9)
Category High : 4 queries to change
Inserting Query 630 ... 0.0 %
Inserting Query 633 ... 25.0 %
Inserting Query 1670 ... 50.0 %
Inserting Query 1672 ... 75.0 %

New Category Inserted :  (309, 'Category Medium', 9)
Category Medium : 4 queries to change
Inserting Query 628 ... 0.0 %
Inserting Query 639 ... 25.0 %
Inserting Query 4593 ... 50.0 %
Inserting Query 5370 ... 75.0 %

New Category Inserted :  (310, 'Category Low', 9)
Category Low : 4 queries to change
Inserting Query 627 ... 0.0 %
Inserting Query 1671 ... 25.0 %
Inserting Query 3771 ... 50.0 %
Inserting Query 3896 ... 75.0 %
```

# License

MIT License

Copyright (c) 2020 Miguel Freitas