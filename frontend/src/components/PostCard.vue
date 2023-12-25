<script setup lang="ts">
import { Post } from '../@types'
defineProps<{ post: Post }>()
</script>

<template>
  <div class="max-w-xl overflow-hidden bg-white rounded-md shadow-md">
    <img class="object-cover w-full max-h-60" :src="post.thumbnail" alt="" />
    <div class="p-6 space-y-2">
      <h2 class="text-xl font-medium">{{ post.title }}</h2>
      <p>{{ post.body.substring(0, 125) }}...</p>
    </div>
  </div>
</template>
