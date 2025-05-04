<template>
  <div class="p-8 max-w-3xl mx-auto">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">✈️ Информация о рейсе</h1>

    <div v-if="loading" class="text-lg text-gray-500">Загрузка...</div>

    <div v-else class="bg-white p-8 rounded-3xl shadow-xl space-y-6">
      <div class="text-2xl font-semibold text-blue-700">
        Маршрут: {{ flight.origin }} → {{ flight.destination }}
      </div>

      <div class="grid grid-cols-2 gap-6 text-lg text-gray-700">
        <div class="flex items-center">
          <span class="mr-3 text-2xl">⏱️</span>
          Длительность:
          <span class="ml-auto font-bold">{{ flight.duration }} мин</span>
        </div>
        <div class="flex items-center">
          <span class="mr-3 text-2xl">🪑</span>
          Свободных мест:
          <span class="ml-auto font-bold">{{ availableSeats }}</span>
        </div>
        <div class="flex items-center">
          <span class="mr-3 text-2xl">📦</span>
          Вместимость:
          <span class="ml-auto font-bold">{{ flight.capacity }}</span>
        </div>
      </div>

      <div v-if="token">
        <button
          @click="book"
          class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 text-lg rounded-xl transition w-full"
        >
          📩 Забронировать место
        </button>
      </div>
      <div v-else class="text-base text-gray-500 italic">
        Для бронирования необходимо войти в систему.
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { fetchFlightDetails, bookFlight } from '../api.js'
import router from "../router.js";

const route = useRoute()
const flight = ref({})
const availableSeats = ref(0)
const loading = ref(true)
const token = localStorage.getItem('token')

onMounted(async () => {
  const data = await fetchFlightDetails(route.params.id)
  flight.value = data.flight
  availableSeats.value = data.available_seats
  loading.value = false
})

async function book() {
  try {

    await router.push(`/booking-form/${flight.value.id}`)
  } catch (err) {
    alert('Ошибка при бронировании')
  }
}
</script>
