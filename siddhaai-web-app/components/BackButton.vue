<script setup>
// Define props and their default values
let { text } = defineProps({
  text:{
    type:String,
    default:"Back"
  }
})

// Function to navigate back
function goBack() {
  return useRouter().back();
}
</script>

<template>
  <div>
    <!-- Button to go back -->
    <button
      @click="goBack"
      class="rounded-lg p-3 text-justify text-2xl font-semibold text-white bg-red-500 shadow-lg hover:shadow-none"
    >
      {{ text }} <!-- Display the text prop -->
    </button>
  </div>
</template>
