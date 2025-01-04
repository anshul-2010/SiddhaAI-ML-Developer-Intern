<script setup>
// Step Value to know the current progress 
// Define Props 
const { stepValue } = defineProps({ stepValue: Number });
// Total no of steps n 
const n = 6;
</script>
<template>
  <div>
    <!-- Row flex  -->
    <div class="flex flex-row lg:scale-100 justify-center items-center">
      <!-- the full componenet circle with line  -->
      <div class="flex flex-row items-center" v-for="i in 5">
        <!-- Render the circle conditionally with color filled  -->
        <div
          v-if="i <= stepValue"
          class="rounded-full bg-emerald-600 px-4 py-2 text-center text-base font-bold text-white hover:bg-gray-200 hover:text-emerabg-emerald-600"
        >
          {{ i }}
        </div>
        <!-- Render circle conditionally with out color filled  -->
        <div
          v-else
          class=" rounded-full bg-gray-200 px-4 py-2 text-center text-base font-bold text-emerald-600 hover:bg-emerald-600 hover:text-white"
        >
          {{ i }}
        </div>
        <!-- Render the interconnecting line conditionally for color filling  -->
        <span v-if="i <= stepValue" class="h-2 w-5 lg:w-16 bg-emerald-600"></span>
        <span v-else class="h-2 w-5 lg:w-16 bg-gray-200"></span>
      </div>
      <!-- Render final step circle based on Step Value  -->
      <div
        v-if="n <= stepValue"
        class=" rounded-full bg-emerald-600 px-4 py-2 text-center text-base font-bold text-white hover:bg-gray-200 hover:text-emerabg-emerald-600"
      >
        {{ n }}
      </div>
      <div
        v-else
        class=" rounded-full bg-gray-200 px-4 py-2 text-center text-base font-bold text-emerald-600 hover:bg-emerald-600 hover:text-white"
      >
        {{n}}
      </div>
    </div>
  </div>
</template>
