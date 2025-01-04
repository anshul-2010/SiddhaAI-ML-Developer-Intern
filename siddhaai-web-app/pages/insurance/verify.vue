<script setup lang="ts">
import { usePatientDataStore } from "~/composables/patientDataStore";

const usePatientData = usePatientDataStore();

const inputArray = ref([
  {
    inputName: "Group Number",
    type: "text",
    value: "",
  },
  {
    inputName: "Member ID",
    type: "text",
    value: "",
  },
]);

const inputArraySubcriber = ref([
  ...inputArray.value,
  {
    inputName: "Subscriber First Name",
    type: "text",
    value: "",
  },
  {
    inputName: "Subscriber Last Name",
    type: "text",
    value: "",
  },
  {
    inputName: "Subscriber Date of Birth ( dd-mm-yyyy )",
    type: "date",
    value: "",
  },
  {
    inputName: "Subscriber Relationship to Patient",
    type: "select",
    value: [
      "Father",
      "Mother",
      "Child",
      "Significant Other",
      "Life Partner",
      "Dependent",
    ],
  },
]);
const insuredPatient = ref(true);
</script>
<template>
  <div class="flex flex-col space-y-4 px-4 lg:items-center">
    <!-- Renders Progress Bar Component  -->
    <ProgressBarComp :step-value="5" />
    <!-- checkbox  -->
    <div class="px-8 py-4 text-center text-xl font-semibold">
      <!-- Check Box Input  -->
      <input
        type="checkbox"
        name=""
        id=""
        class="mx-2 h-6 w-6 transition checked:text-green-500"
        v-model="insuredPatient"
      />
      <!-- Text  -->
      Insured person is same as the Patient
    </div>
    <!-- List Form Component  -->
    <ListFormComp
      :input-array="insuredPatient ? inputArray : inputArraySubcriber"
      title="Insurance Details"
      next-page-link="/contact"
      next-button
      @emit-value="
        (inputName, newValue) => {
          usePatientData.changeValue(inputName, newValue);
          console.log(usePatientData.patient);
        }
      "
    />
  </div>
</template>
