from fastapi import APIRouter, Depends, UploadFile, File, Body
import requests
from utils import token
from typing import List
from . import models
from drchrono.drc import drc
import json
import base64

base_url = "https://drchrono.com"
router = APIRouter(prefix="/patient")


@router.get("/")
async def get_patients():
    drc_client = drc(token.get_token())
    return drc_client.patients().patientlist(verbose_true=True)

@router.post("/")
async def create_patient(
    data: models.Patient
):
    
    headers = token.create_headers()
    headers["Content-Type"] = "application/json"

    # insurance_front_data = base64.b64encode(data.primary_insurance.photo_front).decode() # str
    # insurance_back_data = base64.b64encode(await files[1].read()).decode()
    post_data = {
        "first_name": data.first_name,
        "middle_name": data.middle_name,
        "last_name": data.last_name,
        "gender": data.gender,
        "doctor": 359001,
        "cell_phone": data.cell_phone,
        "date_of_birth": data.dob.strftime("%Y-%m-%d"),
        "address": data.address,
        "city": data.city,
        "state": data.state,
        "zip_code": data.zip_code,
        "email": data.email,
        "emergency_contact_name": data.emergency_contact_name,
        "emergency_contact_phone": data.emergency_contact_phone,
        "emergency_contact_relation": data.emergency_contact_relation,
        "referring_doctor": {
            "first_name": data.referrel_doctor.first_name,
            "last_name": data.referrel_doctor.last_name,
            "fax": data.referrel_doctor.fax,
            "phone": data.referrel_doctor.phone,
            "address":data.referrel_doctor.address
        },
        "primary_insurance": {
            "insurance_id_number": data.primary_insurance.insurance_id_number,
            "insurance_group_number": data.primary_insurance.insurance_group_number,
            "photo_front": data.primary_insurance.photo_front,
            "photo_back": data.primary_insurance.photo_back,
        },
    }
    if(not data.primary_insurance.is_subscriber_the_patient):
        post_data["primary_insurance"]["is_subscriber_the_patient"] = False
        post_data["primary_insurance"]["subscriber_first_name"] = data.primary_insurance.subscriber_first_name
        post_data["primary_insurance"]["subscriber_last_name"] = data.primary_insurance.subscriber_last_name
        post_data["primary_insurance"]["subscriber_date_of_birth"] = data.primary_insurance.subscriber_dob.strftime("%Y-%m-%d")
        post_data["primary_insurance"]["patient_relationship_to_subscriber"] = data.primary_insurance.subscriber_relationship
    
    payload = json.dumps(post_data)
    data: requests.Response = requests.post(
        base_url + f"/api/patients", data=payload, headers=headers
    )
    
    if data.status_code == 201:
        return {"status": data.status_code, "data": data.json()}
    return {"status": data.status_code, "response": data.content}


@router.delete("/{id}")
async def delete_patient(id: str):
    headers = token.create_headers()
    data = requests.delete(base_url + f"/api/patients/{id}", headers=headers)
    return {"status": data.status_code}

