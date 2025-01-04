<script setup lang="ts">
import { usePatientDataStore } from '~/composables/patientDataStore';
const usePatientData = usePatientDataStore();

// Personal Details Array for ListFormComp
const personalDetailsArray = [
  {
    inputName: "Last Name",
    type: "text",
    value: "",
  },
  {
    inputName: "Middle Name",
    type: "text",
    value: "",
  },
  {
    inputName: "First Name",
    type: "text",
    value: "",
  },
  {
    inputName: "Date of Birth ( dd-mm-yyyy )",
    type: "date",
    value: "",
  },
  {
    inputName: "Gender",
    type: "select",
    value: [
      "Choose not to disclose",
      "Female",
      "Male",
      "Other",
      "Transgender Female",
      "Transgender Male",
    ],
  },
  {
    inputName: "Preferred Language",
    type: "select",
    required: false,
    value: ["English", "Russian", "Spanish", "Other"],
  },
];
</script>
<template>
  <div class="flex flex-col px-4 lg:items-center">
    <!-- progress bar component  -->
    <ProgressBarComp :step-value="2" />
    <!-- list form component  -->
    <ListFormComp
      title="Personal Details"
      :input-array="personalDetailsArray"
      next-page-link="/address"
      next-button
      @emit-value="
        (inputName:string, newValue:string) => {
          usePatientData.changeValue(inputName, newValue);
          console.log(usePatientData.patient);
        }
      "
    />
  </div>
</template>
