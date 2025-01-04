<script setup></script>
<template>
  <div>
    <!-- form  -->
    <div
      class="flex flex-col items-center justify-center space-y-6 p-4 text-emerald-600"
    >
      <!-- title  -->
      <div class="text-center text-4xl font-semibold text-gray-900">
        Please upload your Insurance ID card now.
      </div>
      <!-- bread crumbs or progess  -->
      <ProgressBarComp :step-value="4" />
      <div class="text-3xl font-medium lg:text-4xl">Front Page</div>
      <!-- file box  -->
      <FileInput input-name="Insurance" />
      <div class="text-3xl font-medium lg:text-4xl">Back Page</div>
      <!-- file box  -->
      <FileInput input-name="Insurance" />

      <!-- button to next page -->
      <div class="flex flex-row space-x-8">
        <!-- Renders Back Button  -->
        <BackButton />
        <!-- Submit Button with Nuxt Link  -->
        <NuxtLink to="/insurance/verify">
          <PrimaryButton>Submit</PrimaryButton>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
