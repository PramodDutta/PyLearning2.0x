# API Request - HTTP Request

import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests


@allure.title("Create Booking CRUD")
@allure.description("TC#1 - Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive():
    # Request
    # URL
    # Method
    # Headers
    # Payload / Data / Body
    # Auth(No
    # Auth in Post)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    
    # Response Body  Verification,
    # Headers
    # Status Code
    # JSON Schema Validation
    # Time Response
    
    assert response.status_code == 200
    print(response.headers)
    response_json = response.json()
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int
    firstname = response_json["booking"]["firstname"]
    checkin = response_json["booking"]["bookingdates"]["checkin"]
    assert firstname == "Amit"
    assert checkin == "2018-01-01"
    
    
@allure.title("Create Booking CRUD")
@allure.description("TC#2 - Verify Booking is not created with {} data ")
@pytest.mark.crud
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    
    # Assertions
    assert response.status_code == 500

