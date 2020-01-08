__author__ = 'miguel.freitas@checkmarx.com'

import os
import sys
import inspect

currentdir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(inspect.currentframe())
    ))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pytest
from collections import namedtuple
from add_custom_category import main
from add_custom_category import get_args
from add_custom_category import update_queries
from add_custom_category import insert_queries
from add_custom_category import get_categories_ids_by_category_type
from add_custom_category import get_queries
from add_custom_category import insert_new_categories
from add_custom_category import get_categories_by_category_type_id_and_name
from add_custom_category import update_category_for_query
from add_custom_category import add_category_for_query
from add_custom_category import get_category_id
from add_custom_category import add_category
from add_custom_category import clean_old_data
from add_custom_category import \
    delete_categories_for_queries_by_category_type_id
from add_custom_category import delete_categories_by_category_type_id
from add_custom_category import check_category_type_by_name
from add_custom_category import add_category_type_by_name
from add_custom_category import get_category_type_id_by_name
from add_custom_category import connect_to_db
from add_custom_category import read_file
from add_custom_category import is_conn
from add_custom_category import is_int
from add_custom_category import is_str


# import pyodbc
FILE = "groups.json"
DBDRIVER = "SQL Server"
DBU = "test"
DBP = "test"
DBS = "TESTSERVER"
DBD = "Database"


def test_is_str():
    assert is_str(None) is False
    assert is_str(True) is False
    assert is_str(False) is False
    assert is_str(1) is False
    assert is_str(0) is False
    assert is_str(-1) is False
    assert is_str(1.1) is False
    assert is_str([]) is False
    assert is_str({}) is False
    assert is_str("") is False
    assert is_str("123") is True


def test_is_int():
    assert is_int(None) is False
    assert is_int(True) is False
    assert is_int(False) is False
    assert is_int(1.1) is False
    assert is_int([]) is False
    assert is_int({}) is False
    assert is_int("") is False
    assert is_int("123") is False
    assert is_int(1) is True
    assert is_int(0) is True
    assert is_int(-1) is True


def test_is_conn():
    assert is_conn(None) is False
    assert is_conn(True) is False
    assert is_conn(False) is False
    assert is_conn(1) is False
    assert is_conn(0) is False
    assert is_conn(-1) is False
    assert is_conn(1.1) is False
    assert is_conn([]) is False
    assert is_conn({}) is False
    assert is_conn("") is False
    assert is_conn("123") is False
    # Missing pyodbc.Connection test


def test_read_file():
    with pytest.raises(AttributeError,
                       match="No Filename provided"):
        assert read_file(None)
        assert read_file(True)
        assert read_file(False)
        assert read_file(1)
        assert read_file(0)
        assert read_file(-1)
        assert read_file(1.1)
        assert read_file([])
        assert read_file({})
        assert read_file("")
    with pytest.raises(AttributeError,
                       match="File should have \".json\" extension"):
        assert read_file("test")
    with pytest.raises(FileNotFoundError,
                       match="File Not Found"):
        assert read_file("test.json")
    json = read_file(FILE)
    assert len(json) > 0


def test_connect_to_db():
    with pytest.raises(TypeError):
        assert connect_to_db()
    with pytest.raises(AttributeError,
                       match="server | user | password | database \
                           were not provided"):
        assert connect_to_db("", "", "", "", "")
    # with pytest.raises(
    # (ConnectionError, pyodbc.InterfaceError, pyodbc.Error)
    # ):
    # assert connect_to_db(DBDRIVER, DBS, DBU, DBP, DBD)


def test_get_category_type_id_by_name():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Name \
                was not provided"):
        assert get_category_type_id_by_name(None, None)
        assert get_category_type_id_by_name(True, True)
        assert get_category_type_id_by_name(False, False)
        assert get_category_type_id_by_name(0, 0)
        assert get_category_type_id_by_name(1, 1)
        assert get_category_type_id_by_name(-1, -1)
        assert get_category_type_id_by_name(1.1, 1.1)
        assert get_category_type_id_by_name([], [])
        assert get_category_type_id_by_name({}, {})
        assert get_category_type_id_by_name("", "")


def test_add_category_type_by_name():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Name \
                was not provided"):
        assert add_category_type_by_name(None, None)
        assert add_category_type_by_name(True, True)
        assert add_category_type_by_name(False, False)
        assert add_category_type_by_name(0, 0)
        assert add_category_type_by_name(1, 1)
        assert add_category_type_by_name(-1, -1)
        assert add_category_type_by_name(1.1, 1.1)
        assert add_category_type_by_name([], [])
        assert add_category_type_by_name({}, {})
        assert add_category_type_by_name("", "")


def test_check_category_type_by_name():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Name \
                was not provided"):
        assert check_category_type_by_name(None, None)
        assert check_category_type_by_name(True, True)
        assert check_category_type_by_name(False, False)
        assert check_category_type_by_name(0, 0)
        assert check_category_type_by_name(1, 1)
        assert check_category_type_by_name(-1, -1)
        assert check_category_type_by_name(1.1, 1.1)
        assert check_category_type_by_name([], [])
        assert check_category_type_by_name({}, {})
        assert check_category_type_by_name("", "")


def test_delete_categories_by_category_type_id():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Type ID \
                was not provided"):
        assert delete_categories_by_category_type_id(None, None)
        assert delete_categories_by_category_type_id(True, True)
        assert delete_categories_by_category_type_id(False, False)
        assert delete_categories_by_category_type_id(0, 0)
        assert delete_categories_by_category_type_id(1, 1)
        assert delete_categories_by_category_type_id(-1, -1)
        assert delete_categories_by_category_type_id(1.1, 1.1)
        assert delete_categories_by_category_type_id([], [])
        assert delete_categories_by_category_type_id({}, {})
        assert delete_categories_by_category_type_id("", "")


def test_delete_categories_for_queries_by_category_type_id():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Type ID \
                was not provided"):
        assert delete_categories_for_queries_by_category_type_id(None, None)
        assert delete_categories_for_queries_by_category_type_id(True, True)
        assert delete_categories_for_queries_by_category_type_id(False, False)
        assert delete_categories_for_queries_by_category_type_id(0, 0)
        assert delete_categories_for_queries_by_category_type_id(1, 1)
        assert delete_categories_for_queries_by_category_type_id(-1, -1)
        assert delete_categories_for_queries_by_category_type_id(1.1, 1.1)
        assert delete_categories_for_queries_by_category_type_id([], [])
        assert delete_categories_for_queries_by_category_type_id({}, {})
        assert delete_categories_for_queries_by_category_type_id("", "")


def test_clean_old_data():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Type ID \
                was not provided"):
        assert clean_old_data(None, None)
        assert clean_old_data(True, True)
        assert clean_old_data(False, False)
        assert clean_old_data(0, 0)
        assert clean_old_data(1, 1)
        assert clean_old_data(-1, -1)
        assert clean_old_data(1.1, 1.1)
        assert clean_old_data([], [])
        assert clean_old_data({}, {})
        assert clean_old_data("", "")


def test_add_category():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Name or Category Type ID \
                was not provided"):
        assert add_category(None, None, None)
        assert add_category(True, True, True)
        assert add_category(False, False, False)
        assert add_category(0, 0, 0)
        assert add_category(1, 1, 1)
        assert add_category(-1, -1, -1)
        assert add_category(1.1, 1.1, 1.1)
        assert add_category([], [], [])
        assert add_category({}, {}, {})
        assert add_category("", "", "")


def test_get_category_id():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Name or Category Type ID \
                was not provided"):
        assert get_category_id(None, None, None)
        assert get_category_id(True, True, True)
        assert get_category_id(False, False, False)
        assert get_category_id(0, 0, 0)
        assert get_category_id(1, 1, 1)
        assert get_category_id(-1, -1, -1)
        assert get_category_id(1.1, 1.1, 1.1)
        assert get_category_id([], [], [])
        assert get_category_id({}, {}, {})
        assert get_category_id("", "", "")


def test_add_category_for_query():
    with pytest.raises(AttributeError,
                       match="Connection object or Category ID or Query ID \
                was not provided"):
        assert add_category_for_query(None, None, None)
        assert add_category_for_query(True, True, True)
        assert add_category_for_query(False, False, False)
        assert add_category_for_query(0, 0, 0)
        assert add_category_for_query(1, 1, 1)
        assert add_category_for_query(-1, -1, -1)
        assert add_category_for_query(1.1, 1.1, 1.1)
        assert add_category_for_query([], [], [])
        assert add_category_for_query({}, {}, {})
        assert add_category_for_query("", "", "")


def test_update_category_for_query():
    with pytest.raises(AttributeError,
                       match="Connection object or Category ID or Query ID \
                was not provided"):
        assert update_category_for_query(None, None, None)
        assert update_category_for_query(True, True, True)
        assert update_category_for_query(False, False, False)
        assert update_category_for_query(0, 0, 0)
        assert update_category_for_query(1, 1, 1)
        assert update_category_for_query(-1, -1, -1)
        assert update_category_for_query(1.1, 1.1, 1.1)
        assert update_category_for_query([], [], [])
        assert update_category_for_query({}, {}, {})
        assert update_category_for_query("", "", "")


def test_get_categories_by_category_type_id_and_name():
    with pytest.raises(AttributeError,
                       match="Connection object or Category ID or Query ID \
                was not provided"):
        assert get_categories_by_category_type_id_and_name(None, None, None)
        assert get_categories_by_category_type_id_and_name(True, True, True)
        assert get_categories_by_category_type_id_and_name(False, False, False)
        assert get_categories_by_category_type_id_and_name(0, 0, 0)
        assert get_categories_by_category_type_id_and_name(1, 1, 1)
        assert get_categories_by_category_type_id_and_name(-1, -1, -1)
        assert get_categories_by_category_type_id_and_name(1.1, 1.1, 1.1)
        assert get_categories_by_category_type_id_and_name([], [], [])
        assert get_categories_by_category_type_id_and_name({}, {}, {})
        assert get_categories_by_category_type_id_and_name("", "", "")


def test_insert_new_categories():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Type ID \
                was not provided"):
        assert insert_new_categories(None, None, None)
        assert insert_new_categories(True, True, True)
        assert insert_new_categories(False, False, False)
        assert insert_new_categories(0, 0, 0)
        assert insert_new_categories(1, 1, 1)
        assert insert_new_categories(-1, -1, -1)
        assert insert_new_categories(1.1, 1.1, 1.1)
        assert insert_new_categories([], [], [])
        assert insert_new_categories({}, {}, {})
        assert insert_new_categories("", "", "")


def test_get_queries():
    with pytest.raises(AttributeError,
                       match="Connection object or Query List \
            was not provided"):
        assert get_queries(None, None)
        assert get_queries(True, True)
        assert get_queries(False, False)
        assert get_queries(0, 0)
        assert get_queries(1, 1)
        assert get_queries(-1, -1)
        assert get_queries(1.1, 1.1)
        assert get_queries([], [])
        assert get_queries({}, {})
        assert get_queries("", "")


def test_insert_queries():
    with pytest.raises(AttributeError,
                       match="Connection object or Category ID \
                was not provided"):
        assert insert_queries(None, None, None)
        assert insert_queries(True, True, True)
        assert insert_queries(False, False, False)
        assert insert_queries(0, 0, 0)
        assert insert_queries(1, 1, 1)
        assert insert_queries(-1, -1, -1)
        assert insert_queries(1.1, 1.1, 1.1)
        assert insert_queries([], [], [])
        assert insert_queries({}, {}, {})
        assert insert_queries("", "", "")


def test_get_categories_ids_by_category_type():
    with pytest.raises(AttributeError,
                       match="Connection object or Category Type ID \
                was not provided"):
        assert get_categories_ids_by_category_type(None, None)
        assert get_categories_ids_by_category_type(True, True)
        assert get_categories_ids_by_category_type(False, False)
        assert get_categories_ids_by_category_type(0, 0)
        assert get_categories_ids_by_category_type(1, 1)
        assert get_categories_ids_by_category_type(-1, -1)
        assert get_categories_ids_by_category_type(1.1, 1.1)
        assert get_categories_ids_by_category_type([], [])
        assert get_categories_ids_by_category_type({}, {})
        assert get_categories_ids_by_category_type("", "")


def test_update_queries():
    with pytest.raises(AttributeError,
                       match="Connection object or Category ID \
                was not provided"):
        assert update_queries(None, None, None)
        assert update_queries(True, True, True)
        assert update_queries(False, False, False)
        assert update_queries(0, 0, 0)
        assert update_queries(1, 1, 1)
        assert update_queries(-1, -1, -1)
        assert update_queries(1.1, 1.1, 1.1)
        assert update_queries([], [], [])
        assert update_queries({}, {}, {})
        assert update_queries("", "", "")


def test_get_args():
    with pytest.raises(AttributeError,
                       match="args should be a non-empty array"):
        assert get_args(None)
        assert get_args(True)
        assert get_args(False)
        assert get_args(1)
        assert get_args(0)
        assert get_args(-1)
        assert get_args(1.1)
        assert get_args([])
        assert get_args({})
        assert get_args("")
        assert get_args("False")
    args = get_args(["-dbd", DBDRIVER, "-dbu", DBU,
                     "-dbs", DBS, "-dbp", DBP, "-fg", FILE])
    assert hasattr(args, "file_groups") and \
        hasattr(args, "dbdriver") and \
        hasattr(args, "dbserver") and \
        hasattr(args, "dbuser") and \
        hasattr(args, "dbpassword")
    assert args.dbdriver == DBDRIVER
    assert args.dbuser == DBU and args.dbpassword == DBP
    assert args.dbserver == DBS and args.file_groups == FILE


def test_main():
    with pytest.raises(AttributeError,
                       match="args does not has file_groups as attribute"):
        assert main(None)
        assert main(True)
        assert main(False)
        assert main(1)
        assert main(0)
        assert main(-1)
        assert main(1.1)
        assert main([])
        assert main({})
        assert main("")
        assert main("123")
    a = {"file_groups": None}
    args = namedtuple("Arguments", a.keys())(*a.values())
    assert hasattr(args, "file_groups")
    with pytest.raises(TypeError,
                       match="file_groups is not a string"):
        assert main(args)
        args.file_groups = True
        assert main(args)
        args.file_groups = False
        assert main(args)
        args.file_groups = 1
        assert main(args)
        args.file_groups = 0
        assert main(args)
        args.file_groups = -1
        assert main(args)
        args.file_groups = 1.1
        assert main(args)
        args.file_groups = []
        assert main(args)
        args.file_groups = {}
        assert main(args)
        args.file_groups = ""
        assert main(args)
    a = {"file_groups": "123"}
    args = namedtuple("Arguments", a.keys())(*a.values())
    assert hasattr(args, "file_groups")
    with pytest.raises(AttributeError,
                       match='File should have \".json\" extension'):
        assert main(args)
        args.file_groups = "groups.txt"
        assert main(args)
    a = {"file_groups": FILE}
    args = namedtuple("Arguments", a.keys())(*a.values())
    assert hasattr(args, "file_groups")
    with pytest.raises(Exception,
                       match="db_server | db_user | db_pwd \
                           was not provided as an argument"):
        assert main(args)

    a = {"file_groups": FILE, "dbserver": "",
         "dbuser": "", "dbpassword": ""}
    args = namedtuple("Arguments", a.keys())(*a.values())
    assert hasattr(args, "file_groups") and \
        hasattr(args, "dbserver") and \
        hasattr(args, "dbuser") and \
        hasattr(args, "dbpassword")
    with pytest.raises(Exception,
                       match="db_server | db_user | db_pwd \
                           are not valid strings"):
        assert main(args)

    a = {"file_groups": FILE, "dbserver": DBS,
         "dbuser": DBU, "dbpassword": DBP,
         "dbdriver": DBDRIVER}
    args = namedtuple("Arguments", a.keys())(*a.values())
    assert hasattr(args, "file_groups") and \
        hasattr(args, "dbserver") and \
        hasattr(args, "dbuser") and \
        hasattr(args, "dbpassword") and \
        hasattr(args, "dbdriver")
    # with pytest.raises(ConnectionError):
    # assert main(args)
