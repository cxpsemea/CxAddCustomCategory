__author__ = 'miguel.freitas@checkmarx.com'

from add_custom_category import *
import pyodbc
import pytest
FILE = "groups.json"


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
    assert is_conn("123") is False
    # Missing pyodbc.Connection test


def test_is_conn():
    with pytest.raises(AttributeError, match="No Filename provided"):
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
    with pytest.raises(AttributeError, match="File should have \".json\" extension"):
        assert read_file("test")
    with pytest.raises(FileNotFoundError, match="File Not Found"):
        assert read_file("test.json")
    json = read_file(FILE)
    assert len(json) > 0
