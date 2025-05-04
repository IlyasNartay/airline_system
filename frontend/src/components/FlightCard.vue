<template>
  <router-link :to="`/flight/${flight.id}`" class="block">
  <div class="bg-white rounded-2xl shadow p-4 hover:shadow-lg transition">
    <h3 class="text-lg font-bold text-gray-800 mb-2">
      Рейс №{{ flight.id }}
    </h3>
    <p class="text-sm text-gray-600">
      ⏱️ Длительность: <span class="font-medium">{{ flight.duration }} мин</span>
    </p>
    <p class="text-sm text-gray-500 mt-2">
      🛫 Откуда: {{ flight.origin }}<br />
      🛬 Куда: {{ flight.destination }}
    </p>
  </div>
  </router-link>
</template>

<script setup>
defineProps({
  flight: Object
});
</script>
