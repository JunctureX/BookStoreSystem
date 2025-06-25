<template>
  <div>
    <el-table :data="users" style="width: 100%">
      <!-- 假设 User 表有 id、name、email 等字段，可按需修改 -->
      <el-table-column prop="id" label="ID" />
      <el-table-column prop="username" label="用户名" />
      <el-table-column prop="email" label="邮箱" />
      <el-table-column prop="phone" label="电话" />
      <el-table-column prop="user_type" label="角色" />
      <!-- 添加操作列 -->
      <el-table-column label="操作">
        <template #default="{ row }">
          <el-button @click="goToModify(row.id)">修改</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[10, 20, 30, 40]"
      :page-size="pageSize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getUsersPaginated } from '@/api/index'; // 导入新的分页 API
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

const router = useRouter();
const store = useStore();

const users = ref([]);
const currentPage = ref(1);
const pageSize = ref(20);
const total = ref(0);

const fetchUsers = async () => {
  try {
    const response = await getUsersPaginated(currentPage.value, pageSize.value);
    users.value = response.data.users;
    total.value = response.data.total;
  } catch (error) {
    console.error('获取用户列表失败:', error);
  }
};

const handleSizeChange = (newSize) => {
  pageSize.value = newSize;
  fetchUsers();
};

const handleCurrentChange = (newPage) => {
  currentPage.value = newPage;
  fetchUsers();
};

const goToModify = (id) => {
  store.dispatch('set_modifyid', id);
  router.push(`/index/modify`);
};

onMounted(() => {
  fetchUsers();
});
</script>

<style scoped>
/* 可添加自定义样式 */
</style>