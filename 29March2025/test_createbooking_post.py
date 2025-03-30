import requests
import pytest

@pytest.mark.positive
def test_Createbooking_positive():
    print("Create booking testcase")
    URL="https://restful-booker.herokuapp.com/booking"
    header={"Content-Type":"application/json"}
    jason_payload={
    "firstname" : "Ankit",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    responce_body=requests.post(url=URL,headers=header,json=jason_payload)
    print(type(URL))
    print(type(header))
    print(type(jason_payload))

    assert responce_body.status_code == 200

    # get the reponse Body and Verify the JSON, Booking ID is not None
    data=responce_body.json()
    bookingid=  data["bookingid"]
    print(bookingid)
    assert bookingid is not  None
    assert data["booking"]["firstname"] == "Ankit","this is not the way"

@pytest.mark.negative
def test_createbooking_neagtive():
    print("Create booking testcase ")
    header={"Content-Type": "application/json"}
    Jason={}
    URL="https://restful-booker.herokuapp.com/booking"
    responce_body=requests.post(url=URL,headers=header,json=Jason)
    data=responce_body.json()
    assert responce_body.status_code == 500
    print(type(URL))
    print(type(header))
    print(type(Jason))

