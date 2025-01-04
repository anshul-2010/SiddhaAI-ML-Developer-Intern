<script setup></script>
<template>
  <div>
    <!-- button with slot for text  -->
    <button
      class="rounded-lg bg-emerald-600 p-3 text-2xl font-semibold tracking-wider text-white shadow-xl hover:bg-emerald-700 hover:shadow-sm"
    >
      <slot /> <!-- Text will be placed here-->
    </button>
  </div>
</template>
