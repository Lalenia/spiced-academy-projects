"""
pytest looks for a file called conftest.py and if it exists it will execute it.
"""


import pytest
from application import app


# Fixture sets up an environment/server/database connection for testing
@pytest.fixture()
def client():  # name of the function is determining how to pass it into a test function
    with app.test_client() as client:
        yield client

