<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>修改书籍库存</span>
      </div>
    </template>
    <el-form :model="form" label-width="120px" class="form-container">
      <el-form-item label="库存">
        <el-input v-model="form.stock" type="number" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="updateStock">保存</el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue';
import { useRoute } from 'vue-router';
import { adminBookStock } from '@/api';
import { ElMessage } from 'element-plus';

const route = useRoute();
const bookId = route.params.bookId;
const form = ref({ stock: 0 });

onBeforeMount(async () => {
  try {
    const response = await adminBookStock.get({ params: { bookId } });
    form.value.stock = response.data.stock;
  } catch (error) {
    console.error('获取书籍库存失败:', error);
  }
});

const updateStock = async () => {
  try {
    await adminBookStock.patch({ bookId }, { stock: form.value.stock });
    ElMessage.success('库存更新成功');
  } catch (error) {
    console.error('更新库存失败:', error);
    ElMessage.error('库存更新失败');
  }
};
</script>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.el-card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  margin: 20px auto;
  max-width: 500px;
}

.el-form-item {
  margin-bottom: 20px;
}

.el-input {
  width: 100%;
}

.el-button {
  transition: all 0.3s ease;
}

.el-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>