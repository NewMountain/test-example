# Rough example intended to show a simple example of an integration test

from src.server import create_flask_app

app = create_flask_app()


def test_home_route():
    with app.test_client() as c:
        response = c.get("/").data.decode("utf-8")
        assert response == "Hello world"


def test_add_two_handler():
    with app.test_client() as c:
        TEST_NUMBER = 8
        rv = c.post("/addTwo", json={"number": TEST_NUMBER})
        json_data = rv.get_json()

        assert json_data == {"number": 10}
        assert (TEST_NUMBER + 2) == json_data["number"]
