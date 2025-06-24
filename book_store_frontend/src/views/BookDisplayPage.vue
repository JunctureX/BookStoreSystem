<template>
  <div class="book-display-page">
    <h1>书籍展示页面</h1>
    <div class="search-filters">
      <select v-model="selectedPublisher" @change="fetchBooks()">
        <option value="">所有出版社</option>
        <option v-for="publisher in publishers" :key="publisher.id" :value="publisher.id">
          {{ publisher.name }}
        </option>
      </select>
      <select v-model="selectedCategory" @change="fetchBooks()">
        <option value="">所有类别</option>
        <option v-for="category in categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
    </div>
    <div class="book-list">
      <div v-for="book in books" :key="book.id" class="book-item">
        <h2>{{ book.title }}</h2>
        <p>作者: {{ book.author }}</p>
        <p>价格: {{ book.price }}</p>
        <p>评分: {{ book.rating }}</p>
        <div class="reviews">
          <h3>评论</h3>
          <div v-for="review in book.reviews" :key="review.id" class="review-item">
            <p>评分: {{ review.rating }}</p>
            <p>评论: {{ review.comment }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const selectedPublisher = ref('');
const selectedCategory = ref('');
const books = ref([]);
const publishers = ref([]);
const categories = ref([]);

const fetchBooks = async () => {
  try {
    const response = await axios.get('/api/books', {
      params: {
        publisher: selectedPublisher.value,
        category: selectedCategory.value,
      },
    });
    books.value = response.data;
  } catch (error) {
    console.error('获取书籍数据失败:', error);
  }
};

const fetchPublishers = async () => {
  try {
    const response = await axios.get('/api/publishers');
    publishers.value = response.data;
  } catch (error) {
    console.error('获取出版社数据失败:', error);
  }
};

const fetchCategories = async () => {
  try {
    const response = await axios.get('/api/categories');
    categories.value = response.data;
  } catch (error) {
    console.error('获取类别数据失败:', error);
  }
};

onMounted(() => {
  fetchBooks();
  fetchPublishers();
  fetchCategories();
});
</script>

<style scoped>
.book-display-page {
  padding: 20px;
}
.search-filters {
  margin-bottom: 20px;
}
.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
.book-item {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
}
.reviews {
  margin-top: 10px;
}
.review-item {
  margin-bottom: 10px;
  padding: 5px;
  border: 1px solid #eee;
  border-radius: 3px;
}
</style>