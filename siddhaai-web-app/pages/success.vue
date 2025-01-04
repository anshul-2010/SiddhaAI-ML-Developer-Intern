<script setup>
import { usePatientDataStore } from "~/composables/patientDataStore";

const patientStore = usePatientDataStore();
const requestData = JSON.stringify(patientStore.getRequestData());
const { data, error, pending } = useLazyFetch(
  "https://siddhaai-demo-api.blueswype.in/patient/",
  {
    method: "POST",
    body: {
      data: requestData,
    },
    headers: {
      "accept":"application/json",
      "Content-Type": "application/x-www-form-urlencoded",
    },
  }
);
console.log(requestData);
</script>
<template>
  <div>
    <!-- Column Flex  -->
    <div class="flex flex-col items-center">
      <!-- Text  -->
      <div class="text-center text-3xl font-bold text-emerald-600 lg:text-4xl">
        Your Request has been submitted sucessfully. <br />
        <span class="text-2xl text-gray-900"
          >You will recieve registration SMS shortly.
          {{ pending ? "Loading" : data }}</span
        >
      </div>
    </div>
  </div>
</template>
