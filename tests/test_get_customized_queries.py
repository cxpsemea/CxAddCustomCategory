__author__ = 'miguel.freitas@checkmarx.com'

from get_customized_queries import is_str
from get_customized_queries import is_int
from get_customized_queries import is_conn
from get_customized_queries import connect_to_db
from get_customized_queries import get_customized_queries
from get_customized_queries import get_args
from get_customized_queries import main

import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(inspect.currentframe())
    ))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


# import pyodbc
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


def test_get_customized_queries():
    with pytest.raises(AttributeError,match="Connection object was not provided"):
        assert get_customized_queries(None)
        assert get_customized_queries(True)
        assert get_customized_queries(False)
        assert get_customized_queries(1)
        assert get_customized_queries(0)
        assert get_customized_queries(-1)
        assert get_customized_queries(1.1)
        assert get_customized_queries([])
        assert get_customized_queries({})
        assert get_customized_queries("")
        assert get_customized_queries("False")


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

def test_get_args():
    with pytest.raises(AttributeError,match="args should be a non-empty array"):
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
                     "-dbs", DBS, "-dbp", DBP])
    assert hasattr(args, "dbdriver") and \
        hasattr(args, "dbserver") and \
        hasattr(args, "dbuser") and \
        hasattr(args, "dbpassword")
    assert args.dbdriver == DBDRIVER
    assert args.dbuser == DBU and args.dbpassword == DBP
    assert args.dbserver == DBS
