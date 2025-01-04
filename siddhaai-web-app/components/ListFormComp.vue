<script setup>
// define props
const { inputArray, nextPageLink, title, nextButton } = defineProps({
  inputArray: [Object],
  nextPageLink: String,
  title: String,
  nextButton: Boolean,
});
defineEmits(["emitValue"]);
</script>
<template>
  <div>
    <!-- Only render on the client-side -->
    <ClientOnly>
      <div class="flex flex-col space-y-8 px-2 py-4 lg:items-center">
        <!-- title for form  -->
        <div
          class="text-center text-3xl font-bold text-emerald-600 lg:text-5xl"
        >
          {{ title }}
        </div>
        <!-- main component  -->
        <div class="grid w-full grid-cols-1 gap-y-6 lg:w-96">
          <!-- Iterate over inputArray items -->
          <div v-for="item in inputArray" :key="item">
            <!-- Render SelectOption component if type is 'select' -->
            <SelectOption
              v-if="item.type === 'select'"
              v-bind="item"
              @emit-value="(newValue) => {
                $emit('emitValue', item.inputName, newValue);
              }"
            />
            <!-- Render SingleInput component for other types -->
            <SingleInput
              v-else
              v-bind="item"
              @emit-value="
                (newValue) => {
                  console.log(newValue);
                  $emit('emitValue', item.inputName, newValue);
                }
              "
            />
          </div>
        </div>
        <!-- next and back button row  -->
        <div v-if="nextButton" class="flex flex-row justify-center space-x-8">
          <!-- Render BackButton Component  -->
          <BackButton />
          <!-- Render NextButton with Nuxt Link  -->
          <NuxtLink :to="nextPageLink">
            <PrimaryButton>Next</PrimaryButton>
          </NuxtLink>
        </div>
      </div>
    </ClientOnly>
  </div>
</template>
