<script setup>
import { usePatientDataStore } from '~/composables/patientDataStore';
const usePatientData = usePatientDataStore();
const inputArray = ref([

  {
    inputName: "Primary Care Doctor Name",
    type: "text",
    value: "",
  },
  {
    inputName: "Primary Care Phone Number",
    type: "text",
    value: "",
  },
  {
    inputName: "Primary Care Fax Number",
    type: "text",
    required:false,
    value: "",
  },
  {
    inputName:"Primary Care Street Name",
    type:"text",
    value:""
  },
  {
    inputName:"Primary Care City",
    type:"text",
    value:""
  },
  {
    inputName:"Primary Care State",
    type:"text",
    value:""
  },{
    inputName:"Primary Care Zipcode",
    type:"number",
    value:""
  },
]);
</script>
<template>
  <div class="flex flex-col lg:items-center px-4 space-y-4">
    <!-- Renders List Form Component  -->
    <ListFormComp
      :input-array="inputArray"
      title="Referral Details"
      next-page-link="/confirm"
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
