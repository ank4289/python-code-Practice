import requests

def main():
    id="1171"
    URL="https://restful-booker.herokuapp.com/booking/"
    full_url=URL+id
    responce_body=requests.get(full_url)
    assert responce_body.status_code == 200

    data=responce_body.json()
    print(type(data))


 # Assertions

# Verification of Keys

    assert "firstname" in data,"incorrect firstname"
    assert "lastname" in data ,"incorrect last name"

# Verification of Data
    assert data["firstname"] == "Ankit","Incorrect  FirstName is John"
    print(data["firstname"])
    assert data["lastname"] == "Brown","Incorrect,FirstName is Smith"
    assert data["bookingdates"]["checkin"] == "2018-01-01","Check in date is incorrect it should 1 jan 2018"


if __name__== "__main__":
    main()
