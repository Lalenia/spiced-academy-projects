"""
Contains the test cases for the application unit tests.
"""

# from application import app
# import requests


def test_homepage_available(client):
    """Test if we can access the homepage"""
    response = client.get("/")

    # 3. assert that the request was valid and served
    assert response.status_code == 200


def test_homepage_contains_recommender(client):
    """Tests if the homepage contains the word Recommender"""
    response = client.get("/")
    assert "Recommender" in response.data.decode("utf-8")
