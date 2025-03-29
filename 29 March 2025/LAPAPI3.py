import requests

def main():
    id="573"
    url="https://restful-booker.herokuapp.com/booking/"
    fullurl =url+id
    print(type(fullurl))
    print(fullurl)
    responce_body=requests.get(fullurl)
    assert responce_body.status_code == 200 # If sc != 200 it error, else it will not give error


if __name__== "__main__":
    main()
