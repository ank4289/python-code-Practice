# API
# Request Lib
import requests
# Make a GET, POST, PUT , PATCH and DELETE and verify.
# HTTP Methods

def main():
    responce_body=requests.get("https://restful-booker.herokuapp.com/booking/1")
    if responce_body.status_code==200:
        print("TC1-Get request passed successfully")
    else:
        print("TC2 -get request is not successfull")

# To make an API Testing Req.
# url, auth, headers, cookies, data (payload), json, file

# Validate in API Testing
# response, headers, statuscode,responseTime, JSON Schema Validation




if __name__== "__main__":
    main()