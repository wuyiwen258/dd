import { createRouter, createWebHistory } from 'vue-router';
import AsicSearch from '../components/AsicSearch.vue';
import AustralianSearch from '../components/AustralianSearch.vue';
import RiskCheck from '../components/RiskCheck.vue';

const routes = [
  { path: '/', redirect: '/asic-search' },
  { path: '/asic-search', component: AsicSearch },
  { path: '/australian-search', component: AustralianSearch },
  { path: '/risk-check', component: RiskCheck },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
