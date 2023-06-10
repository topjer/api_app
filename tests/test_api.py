import pytest
from fastapi.testclient import TestClient

from ..sql_app.app import my_sessionmaker, app
from ..sql_app.crud import empty_table

client = TestClient(app)


# make sure that target table is empty before each tests
@pytest.fixture(autouse=True)
def prepare_table():
    empty_table(my_sessionmaker())


def test_root():
    response = client.get("/")
    assert response.json() == {"message": "Hello World!"}


def test_add_url():
    """Check that url is correctly added"""
    response = client.post(
        "add_url",
        json={
            "url": "https://www.codecentric.de/ueber-uns/standorte/leipzig",
            "description": "Definitely apply here!",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "https://www.codecentric.de/ueber-uns/standorte/leipzig was added."
    }

    response = client.get("list_urls")
    assert response.status_code == 200
    response_dict = response.json()[0]
    assert (
        response_dict["long_url"]
        == "https://www.codecentric.de/ueber-uns/standorte/leipzig"
    )
    assert response_dict["short_url"] == "vJTnE3Ju"
    assert response_dict["description"] == "Definitely apply here!"
    assert response_dict["klicks"] == 0


def test_add_twice_results_in_error():
    """Make sure correct return code when url is added twice"""
    _ = client.post("add_url", json={"url": "https://www.google.com"})

    response = client.post("add_url", json={"url": "https://www.google.com"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Short-url is already in database."}


def test_redirect():
    _ = client.post("add_url", json={"url": "https://www.manjaro.org"})

    response = client.get(f"/redirect/yfPy1LZh")

    assert response.status_code == 200
