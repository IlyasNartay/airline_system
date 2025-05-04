<template>
  <div class="mt-20 px-4 pt-5 max-w-md mx-auto bg-white rounded-lg shadow">
    <h1 class="text-3xl font-bold mb-6 text-center">Управление бронированием</h1>

    <div class="mb-4">
      <label for="code" class="block text-sm font-medium text-gray-700">Код бронирования</label>
      <input
        v-model="code"
        type="text"
        id="code"
        class="mt-1 p-3 w-full border border-gray-300 rounded text-lg"
        placeholder="Введите код (например: ABC123)"
      />
    </div>

    <button
      @click="manage"
      :disabled="loading || !code"
      class="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded transition disabled:opacity-50"
    >
      {{ loading ? 'Поиск...' : 'Проверить' }}
    </button>

    <div v-if="booking" class="mt-6 bg-gray-50 p-4 rounded shadow-inner text-gray-800">
      <h2 class="text-lg font-semibold mb-2">Детали бронирования:</h2>
      <p><strong>Рейс:</strong> {{ booking.flight.origin }} → {{ booking.flight.destination }}</p>
      <p><strong>Пассажир:</strong> {{ booking.passenger.name }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { manageBooking } from '../api'

const code = ref('')
const booking = ref(null)
const loading = ref(false)

async function manage() {
  if (!code.value.trim()) return

  loading.value = true
  booking.value = null
  try {
    const data = await manageBooking(code.value.trim())
    booking.value = data
  } catch {
    alert('Бронирование не найдено')
  } finally {
    loading.value = false
  }
}
</script>
