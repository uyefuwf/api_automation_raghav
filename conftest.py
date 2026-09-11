# conftest.py
import requests
import json
import pytest
import urllib3
from config.config import BASE_URL, USERNAME, PASSWORD
from pathlib import Path
# Disable SSL warnings for local testing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
BASE_DIR = Path(__file__).resolve().parent
# DATA_FILE = BASE_DIR / "data" / "data.json"


@pytest.fixture
def device_data():
    with open("data/data.json", "r") as file:
        return json.load(file)

@pytest.fixture
def apiclient():
    # Create a session
    session = requests.Session()
    session.verify = False  # Bypass SSL
    # If your API uses Basic Authentication, set it here:
    session.auth = (USERNAME, PASSWORD)
    # Pass the session and the base URL to the test
    return session, BASE_URL