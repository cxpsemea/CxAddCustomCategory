__author__ = 'miguel.freitas@checkmarx.com'

from add_custom_category import is_str
from add_custom_category import is_int
from add_custom_category import is_conn
from add_custom_category import read_file
from add_custom_category import connect_to_db
from add_custom_category import get_category_type_id_by_name

from add_custom_category import get_args
from add_custom_category import main

from collections import namedtuple
import pytest
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
    with pytest.raises(ConnectionError):
        assert connect_to_db(DBDRIVER, DBS, DBU, DBP, DBD)


def test_get_category_type_id_by_name():
    assert get_category_type_id_by_name("", "")
    with pytest.raises(AttributeError,
                       match="Connection object or Category Name \
                           was not provided"):
        assert get_category_type_id_by_name(None, None)


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
    with pytest.raises(ConnectionError):
        assert main(args)
