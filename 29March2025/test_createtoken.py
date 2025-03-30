import requests
def createtoken():
    URL="https://restful-booker.herokuapp.com/auth"
    jason_payload={
    "username" : "admin",
    "password" : "password123"
}
    header={"Content-Type":"application/json"}
    responce_body=requests.post(url=URL,headers=header,json=jason_payload)
    data=responce_body.json()
    tok=data["token"]
    print(tok)
    return tok

def createbooking():
    print("Create booking testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    header = {"Content-Type": "application/json"}
    jason_payload = {
            "firstname": "Ankit",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": true,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    responce_body = requests.post(url=URL, headers=header, json=jason_payload)
    print(type(URL))
    print(type(header))
    print(type(jason_payload))

    data=responce_body.json()
    bookingid=data["bookingid"]
    return bookingid

def test_put_request():
    URL="https://restful-booker.herokuapp.com/booking/"
    print(type(URL))
    id=createbooking()
    print(type(id))
    fullurl=URL+str(id)
    cookieval= "token="+ createtoken()

    header={"Content-Type":"application/json",
            "Cookie": cookieval}
    jason={
    "firstname" : "Ankittest",
    "lastname" : "sharma",
    "totalprice" : 222,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    responce_body=requests.put(url=fullurl,headers=header,json=jason)
    assert responce_body.status_code ==200

    data=responce_body.json()
    assert data["firstname"] == "Ankittest", "Failed Message - Incorrect FirstName"


def test_deleterecord():
    try:
        URL="https://restful-booker.herokuapp.com/booking/"
        id=test_createbooking()
        fullurl=URL+str(id)
        header={"Content-Type":"application/json"}
        rsponce_body=requests.delete(url=URL,headers=header)
        assert rsponce_body.status_code == 201
    except Exception as e:
        print(e)


