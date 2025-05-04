<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="w-full max-w-md bg-white p-8 rounded-3xl shadow-xl">
      <h1 class="text-3xl font-bold text-center text-blue-700 mb-6">🔐 Вход в аккаунт</h1>
      <form @submit.prevent="login" class="space-y-5">
        <div>
          <label for="username" class="block text-base font-medium text-gray-700">Имя пользователя</label>
          <input
            v-model="username"
            type="text"
            id="username"
            placeholder="Введите имя"
            class="mt-2 block w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-400 focus:outline-none"
            required
          />
        </div>

        <div>
          <label for="password" class="block text-base font-medium text-gray-700">Пароль</label>
          <input
            v-model="password"
            type="password"
            id="password"
            placeholder="Введите пароль"
            class="mt-2 block w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-400 focus:outline-none"
            required
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl text-lg transition"
        >
          🚀 Войти
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { loginUser } from '../api'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const router = useRouter()

async function login() {
  try {
    await loginUser({ username: username.value, password: password.value })
    window.location.href = '/'
  } catch {
    alert('Неверные данные для входа')
  }
}
</script>
