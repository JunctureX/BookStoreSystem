<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>管理员书籍列表</span>
      </div>
    </template>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="id" label="ID" />
      <el-table-column prop="title" label="书名" />
      <el-table-column prop="stock" label="库存" />
    </el-table>
  </el-card>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue';
import { adminBookList } from '@/api';

const tableData = ref([]);

onBeforeMount(async () => {
  try {
    const response = await adminBookList.get();
    tableData.value = response.data;
  } catch (error) {
    console.error('获取书籍列表失败:', error);
  }
});
</script>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>