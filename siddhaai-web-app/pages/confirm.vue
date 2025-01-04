<script setup>
// Dummy Input Array 
const inputArray = [
  {
    inputName: "Last Name",
    type: "text",
    value: "Krishnan",
  },
  {
    inputName: "Middle Name",
    type: "text",
    value: "J",
  },
  {
    inputName: "First Name",
    type: "text",
    value: "Bhaarat",
  },
  {
    inputName: "Date of Birth ( dd-mm-yyyy )",
    type: "date",
    value: "2003-10-29",
  },
  {
    inputName: "Gender",
    type: "select",
    value: "Male",
  },
  {
    inputName: "House No",
    type: "text",
    value: "105",
  },
  {
    inputName: "Street Name",
    type: "text",
    value: "24th Street",
  },
  {
    inputName: "City",
    type: "text",
    value: "Anytown",
  },
  {
    inputName: "State",
    type: "select",
    value: "CA",
  },
  {
    inputName: "Zipcode",
    type: "text",
    value: "95818",
  },
  {
    inputName: "Insurance Group Number",
    type: "text",
    value: "12345",
  },
  {
    inputName: "Insurance Member ID",
    type: "text",
    value: "12345",
  },
  {
    inputName: "Emergency Contact Name",
    type: "text",
    value: "Arjun",
  },
  {
    inputName: "Emergency Contact Phone Number",
    type: "text",
    value: "+1 (444) 555 3333",
  },
  {
    inputName: "Emergency Contact Relationship",
    type: "text",
    value: "Friend",
  },
  {
    inputName: "Primary Care Doctor Name",
    type: "text",
    value: "Shamuga Priya Arumugam",
  },
  {
    inputName: "Primary Care Phone Number",
    type: "text",
    value: "+1 (444) 555 3333",
  },
  {
    inputName: "Primary Care Address",
    type: "text",
    value: "11, Street Name, City, State, Zipcode",
  },
  
];
</script>
<template>
  <div>
    <div class="flex flex-col items-center space-y-10 p-4">
      <!-- Render Progress Bar Component  -->
      <ProgressBarComp :step-value="6" />
      <!-- summary  -->
      <div class="grid grid-cols-2 gap-8 text-xl lg:text-2xl font-medium">
        <!-- Iterating Input Array  -->
        <template v-for="item in inputArray">
          <!-- Key  -->
          <div>{{ item.inputName }}</div>
          <!-- Value  -->
          <div class="text-emerald-500">{{ item.value }}</div>
        </template>
      </div>
      <!-- check box -->
      <div class="flex flex-row space-x-4 text-base text-gray-600">
        <!-- Check Box Input  -->
        <input type="checkbox" name="termsCheck" id=""
          class="h-5 w-5 transition duration-200 ease-in-out checked:text-emerald-500 checked:ring-emerald-700" />
        <!-- Label terms and conditon  -->
        <label for="termsCheck">I agree to the
          <!-- Terms and Conditions Page Dummy Link  -->
          <a href="https://www.google.com" target="_blank" class="text-emerald-500 underline">Terms and
            Conditions</a></label>
      </div>
      <!-- button to submit  -->
      <div class="flex flex-row space-x-8">
        <!-- Renders Back Button  -->
        <BackButton />
        <!-- Submit Button with Nuxt Link  -->
        <NuxtLink to="success">
          <PrimaryButton> Submit </PrimaryButton>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
