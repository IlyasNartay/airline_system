<template>
  <div class="min-h-screen bg-gray-100 text-gray-900">
    <Navbar />
    <router-view />
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
</script>
