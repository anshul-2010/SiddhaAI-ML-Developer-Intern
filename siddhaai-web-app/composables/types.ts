export type Patient = {
    firstName: string,
    lastName: string,
    middleName: string,
    dateOfBirth: string,
    gender: string,
    preferredLanguage: string,
    address: Address,
    email: string,
    phoneNumber:string,
    insurance:Insurance,
    emergencyFirstName:string,
    emergencyLastName:string,
    emergencyContactNumber:string,
    emergencyRelationship:string,
    referrelDoctorName:string,
    referrelDoctorPhone:string,
    referrelDoctorFax:string,
    referrelDoctorAddress:Address
};
type Address = {
    streetName: string,
    city: string,
    state: string,
    zipcode: string
}
type Insurance = {
    subscriberFirstName: string | undefined,
    subscriberLastName: string | undefined,
    subscriberDateOfBirth: string | undefined,
    subscriberRelationship: string | undefined,
    groupNumber: string,
    memberId: string
}
