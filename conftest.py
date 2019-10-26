# content of conftest.py
import pytest
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption("--game_date", action="store", default=[], help="list of game_date to pass to test functions")