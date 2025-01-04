<script setup>
// Define props
const { inputName } = defineProps({
  inputName: String,
});

// Reactive variable to store the file name
const fileName = ref("");

// Function to handle file change event
function onFileChange(event) {
  fileName.value = event.target.files[0].name;
}
</script>

<template>
  <div
    class="relative flex w-full flex-col items-center justify-center space-y-4 rounded-lg border-2 border-dashed border-gray-400 px-6 py-8 lg:w-1/2 lg:px-16"
  >
    <!-- dummy label for accessibility  -->
    <label for="file--upload" class="hidden">Label for file upload</label>

    <!-- file input relative  -->
    <input
      name="file-upload"
      type="file"
      class="absolute inset-0 cursor-pointer opacity-0"
      @change="onFileChange"
    />

    <!-- capture or upload row  -->
    <div
      class="flex flex-col items-center justify-evenly text-center text-3xl font-semibold text-emerald-500 lg:flex-row lg:space-x-5"
    >
      <!-- capture text with icon  -->
      <div class="rounded-md p-3 text-center shadow-md border-2">
        <!-- icon -->
        <span>
          <Icon name="material-symbols:android-camera" class="text-2xl" />
        </span>
        Capture
      </div>

      <!-- or text  -->
      <div class="text-lg text-gray-500">or</div>

      <!-- upload text with icon  -->
      <div class="rounded-md p-3 text-center shadow-md border-2">
        <!-- icon -->
        <span>
          <Icon name="material-symbols:drive-folder-upload" class="text-3xl" />
        </span>
        Upload File
      </div>
    </div>

    <!-- card top and bottom  -->
    <div class="text-gray-700 font-light text-2xl">Card Top</div>
    <div class="w-full lg:w-1/2 items-center text-center p-5 bg-gradient-to-r from-gray-200 to-gray-100 rounded-xl">
      <Icon
        name="clarity:license-solid"
        class="text-center text-[15em] text-emerald-600"
      />
    </div>
    <div class="text-gray-700 font-light text-2xl">Card Bottom</div>

    <!-- file name  -->
    <p v-if="fileName" class="text-2xl">{{ fileName }}</p>
  </div>
</template>
