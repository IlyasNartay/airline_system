<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="w-full max-w-sm bg-white p-6 rounded-xl shadow-md">
      <h1 class="text-2xl font-bold text-center text-blue-700 mb-5">📝 Регистрация</h1>
      <form @submit.prevent="register" class="space-y-4">
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700">Имя пользователя</label>
          <input
            v-model="username"
            type="text"
            id="username"
            placeholder="Введите имя"
            class="mt-1 block w-full p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none"
            required
          />
        </div>

        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            v-model="email"
            type="email"
            id="email"
            placeholder="example@mail.com"
            class="mt-1 block w-full p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none"
            required
          />
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <input
            v-model="password"
            type="password"
            id="password"
            placeholder="Введите пароль"
            class="mt-1 block w-full p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none"
            required
          />
        </div>

        <div>
          <label for="password2" class="block text-sm font-medium text-gray-700">Повторите пароль</label>
          <input
            v-model="password2"
            type="password"
            id="password2"
            placeholder="Повторите пароль"
            class="mt-1 block w-full p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none"
            required
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2.5 rounded-lg transition"
        >
          ✅ Зарегистрироваться
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { registerUser } from '../api'
import { useRouter } from 'vue-router'

const username = ref('')
const email = ref('')
const password = ref('')
const password2 = ref('') // добавлено

const router = useRouter()

async function register() {
  try {
    await registerUser({
      username: username.value,
      email: email.value,
      password: password.value,
      password2: password2.value
    })
    alert('Успешно зарегистрировано!')
    router.push('/login')
  } catch (error) {
    alert('Ошибка регистрации: ' + (error.response?.data?.message || 'Проверьте данные'))
  }
}
</script>
