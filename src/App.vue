<script setup>
import { createRouter, createWebHistory } from 'vue-router';
import { onMounted } from 'vue'; // 引入生命周期方法

import AsicSearch from './components/AsicSearch.vue';
import AustralianSearch from './components/AustralianSearch.vue';
import RiskCheck from './components/RiskCheck.vue';

// Define router
const routes = [
  { path: '/', redirect: '/asic-search' }, 
  { path: '/asic-search', component: AsicSearch },
  { path: '/australian-search', component: AustralianSearch },
  { path: '/risk-check', component: RiskCheck },
];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 挂载 Vue 实例时添加路由
onMounted(() => {
  const app = createApp({
    setup() {
      // 这里可以做一些全局级别的初始化设置
    },
  });
  app.use(router).mount('#app');
});
</script>

<template>
  <div id="app">
    <router-view></router-view>
  </div>
  <header>
    

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}



@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
