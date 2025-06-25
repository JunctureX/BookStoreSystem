<template>
  <div class="book-detail">
    <h1>图书详情</h1>
    <div v-if="bookDetail" class="detail-container">
      <p><strong>ID:</strong> {{ bookDetail.id }}</p>
      <p><strong>书名:</strong> {{ bookDetail.title }}</p>
      <p><strong>作者:</strong> {{ bookDetail.author }}</p>
      <p><strong>出版社 ID:</strong> {{ bookDetail.publisher_id }}</p>
      <p><strong>库存数量:</strong> {{ bookDetail.stock_quantity }}</p>
      <p><strong>价格:</strong> {{ bookDetail.price }}</p>
      <p><strong>评分:</strong> {{ bookDetail.rating }}</p>
    </div>
    <div v-else class="loading">
      <p>加载中...</p>
    </div>
    <div class="recommendation-sidebar">
      <h2>为您推荐</h2>
      <ul>
        <li v-for="book in recommendedBooks" :key="book.id">
          {{ book.title }} - 评分: {{ book.rating }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { getBookDetail, userRecommendation } from '@/api/index'

const store = useStore()
const bookDetail = ref({})
const recommendedBooks = ref([])

onMounted(async () => {
  try {
    const detailId = store.state.detailid
    const response = await getBookDetail(detailId).get()
    bookDetail.value = response.data

    const userId = store.state.id
    const recommendationResponse = await userRecommendation(userId).get()
    const bookIds = recommendationResponse.data.map(item => item.id)

    for (const id of bookIds) {
      const bookResponse = await getBookDetail(id).get()
      recommendedBooks.value.push(bookResponse.data)
    }
  } catch (error) {
    console.error('获取图书详情或推荐失败:', error)
  }
})
</script>

<style scoped>
.book-detail {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}
.detail-container {
  border: 1px solid #eee;
  padding: 20px;
  border-radius: 8px;
}
.detail-container p {
  margin: 10px 0;
}
.loading {
  text-align: center;
  padding: 20px;
}
.recommendation-sidebar {
  position: fixed;
  right: 0;
  top: 0;
  width: 20%;
  height: 100vh;
  background-color: #f9f9f9;
  padding: 20px;
  overflow-y: auto;
}
</style>