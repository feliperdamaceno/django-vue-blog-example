<script setup lang="ts">
import { PostCard } from './components'
import { usePosts } from './composables'

const { posts } = usePosts()
</script>

<template>
  <main class="grid max-w-2xl gap-4 p-4 mx-auto">
    <template v-for="post in posts">
      <PostCard :post="post" />
    </template>
  </main>
</template>
