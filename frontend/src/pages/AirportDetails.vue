<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Аэропорт: {{ airport?.city }} ({{ airport?.code }})</h1>

    <div v-if="loading">Загрузка...</div>
    <div v-else>
      <section class="mb-6">
        <h2 class="text-lg font-semibold mb-2">Прибытия</h2>
        <ul class="space-y-2">
          <FlightCard
          v-for="flight in arrivals"
          :key="flight.id"
          :flight="flight"
        />
        </ul>
      </section>

      <section>
        <h2 class="text-lg font-semibold mb-2">Вылеты</h2>
        <ul class="space-y-2">
          <FlightCard
          v-for="flight in departures"
          :key="flight.id"
          :flight="flight"
        />
        </ul>
      </section>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { fetchAirportDetails } from '../api.js'
import { useRoute } from 'vue-router';
import FlightCard from "../components/FlightCard.vue";

const route = useRoute();
const airport = ref(null);
const arrivals = ref([]);
const departures = ref([]);
const loading = ref(true);

onMounted(async () => {
  const { code } = route.params;
  try {
    const res = await fetchAirportDetails(code);
    airport.value = res.airport;
    arrivals.value = res.arrivals;
    departures.value = res.departures;
  } catch (err) {
    console.error('Ошибка при загрузке деталей аэропорта', err);
  } finally {
    loading.value = false;
  }
});
</script>
