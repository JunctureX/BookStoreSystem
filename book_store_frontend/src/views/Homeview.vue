<script setup>
import HomeHeaderBar from "@/conponents/HomeHeaderBar.vue";
import MenuBar from "@/conponents/MenuBar.vue";
import Footer from "@/conponents/Footer.vue";
import {onBeforeUpdate, computed} from "vue";
import {useRoute, useRouter} from "vue-router";



const route = useRoute();

const props = defineProps({
  type: {
    type:String,
    default: 'user'
  },
})

let getQueryPage = computed(()=>{

  return props.type;
})

onBeforeUpdate(()=>{
})

const getView = computed(()=>{
  if(getQueryPage.value === 'user'){
    return UserView;
  }
  if(getQueryPage.value === 'author'){
    return AuthorView;
  }
  if(getQueryPage.value === 'book'){
    return BookView;
  }
  if(getQueryPage.value === 'book-copy'){
    return BookCopyView;
  }
  if(getQueryPage.value === 'borrow'){
    return BorrowView;
  }
  if(getQueryPage.value === 'about'){
    return AboutWe;
  }
})

</script>

<template>
  <el-container class="">

    <el-aside width="200px"><MenuBar /></el-aside>
    <el-container>
      <el-header><HomeHeaderBar /></el-header>
      <el-main><component :is="getView" /></el-main>
      <el-footer><Footer /></el-footer>
    </el-container>
  </el-container>
</template>

<style lang="scss" scoped>

.el-header,.el-footer{
  padding: 0;
}

.el-main{
  @include home-main();
}


</style>
