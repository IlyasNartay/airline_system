<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-md max-w-md w-full text-center">
      <h1 class="text-3xl font-bold text-green-600 mb-4">✅ Бронирование подтверждено!</h1>
      <p class="text-gray-700 mb-2">Ваш код бронирования:</p>
      <div class="text-2xl font-mono bg-gray-100 p-4 rounded border border-dashed border-green-400 text-green-800 mb-6">
        {{ bookingCode }}
      </div>
      <router-link to="/" class="inline-block bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded transition">
        На главную
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const bookingCode = route.params.code || 'Неизвестно'
</script>
