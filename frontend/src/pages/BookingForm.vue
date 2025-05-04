<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded shadow">
    <h2 class="text-xl font-bold mb-4">Бронирование рейса</h2>
    <form @submit.prevent="submitBooking">
      <div class="mb-4">
        <label for="name" class="block text-gray-700 mb-1">Имя</label>
        <input
          v-model="form.name"
          type="text"
          id="name"
          class="w-full border border-gray-300 rounded px-3 py-2"
          required
        />
      </div>
      <div class="mb-4">
        <label for="email" class="block text-gray-700 mb-1">Email</label>
        <input
          v-model="form.email"
          type="email"
          id="email"
          class="w-full border border-gray-300 rounded px-3 py-2"
          required
        />
      </div>
      <button
        type="submit"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Забронировать
      </button>
    </form>

    <div v-if="successMessage" class="mt-4 text-green-600">
      {{ successMessage }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { bookFlight } from '../api.js'

const form = ref({
  name: '',
  email: ''
})

const successMessage = ref('')
const route = useRoute()
const router = useRouter()

const submitBooking = async () => {
  try {
    const response = await bookFlight(
      form.value.email,
      form.value.name,
      route.params.id
    )

    const bookingCode = response.booking_code
    await router.push(`/booking-confirmation/${bookingCode}`)
  } catch (error) {
    console.error('Ошибка бронирования:', error)
    successMessage.value = 'Произошла ошибка при бронировании.'
  }
}
</script>

