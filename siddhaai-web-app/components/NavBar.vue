<script setup>
// Image Link 
const imgLink =
  "https://p1.hiclipart.com/preview/806/297/131/ubuntu-dock-icons-temporary-files-temp-text-on-black-background-png-clipart.jpg";

// Array of contact information 
const contactArray = [
  {
    icon: "ic:baseline-mail",
    text: "Email",
  },
  {
    icon: "ic:baseline-local-phone",
    text: "Call us",
  },
];
</script>
<template>
  <div>
    <!-- Row flex  -->
    <div
      class="mb-6 flex flex-row justify-between bg-emerald-600 p-2 text-white shadow-md lg:mb-10"
    >
      <!-- Logo part  -->
      <div class="flex flex-row items-center space-x-4">
        <!-- Image  -->
        <div>
          <img
            :src="imgLink"
            alt=""
            class="h-14 w-14 rounded-full object-cover object-center"
          />
        </div>
        <!-- Name  with nuxt link to home page -->
        <NuxtLink to="/">
          <div class="text-4xl font-semibold">Temp Health</div>
        </NuxtLink>
      </div>
      <!-- Contact part  -->
      <div class="flex flex-row items-center space-x-4 mx-4">
        <!-- Iterate over Contact Array  -->
        <div
          v-for="item in contactArray"
          class="rounded-lg px-2 py-1 text-center text-base transition hover:scale-105 hover:bg-white hover:text-pink-500"
        >
          <!-- Icon -->
          <Icon :name="item.icon" size="2em" class="" />
          {{ item.text }} <!-- Text --> 
        </div>
      </div>
    </div>
  </div>
</template>
