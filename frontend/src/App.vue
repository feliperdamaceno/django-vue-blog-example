<script setup lang="ts">
import type { Post } from './@types'
import { PostCard } from './components'

const posts: Post[] = [
  {
    title: 'Lorem ipsum dolor sit',
    body: 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Culpa eaque nostrum ut autem dolorum tenetur corporis, velit ratione voluptas ad dolor ea animi repudiandae dignissimos saepe inventore voluptatibus, error sunt. Eveniet aliquam, dolores quia nisi eius odio asperiores explicabo quo? Voluptas obcaecati veritatis aut, magnam ullam culpa consectetur numquam tempora.',
    thumbnail: 'https://picsum.photos/800/600'
  },
  {
    title: 'Vero dolorum labore dolorem',
    body: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus, deleniti quam! Perspiciatis doloremque repellendus blanditiis cum esse possimus placeat, recusandae, quas error mollitia maxime. Vero dolorum labore dolorem quod quisquam voluptas accusantium dignissimos similique amet.',
    thumbnail: 'https://picsum.photos/799/600'
  },
  {
    title: 'Lorem ipsum dolor sit',
    body: 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Culpa eaque nostrum ut autem dolorum tenetur corporis, velit ratione voluptas ad dolor ea animi repudiandae dignissimos saepe inventore voluptatibus, error sunt. Eveniet aliquam, dolores quia nisi eius odio asperiores explicabo quo? Voluptas obcaecati veritatis aut, magnam ullam culpa consectetur numquam tempora.',
    thumbnail: 'https://picsum.photos/798/600'
  },
  {
    title: 'Vero dolorum labore dolorem',
    body: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus, deleniti quam! Perspiciatis doloremque repellendus blanditiis cum esse possimus placeat, recusandae, quas error mollitia maxime. Vero dolorum labore dolorem quod quisquam voluptas accusantium dignissimos similique amet.',
    thumbnail: 'https://picsum.photos/799/600'
  },
  {
    title: 'Lorem ipsum dolor sit',
    body: 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Culpa eaque nostrum ut autem dolorum tenetur corporis, velit ratione voluptas ad dolor ea animi repudiandae dignissimos saepe inventore voluptatibus, error sunt. Eveniet aliquam, dolores quia nisi eius odio asperiores explicabo quo? Voluptas obcaecati veritatis aut, magnam ullam culpa consectetur numquam tempora.',
    thumbnail: 'https://picsum.photos/797/600'
  },
  {
    title: 'Vero dolorum labore dolorem',
    body: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus, deleniti quam! Perspiciatis doloremque repellendus blanditiis cum esse possimus placeat, recusandae, quas error mollitia maxime. Vero dolorum labore dolorem quod quisquam voluptas accusantium dignissimos similique amet.',
    thumbnail: 'https://picsum.photos/796/600'
  }
]
</script>

<template>
  <main class="grid max-w-2xl gap-4 p-4 mx-auto">
    <template v-for="post in posts">
      <PostCard :post="post" />
    </template>
  </main>
</template>
