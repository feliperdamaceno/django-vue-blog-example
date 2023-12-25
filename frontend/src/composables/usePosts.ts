import { ref, onMounted } from 'vue'
import { Post } from '../@types'

export default function usePosts() {
  const posts = ref<Post[]>([])

  onMounted(async () => {
    const API_URL = import.meta.env.VITE_API_URL
    const response = await fetch(API_URL)
    posts.value = await response.json()
  })

  return { posts }
}
