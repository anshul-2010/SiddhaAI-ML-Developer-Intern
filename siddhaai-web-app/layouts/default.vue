<script setup></script>
<template>
  <div class="flex h-screen flex-col space-y-2">
    <!-- Renders NavBar component -->
    <NavBar />
    <main>
      <slot />
    </main>
    <!-- Footer  -->
    <footer class="sticky top-[100vh] w-full bg-gray-900 font-semibold text-white">
      <!-- Center Container -->
      <div class="container mx-auto px-6 py-4">
        <!-- Text  -->
        <p class="text-center">Pervasive Health Support - Siddha AI</p>
      </div>
    </footer>
  </div>
</template>
