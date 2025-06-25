<template>
  <div class="book-detail">
    <h1>图书详情</h1>
    <!-- 这里添加图书详情展示内容 -->
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const bookId = ref(route.params.id)
const bookDetail = ref({})

onMounted(async () => {
  // 这里添加获取图书详情的 API 调用
  // bookDetail.value = await getBookDetail(bookId.value)
})
</script>

<style scoped>
.book-detail {
  padding: 20px;
}
</style>