<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>创建订单</span>
      </div>
    </template>
    <el-table :data="orderItems" style="width: 100%">
      <el-table-column prop="title" label="书名" width="200">
        <template #default="{ row, $index }">
          <el-autocomplete
            v-model="row.title"
            :fetch-suggestions="(queryString, cb) => fetchTitles(queryString, cb, $index)"
            placeholder="请输入书名"
            @select="(item) => selectTitle(item, $index)"
          ></el-autocomplete>
        </template>
      </el-table-column>
      <el-table-column prop="isbn" label="ISBN" width="200">
        <template #default="{ row, $index }">
          <el-autocomplete
            v-model="row.isbn"
            :fetch-suggestions="(queryString, cb) => fetchISBNs(queryString, cb, $index)"
            placeholder="请输入 ISBN"
            @select="(item) => selectISBN(item, $index)"
          ></el-autocomplete>
        </template>
      </el-table-column>
      <el-table-column prop="price" label="书籍单价" width="120" />
      <el-table-column prop="quantity" label="订购数量" width="120">
        <template #default="{ row }">
          <el-input-number v-model="row.quantity" :min="1" @change="calculateRowTotal(row)" />
        </template>
      </el-table-column>
      <el-table-column prop="total" label="订购总价" width="120" />
    </el-table>
    <el-button @click="addRow">添加行</el-button>
    <div style="text-align: right; margin-top: 20px;">
      <span>订单总价: {{ totalOrderPrice }}</span>
    </div>
    <div style="text-align: right; margin-top: 20px;">
      <el-button type="primary" @click="submitOrder">完成订单</el-button>
    </div>
  </el-card>
</template>

<script setup>
import { ref, computed } from 'vue';
import { searchBooksByTitle, searchBooksByISBN } from '@/api/index';

const orderItems = ref([{ title: '', isbn: '', price: 0, quantity: 1, total: 0 }]);

const totalOrderPrice = computed(() => {
  return orderItems.value.reduce((sum, item) => sum + item.total, 0);
});

const fetchTitles = async (queryString, cb, index) => {
  if (queryString) {
    try {
      const response = await searchBooksByTitle(queryString);
      const suggestions = response.data.map((book) => ({ value: book.title, book }));
      cb(suggestions);
    } catch (error) {
      console.error('获取书名建议失败:', error);
      cb([]);
    }
  } else {
    cb([]);
  }
};

const fetchISBNs = async (queryString, cb, index) => {
  if (queryString) {
    try {
      const response = await searchBooksByISBN(queryString);
      const suggestions = response.data.map((book) => ({ value: book.isbn, book }));
      cb(suggestions);
    } catch (error) {
      console.error('获取 ISBN 建议失败:', error);
      cb([]);
    }
  } else {
    cb([]);
  }
};

const selectTitle = (item, index) => {
  const book = item.book;
  orderItems.value[index].isbn = book.isbn;
  orderItems.value[index].price = book.price;
  orderItems.value[index].quantity = 1;
  calculateRowTotal(orderItems.value[index]);
};

const selectISBN = (item, index) => {
  const book = item.book;
  orderItems.value[index].title = book.title;
  orderItems.value[index].price = book.price;
  orderItems.value[index].quantity = 1;
  calculateRowTotal(orderItems.value[index]);
};

const calculateRowTotal = (row) => {
  row.total = row.price * row.quantity;
};

const addRow = () => {
  orderItems.value.push({ title: '', isbn: '', price: 0, quantity: 1, total: 0 });
};

const submitOrder = () => {
  // 检查所有书名和 ISBN 是否合法
  const isValid = orderItems.value.every((item) => item.title && item.isbn);
  if (isValid) {
    // 提交订单到后端
    console.log('提交订单:', orderItems.value);
    // 这里需要添加实际的后端请求逻辑
  } else {
    alert('请确保所有书名和 ISBN 都已正确填写。');
  }
};
</script>

<style lang="scss" scoped>
.message-card {
  margin-top: 10px;
}

.message-header {
  display: flex;
  align-items: flex-start;
}

.card-header {
  display: flex;
  align-items: flex-start;
}

.content {
  text-align: start;
}
  .el-table {
    th, td {
      box-sizing: border-box;
    }
  }
  .el-table {
    th, td {
      box-sizing: border-box;
      text-align: left; /* 确保文本左对齐 */
      padding: 0 18px; /* 统一表头和内容的内边距 */
    }
    /* 确保自动完成组件宽度与列宽一致 */
    .el-autocomplete {
      width: 100%;
    }
  }
</style>