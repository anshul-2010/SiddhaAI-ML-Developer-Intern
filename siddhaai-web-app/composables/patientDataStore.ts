import { Patient } from "composables/types";
import { defineStore } from "pinia";

export const usePatientDataStore = defineStore("patientData", () => {
    const patient = ref<Patient>({
        firstName: "",
        lastName: "",
        middleName: "",
        address: {
            city: "",
            state: "",
            streetName: "",
            zipcode: ""
        },
        dateOfBirth: "",
        email: "",
        phoneNumber: "",
        emergencyContactNumber: "",
        emergencyFirstName: "",
        emergencyLastName: "",
        emergencyRelationship: "",
        gender: "",
        preferredLanguage: "",
        insurance: {
            groupNumber: "",
            memberId: "",
            subscriberDateOfBirth: "",
            subscriberFirstName: "",
            subscriberLastName: "",

            subscriberRelationship: ""
        },
        referrelDoctorAddress: {
            city: "",
            state: "",
            streetName: "",
            zipcode: "",
        },
        referrelDoctorFax: "",
        referrelDoctorName: "",
        referrelDoctorPhone: "",

    });
    function changeValue(inputName: string | String, newValue: string) {
        switch (inputName) {
            case "Last Name":
                patient.value.lastName = newValue;
                break;
            case "First Name":
                patient.value.firstName = newValue;
                break;
            case "Middle Name":
                patient.value.middleName = newValue;
                break;
            case "Date of Birth ( dd-mm-yyyy )":
                patient.value.dateOfBirth = newValue;
                break;
            case "Gender":
                patient.value.gender = newValue;
                break;
            case "Preferred Language":
                patient.value.preferredLanguage = newValue;
                break;
            case "Street Name":
                patient.value.address.streetName = newValue;
                break;
            case "City":
                patient.value.address.city = newValue;
                break;
            case "State":
                patient.value.address.state = newValue;
                break;
            case "Zipcode":
                patient.value.address.zipcode = newValue;
                break;
            case "Email Address":
                patient.value.email = newValue;
                break;
            case "Phone Number":
                patient.value.phoneNumber = newValue;
                break;
            case "Group Number":
                patient.value.insurance.groupNumber = newValue;
                break;
            case "Member ID":
                patient.value.insurance.memberId = newValue;
                break;
            case "Subscriber First Name":
                patient.value.insurance.subscriberFirstName = newValue;
                break;
            case "Subscriber Last Name":
                patient.value.insurance.subscriberLastName = newValue;
                break;
            case "Subscriber Date of Birth ( dd-mm-yyyy )":
                patient.value.insurance.subscriberDateOfBirth = newValue;
                break;
            case "Subscriber Relationship to Patient":
                patient.value.insurance.subscriberRelationship = newValue;
                break;
            case "ELast Name":
                patient.value.emergencyLastName = newValue;
                break;
            case "EFirst Name":
                patient.value.emergencyFirstName = newValue;
                break;
            case "EContact Number":
                patient.value.emergencyContactNumber = newValue;
                break;
            case "ERelationship":
                patient.value.emergencyRelationship = newValue;
                break;
            case "Primary Care Doctor Name":
                patient.value.referrelDoctorName = newValue;
                break;
            case "Primary Care Phone Number":
                patient.value.referrelDoctorPhone = newValue;
                break;
            case "Primary Care Fax Number":
                patient.value.referrelDoctorFax = newValue;
                break;
            case "Primary Care Street Name":
                patient.value.referrelDoctorAddress.streetName = newValue;
                break;
            case "Primary Care City":
                patient.value.referrelDoctorAddress.city = newValue;
                break;
            case "Primary Care State":
                patient.value.referrelDoctorAddress.state = newValue;
                break;
            case "Primary Care Zipcode":
                patient.value.referrelDoctorAddress.zipcode = newValue;
                break;
        }
    }
    function getRequestData() {
        return {
            "first_name": "Bhaarat",
            "middle_name": "Krishnan",
            "last_name": "J",
            "gender": "Male",
            "doctor": 359001,
            "dob": "2003-10-29",
            "address": "w/266, c sector, 13th street",
            "city": "Chennai",
            "state": "CA",
            "cell_phone": "+1 (444) 555-1234",
            "zip_code": "90011",
            "email": "bhaaratkrishnan29113@gmail.com",
            "emergency_contact_name": "Arjun",
            "emergency_contact_phone": "+1 (444) 555-1234",
            "emergency_contact_relation": "Friend",
            "primary_insurance": {
                "insurance_group_number": "123456",
                "insurance_id_number": "1234578"
            },
            "referrelDoctor": {
                "first_name": "Shanmuga Priya",
                "last_name": "Arumugam",
                "fax": "+1 (444) 555-1234",
                "phone": "+1 (555) 444-3333"
            }
        }

    }
    return { patient, changeValue, getRequestData }
})