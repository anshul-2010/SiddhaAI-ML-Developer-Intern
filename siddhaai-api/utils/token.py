import requests
from deta import Deta
from os import getenv


def get_token():
    # getting the access_token from db
    db = Deta(getenv("DETA_PROJECT_KEY")).Base("dev")
    access_token = db.get("access_token")
    if access_token is not None:
        return access_token["token"]

    # if access_token is expired
    # fetching refresh token from db
    refresh_token = db.get("refresh_token")["token"]
    # post request data
    data = {
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "client_id": getenv("client_id"),
        "client_secret": getenv("client_secret"),
    }
    print(data)
    # post request to get new access_token
    response = requests.post("https://drchrono.com/o/token/", data=data)
    # error for status
    # response.raise_for_status()
    response_data = response.json()
    access_token = response_data["access_token"]
    # inserting new access_token to db 
    db.put(
        {"key": "access_token", "token": access_token},
        expire_in=response_data["expires_in"],
    )
    return access_token 

def create_headers():
    token = get_token()
    headers = {
        "Authorization":f"Bearer {token}"
    }
    return headers