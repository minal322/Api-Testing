import pytest
from datetime import datetime
import os
import json

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    #Add Timestamp to report file name
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/test_report_{now}.html"


@pytest.fixture(scope="session")
def setup_teardown():
    print("\n Setting Up Resources")
    yield
    print("\n Tearing Down Resources")

@pytest.fixture(scope="class")
def load_user_data():
    filepath = os.path.join(os.path.dirname(__file__),"data","test_jsonplaceholder_data.json")
    with open(filepath) as file:
        data = json.load(file)
    return data