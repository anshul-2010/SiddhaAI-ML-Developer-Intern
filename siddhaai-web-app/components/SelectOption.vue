<script setup>
// Define Props 
const { inputName, value } = defineProps({
  inputName: String,
  value: Array,
  required: {
    type: Boolean,
    default: true,
  }
});
const refValue = ref(value);
defineEmits(["emitValue"]);
</script>
<template>
  <div class="flex flex-col items-start justify-start space-y-4 ">
    <!-- Label for the select option  -->
    <label for="genderSelect" class="text-xl font-semibold">{{
      inputName
    }} <!-- inputName props is passed here -->
    <!-- Required red * -->
      <span v-if="required" class="text-red-600 font-bold">*</span>
    </label>
    <!-- Select options  -->
    <select class="w-full form-select block font-medium rounded-md border-2 border-emerald-400 bg-zinc-100 py-3 text-lg"
      name="genderSelect" v-model="refValue" @change="$emit('emitValue',refValue)">
      <!-- Iterating value array  -->
      <option v-for="item in value" :key="item" :value="item">
        {{ item }}
      </option>
    </select>
  </div>
</template>
