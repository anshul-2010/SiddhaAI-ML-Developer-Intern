<script setup>
</script>
<template>
  <div>
    <!-- form  -->
    <div class="flex flex-col items-center justify-center space-y-8 p-4 text-emerald-500 lg:space-y-4">
      <!-- title  -->
      <div class="font-primary text-center text-3xl lg:text-4xl font-bold">
        New Patient Request Form
      </div>
      <!-- bread crumbs or progess  -->
      <ProgressBarComp :step-value="1" />
      <!-- title for this page -->
      <div class="font-primary text-center text-2xl font-normal text-gray-700 lg:text-4xl">
        Please upload government issued ID such as
        <span class="font-semibold"> Driving License </span> or
        <span class="font-semibold"> State ID </span>
      </div>
      <!-- file box  -->
      <FileInput input-name="License" />
      <!-- button to next page and previous page -->
      <div class="flex flex-row justify-center space-x-8">
        <BackButton text="Cancel" />
        <NuxtLink to="/personalDetails">
          <PrimaryButton>Submit</PrimaryButton>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
