import requests

from conftest import create_token, create_booking


def test_put_request(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking
    PUT_URL = base_url + base_path + str(param)
    cookie = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    print(headers)
    json_payload = {
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Pramod", "Failed Message - Incorrect FirstName"


