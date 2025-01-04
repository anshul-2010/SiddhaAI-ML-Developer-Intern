<script setup lang="ts">
// Define Props 
let { inputName, type, value } = defineProps({
  inputName: String,
  type: String,
  value: String,
  required: {
    type: Boolean,
    default: true,
  },
});
defineEmits(["emitValue"])
const refValue = ref<String | undefined>(value);

</script>
<template>
  <div>
    <div class="flex flex-col space-y-2 rounded-md items-stretch">
      <!-- Label for the input field  -->
      <label
        :for="inputName"
        class="text-xl font-semibold"
        >{{ inputName }}
        <span v-if="required" class="font-bold text-red-600">*</span></label
      >
      <!-- Input field  -->
      <input
        :type="type"
        @change="$emit('emitValue',refValue)"
        class="rounded-lg border-2 border-emerald-500 py-3 bg-zinc-100 text-lg focus:border-blue-600"
        :name="inputName"
        v-model="refValue"
      />
      <!-- Label for edit button  -->
      <label
        :for="inputName"
        class="w-fit px-2 py-1 flex flex-row items-center rounded-md text-lg font-normal hover:bg-gray-100"
      >
        <!-- Edit Icon  -->
        <Icon name="mdi-light:pencil" size="2em" class="text-emerald-500" />
        Edit
      </label>
    </div>
  </div>
</template>
