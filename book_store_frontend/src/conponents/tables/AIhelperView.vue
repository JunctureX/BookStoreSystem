<template>
    <el-card class="box-card">
        <template #header>
            <div class="card-header">
                <span>小助手</span>
                
            </div>
        </template>
        <el-col>
            <el-input v-model="userInput" placeholder="请输入您的问题" @keyup.enter="sendMessage"></el-input>
            <el-button @click="sendMessage">发送</el-button>
<el-button @click="clearMessages">清空记录</el-button>
            <el-card v-for="(msg, index) in messages" :key="index" class="message-card">
                <template #header>
                    <div class="message-header">
                        <span>{{ msg.sender }}</span>
                    </div>
                </template>
                <p>{{ msg.content }}</p>
            </el-card>
        </el-col>
    </el-card>
</template>


<script setup>
import { ref } from 'vue';
import { deepseek } from '@/api/index';

const userInput = ref('');
const messages = ref([
    { sender: '系统', content: '您好！有什么可以帮助您的？' }
]);

const clearMessages = () => {
    messages.value = [
        { sender: '系统', content: '您好！有什么可以帮助您的？' }
    ];
};

const sendMessage = async () => {
    if (userInput.value.trim()) {
        messages.value.push({ sender: '用户', content: userInput.value });
        try {
            const response = await deepseek(userInput.value).get();
            messages.value.push({ sender: 'AI', content: response.data.response });
        } catch (error) {
            messages.value.push({ sender: '系统', content: '抱歉，请求出错，请稍后再试。' });
        }
        userInput.value = '';
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

.card-header{
    display: flex;
    align-items: flex-start;
}

.content{
    text-align: start;
}

</style>