# API Request - HTTP Request

import pytest
import requests  # pip install requests

import allure

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_get_single_request_by_id():
    response = requests.get("https://restful-booker.herokuapp.com/booking/1")
    print(response.text)
    print(response.content)
    print(response.json())
    print(response.headers)
    print(response.url)
    print(response.cookies)
    response_status = response.status_code
    assert response_status == 200


# Verify the Body, POST, PATCH, DELETE, PUT and CRUD operation
# Framework - so that we can scability