# CxAddCustomCategory ![Checkmarx](images/checkmarx.png)

[![Tests](https://github.com/miguelfreitas93/CxAddCustomCategory/workflows/Checkmarx%20Add%20Custom%20Category%20-%20Python%203.8/badge.svg)](https://github.com/miguelfreitas93/CxAddCustomCategory/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python script to add custom Category to Checkmarx SAST

# Inputs 

For using this script, there is a set of inputs that are required to be passed as argument to it, such as:

| Flag | Arg. Value (Example) | Description | Type | Is Required* | Default |
| ------------- | ------------- | ------------- |------------- | ------------- | ------------- |
| -dbu,--dbuser | miguel | Checkmarx MSSQL DB Username | String | Yes* | |
| -dbp,--dbpassword | ****** | Checkmarx MSSQL DB Password | Secure String | Yes* | |
| -dbs,--dbserver | MIGUEL\CHECKMARX | Checkmarx MSSQL DB Server URL | String | Yes* | |
| -fg,--file_groups | **groups.json** | Categories and Queries Mapping File | String | Yes* | |
| -dbd,--dbdriver | SQL Server | MSSQL DB Driver| String | No | SQL Server |
| -h,--help |  | Access Help Manual |  | No | |

**groups.json** content is also considered as an input, which requires to contain the following structure:

```json
{
    "category": {
        "name": "My Custom Category",
        "groups": [
            {
                "name": "Category Critical",
                "severity_id": 3,
                "queryIds": [
                    3717,
                    2277,
                    1678,
                    3885
                ]
            },
            {
                "name": "Category High",
                "severity_id": 2,
                "queryIds": [
                    1670,
                    1672,
                    630,
                    633
                ]
            },
            {
                "name": "Category Medium",
                "severity_id": 1,
                "queryIds": [
                    628,
                    4593,
                    5370,
                    639
                ]
            },
            {
                "name": "Category Low",
                "severity_id": 0,
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

| Subject | Dependency | Versions | 
| ------------- | ------------- | ------------- |
| Checkmarx | Checkmarx SAST | 8.8</br>8.9 |
| Language | Python | 3.8 [![Tests](https://github.com/miguelfreitas93/CxAddCustomCategory/workflows/Checkmarx%20Add%20Custom%20Category%20-%20Python%203.8/badge.svg)](https://github.com/miguelfreitas93/CxAddCustomCategory/actions)</br>3.7 [![Tests](https://github.com/miguelfreitas93/CxAddCustomCategory/workflows/Checkmarx%20Add%20Custom%20Category%20-%20Python%203.7/badge.svg)](https://github.com/miguelfreitas93/CxAddCustomCategory/actions)</br>3.6 [![Tests](https://github.com/miguelfreitas93/CxAddCustomCategory/workflows/Checkmarx%20Add%20Custom%20Category%20-%20Python%203.6/badge.svg)](https://github.com/miguelfreitas93/CxAddCustomCategory/actions)| 
| requirements.txt | <a href="https://pypi.org/project/pyodbc/">pyodbc</a> | 4.0.30 | 
| Database | MSSQL Driver | SQL Server, but is configurable as argument |
| Package Installer | pip | Relative to Python version |

This Python script contains some dependencies that you can find in **"requirements.txt"** file:

```txt
pyodbc==4.0.30
```

Before executing the Python script is required to install the dependencies, with following command (assure you have CMD opened with Admin permissions, if required):

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
Category already exists : My Custom Category - ID: 8
Clearing old data...

New Category Inserted :  (72, 'Category Critical', 8)
Category Critical : 4 queries to change
Inserting Query 1678 ... 0.0 %
Inserting Query 2277 ... 25.0 %
Inserting Query 3717 ... 50.0 %
Inserting Query 3885 ... 75.0 %
Updating Severity Mapping for Severity 3 - Category Critical - My Custom Category

New Category Inserted :  (73, 'Category High', 8)
Category High : 4 queries to change
Inserting Query 630 ... 0.0 %
Inserting Query 633 ... 25.0 %
Inserting Query 1670 ... 50.0 %
Inserting Query 1672 ... 75.0 %
Updating Severity Mapping for Severity 2 - Category High - My Custom Category

New Category Inserted :  (74, 'Category Medium', 8)
Category Medium : 4 queries to change
Inserting Query 628 ... 0.0 %
Inserting Query 639 ... 25.0 %
Inserting Query 4593 ... 50.0 %
Inserting Query 5370 ... 75.0 %
Updating Severity Mapping for Severity 1 - Category Medium - My Custom Category

New Category Inserted :  (75, 'Category Low', 8)
Category Low : 4 queries to change
Inserting Query 627 ... 0.0 %
Inserting Query 1671 ... 25.0 %
Inserting Query 3771 ... 50.0 %
Inserting Query 3896 ... 75.0 %
Updating Severity Mapping for Severity 0 - Category Low - My Custom Category
```

# Additional Scripts for retrieving customized queries

In order to identify correctly the IDs for a proper mapping in **groups.json**, it is required to know the IDs of the customized queries.
For this purpose it was created the script **get_customized_queries.py** in order to retrieve the customized queries to a given file, which is by default **customized_queries.json**.

Command Help Example:

```sh
> python get_customized_queries.py -h
usage: get_customized_queries.py [-h] [-dbd DBDRIVER] -dbu DBUSER -dbp DBPASSWORD -dbs DBSERVER [-f FILE]

Get Customized Queries from CxDB

optional arguments:
  -h, --help            show this help message and exit
  -dbd DBDRIVER, --dbdriver DBDRIVER
                        Checkmarx MSSQL DB Driver
  -dbu DBUSER, --dbuser DBUSER
                        Checkmarx MSSQL DB Username
  -dbp DBPASSWORD, --dbpassword DBPASSWORD
                        Checkmarx MSSQL DB Password
  -dbs DBSERVER, --dbserver DBSERVER
                        Checkmarx MSSQL DB Server URL
  -f FILE, --file FILE  File Name to write customized queries (.json extension)
```

Command Execution Example:

```sh
python get_customized_queries.py -dbu miguel -dbp ****** -dbs MIGUELFR-LAPTOP\CHECKMARX
```

Command Output Generated:

```log
Connection to CxDB success
Found 2 customized queries
File customized_queries.json with customized queries was written.
```

customized_queries.json Example:

```json
{
    "queries": [
        {
            "comments": " ",
            "current_username": " ",
            "cwe": 94,
            "cx_description_id": 1083,
            "draft_source": " ",
            "engine_metadata": null,
            "is_check_out": false,
            "is_compiled": true,
            "is_deprecated": false,
            "is_encrypted": false,
            "is_executable": true,
            "name": "Code_Injection",
            "package_id": 100001,
            "query_id": 100001,
            "severity": 3,
            "source": "result = base.Code_Injection();\r\n\r\nresult = result;",
            "update_time": "2020-01-22 16:52:04.307000"
        },
        {
            "comments": " ",
            "current_username": " ",
            "cwe": 99,
            "cx_description_id": 1231,
            "draft_source": " ",
            "engine_metadata": null,
            "is_check_out": false,
            "is_compiled": true,
            "is_deprecated": false,
            "is_encrypted": false,
            "is_executable": true,
            "name": "Resource_Injection",
            "package_id": 100001,
            "query_id": 100002,
            "severity": 3,
            "source": "result = base.Resource_Injection();\r\n\r\n//test",
            "update_time": "2020-01-22 16:57:07.607000"
        }
    ]
}
```

# License

MIT License

Copyright (c) 2020 Miguel Freitas
