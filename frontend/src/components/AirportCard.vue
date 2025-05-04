<template>
  <router-link :to="`/airport/${airport.code}`" class="block">
    <div class="bg-white rounded-2xl shadow p-4 hover:shadow-lg transition">
      <h3 class="text-lg font-bold text-gray-800">{{ airport.city }}</h3>
      <p class="text-sm text-gray-500">Код: {{ airport.code }}</p>
    </div>
  </router-link>
</template>

<script setup>
defineProps({
  airport: Object
});
</script>
