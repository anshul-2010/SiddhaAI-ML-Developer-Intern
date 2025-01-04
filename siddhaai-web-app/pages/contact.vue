<script setup>
import { usePatientDataStore } from "~/composables/patientDataStore";
const usePatientData = usePatientDataStore();
const inputArray = ref([
  {
    inputName: "Last Name",
    type: "text",
    value: "",
  },
  {
    inputName: "First Name",
    type: "text",
    value: "",
  },
  {
    inputName: "Contact Number",
    type: "text",
    value: "",
  },
  {
    inputName: "Relationship",
    type: "select",
    value: [
      "Spouse",
      "Parent",
      "Children",
      "Cousin",
      "Sibling",
      "Guardian",
      "Other(Neighbor, Friend...)",
    ],
  },
]);
</script>
<template>
  <div class="flex flex-col space-y-4 px-4 lg:items-center">
    <!-- Render Progress Bar Component  -->
    <ProgressBarComp :step-value="5" />
    <!-- 911 Text  -->
    <div class="text-sm text-gray-500 lg:text-lg">
      <span class="text-red-500">*</span>
      911 is not an option for Emergency Contact
    </div>
    <!-- Render List Form Component  -->
    <ListFormComp
      :input-array="inputArray"
      next-page-link="referral"
      title="Emergency Contact"
      next-button
      @emit-value="
        (inputName, newValue) => {
          console.log('E' + inputName);

          usePatientData.changeValue('E' + inputName, newValue);
          console.log(usePatientData.patient);
        }
      "
    />
  </div>
</template>
