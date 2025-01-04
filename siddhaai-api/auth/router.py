from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from os import getenv
from urllib import parse
from deta import Deta
import requests

router = APIRouter(prefix="/auth")

base_url = "https://drchrono.com/"
redirect_uri = "https://siddhaai-demo-api.blueswype.in/auth/callback"


@router.get("/url")
async def auth_client():
    client_id = getenv("client_id")
    query_params = {
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "response_type": "code",
    }
    return RedirectResponse(
        base_url + "o/authorize/?" + parse.urlencode(query=query_params)
    )


@router.get("/callback")
async def auth_callback(code: str = Query()):
    response = requests.post(
        base_url + "o/token/",
        data={
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri,
            "client_id": getenv("client_id"),
            "client_secret": getenv("client_secret"),
        },
    )
    response.raise_for_status()
    data = response.json()
    access_token = data["access_token"]
    refresh_token = data["refresh_token"]
    db = Deta(getenv("DETA_PROJECT_KEY")).Base("dev")
    db.put({"token": access_token, "key": "access_token"}, expire_in=data["expires_in"])
    db.put({"token": refresh_token, "key": "refresh_token"})
    return {"status": 200}
