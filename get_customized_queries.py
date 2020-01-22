__author__ = 'miguel.freitas@checkmarx.com'

import argparse
import pyodbc
import sys
import json
import os


DB = "CxDB"
filename = "customized_queries.json"


def is_str(string):
    return string is not None and isinstance(string, str) and len(string) > 0


def is_int(integer):
    return not isinstance(integer, bool) and isinstance(integer, int)


def is_conn(conn):
    return conn is not None and isinstance(conn, pyodbc.Connection)


def write_queries_to_file(queries, f):
    if queries and len(queries) > 0 and is_str(f):
        if f.endswith(".json"):
            data = {}
            data['queries'] = []

            for query in queries:
                if len(query) == 17:
                    data['queries'].append({
                        'query_id': query[0],
                        'package_id': query[1],
                        'name': query[2],
                        'source': query[3],
                        'draft_source': query[4],
                        'cwe': query[5],
                        'comments': query[6],
                        'severity': query[7],
                        'is_executable': query[8],
                        'is_encrypted': query[9],
                        'is_deprecated': query[10],
                        'is_check_out': query[11],
                        'update_time': str(query[12]),
                        'current_username': query[13],
                        'is_compiled': query[14],
                        'cx_description_id': query[15],
                        'engine_metadata': query[16],
                    })
                else:
                    print("Query row on DB does not has the expected length")
                    print(query)
                    break
            f = os.path.basename(f)
            if os.access("/", os.W_OK):
                with open(f, 'w') as outfile:
                    json.dump(data, outfile, indent=4, sort_keys=True)
            else:
                raise PermissionError("You don't have \
                    permissions to access this file")
        else:
            raise AttributeError("File should have \".json\" extension")
    else:
        print("No Customized Queries Found !")


def connect_to_db(driver, server, user, password, database):
    if is_str(driver) and \
            is_str(server) and \
            is_str(user) and \
            is_str(password) and \
            is_str(database):
        try:
            conn = pyodbc.connect(
                'DRIVER={' + driver + '};SERVER=' + server +
                ';DATABASE=' + database +
                ';UID=' + user +
                ';PWD=' + password,
                timeout=3)
            print("Connection to", database, "success")
            return conn
        except pyodbc.OperationalError or \
                pyodbc.InterfaceError or \
                pyodbc.Error as error:
            raise ConnectionError(error)
    else:
        raise AttributeError(
            "server | user | password | database were not provided")


def get_customized_queries(conn):
    if is_conn(conn):
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM dbo.Query WHERE QueryId>100000")
        rows = cursor.fetchall()
        if len(rows) > 0:
            return rows
        else:
            raise False
    else:
        raise AttributeError(
            "Connection object was not provided")


def get_args(args):
    if isinstance(args, list) and len(args) > 0:
        args_parser = argparse.ArgumentParser(
            description='Get Customized Queries from CxDB')
        args_parser.add_argument(
            '-dbd', '--dbdriver', help='Checkmarx MSSQL DB Driver',
            required=False,
            default="SQL Server")
        args_parser.add_argument(
            '-dbu', '--dbuser', help='Checkmarx MSSQL DB Username',
            required=True)
        args_parser.add_argument('-dbp', '--dbpassword',
                                 help='Checkmarx MSSQL DB Password',
                                 required=True)
        args_parser.add_argument('-dbs', '--dbserver',
                                 help='Checkmarx MSSQL DB Server URL',
                                 required=True)
        args_parser.add_argument('-f', '--file',
                                 help='File Name to write customized queries',
                                 required=False,
                                 default='customized_queries.json')
        return args_parser.parse_args(args)
    else:
        raise AttributeError("args should be a non-empty array")


def main(args):
    if hasattr(args, "dbdriver") and \
            hasattr(args, "dbserver") and \
            hasattr(args, "dbuser") and \
            hasattr(args, "dbpassword"):
        db_server = args.dbserver
        db_user = args.dbuser
        db_pwd = args.dbpassword
        db_driver = args.dbdriver
        filename = args.file
        if is_str(db_driver) and \
                is_str(db_server) and \
                is_str(db_user) and \
                is_str(db_pwd):

            conn = connect_to_db(
                db_driver, db_server, db_user, db_pwd, DB)

            if is_conn(conn):
                queries = get_customized_queries(conn)
                if queries:
                    print("Found", len(queries), "customized queries")
                    write_queries_to_file(queries, filename)
                else:
                    print("No Customized Queries Found !")
            else:
                raise Exception("Cannot connect to Database")
        else:
            raise Exception(
                "db_server | db_user | db_pwd \
                    are not valid strings")
    else:
        raise Exception(
            "db_server | db_user | db_pwd \
                was not provided as an argument")


if __name__ == "__main__":
    main(get_args(sys.argv[1:]))
