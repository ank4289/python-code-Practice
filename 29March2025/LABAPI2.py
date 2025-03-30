import requests

responce_body=requests.get("https://restful-booker.herokuapp.com/booking/1")
print(responce_body.text)
print(responce_body.headers)
print(responce_body.status_code)