<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Аэропорты и Рейсы</h1>

    <!-- Показать промокод, если он есть -->
    <div v-if="!token"  class="bg-green-100 text-green-800 p-4 rounded mb-4">
      <strong>Ваш промокод: {{ promoCode }}</strong>
    </div>

    <div v-if="loading">Загрузка...</div>

    <div v-else>
      <h2 class="text-xl font-semibold mb-2">Аэропорты</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-6">
        <AirportCard
          v-for="airport in airports"
          :key="airport.code"
          :airport="airport"
        />
      </div>

      <h2 class="text-xl font-semibold mb-2">Рейсы</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <FlightCard
          v-for="flight in flights"
          :key="flight.id"
          :flight="flight"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref, onMounted, computed} from 'vue'
import { fetchIndex } from '../api.js'
import FlightCard from '../components/FlightCard.vue'
import AirportCard from "../components/AirportCard.vue";

const airports = ref([])
const flights = ref([])
const loading = ref(true)
const promoCode = localStorage.getItem('promo_code')
const token = computed(() => localStorage.getItem('token'))

onMounted(async () => {
  const data = await fetchIndex()
  airports.value = data.airports
  flights.value = data.flights
  loading.value = false
})
</script>
