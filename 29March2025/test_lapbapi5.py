import requests
import pytest

def test_sample():
    assert 4==4

def test_sample2():
    assert 4==6

def test_getrequest():
    URL="https://restful-booker.herokuapp.com/booking/"
    ID="38pyjava"
    full_url=URL+ID
    responce =requests.get(full_url)
    assert responce.status_code == 200,"Status code is not 200 not successfull"

    data=responce.json()
    print(type(data))

    # Verification of Keys

    assert "firstname" in data, "incorrect firstname"
    assert "lastname" in data, "incorrect last name"

    # Verification of Data
    assert data["firstname"] == "Ankit", "Incorrect  FirstName is John"
    print(data["firstname"])
    assert data["lastname"] == "Brown", "Incorrect,FirstName is Smith"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Check in date is incorrect it should 1 jan 2018"



