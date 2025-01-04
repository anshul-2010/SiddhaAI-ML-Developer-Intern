from pydantic import BaseModel
from enum import Enum
from datetime import date
from typing import Optional

class GenderModel(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"
    unk = "UNK"
    asku = "ASKU"


class PrimaryInsurance(BaseModel):
    insurance_group_number: str
    insurance_id_number: str
    is_subscriber_the_patient:Optional[bool] = True
    subscriber_first_name: Optional[str] = "" 
    subscriber_last_name: Optional[str] = "" 
    subscriber_dob: Optional[date] = ""
    subscriber_relationship: Optional[str] = "" 
    photo_front:str
    photo_back:str

class ReferrelDoctor(BaseModel):
    first_name: str
    last_name: str
    fax: Optional[str] = ""
    phone: str 
    address : str


class Patient(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    gender: GenderModel
    doctor: int
    dob: date
    cell_phone: str
    address: str
    city: str
    state: str
    zip_code: str
    email: str
    emergency_contact_name: str
    emergency_contact_phone: str
    emergency_contact_relation: str
    primary_insurance: PrimaryInsurance
    referrel_doctor: ReferrelDoctor

