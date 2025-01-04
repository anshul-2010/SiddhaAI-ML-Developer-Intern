<script setup lang="ts">
import { usePatientDataStore } from '~/composables/patientDataStore';


const usePatientData = usePatientDataStore();
const addressDetailsArray = ref([
  {
    inputName: "Street Name",
    type: "text",
    value: "",
  },
  {
    inputName: "City",
    type: "text",
    value: "",
  },
  {
    inputName: "State",
    type: "select",
    value: ["CA", "LA", "OK"],
  },
  {
    inputName: "Zipcode",
    type: "text",
    value: "",
  },
  {
    inputName: "Email Address",
    type: "text",
    value: "",
  },
  {
    inputName:"Phone Number",
    type:"text",
    value:""
  }
]);
</script>
<template>
  <div class="flex flex-col space-y-4 px-4 lg:items-center">
    <!-- Renders Progress Bar Component  -->
    <ProgressBarComp :step-value="3" />
    <!-- List Form Component  -->
    <ListFormComp
      title="Address Details"
      :input-array="addressDetailsArray"
      next-page-link="/insurance"
      next-button
      @emit-value="(inputName, newValue) => {
        usePatientData.changeValue(inputName, newValue);
        console.log(usePatientData.patient);
        
      }"
    />
    <!-- mailing address checkbox  -->
    <!-- <div class="text-xl font-semibold px-8 text-center"> -->
    <!-- Check Box Input  -->
    <!-- <input type="checkbox" name="" id="" class="mx-2 h-5 w-5" :value="mailingAddressCheckbox" -->
    <!-- @change="mailingAddressCheckbox = !mailingAddressCheckbox" /> -->
    <!-- Text  -->
    <!-- Apply the above details for mailing address -->
    <!-- </div> -->

    <!-- new list component -->
    <!-- <ListFormComp v-if="mailingAddressCheckbox === false" title="Mailing Address Details" -->
    <!-- :input-array="addressDetailsArray" next-page-link="/insurance" next-button /> -->
  </div>
</template>
