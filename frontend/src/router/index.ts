import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
	{
		path: '/',
		name: 'home',
		component: () => import('../pages/HomePage.vue')
	},
	{
		path: '/auth',
		name: 'auth',
		component: () => import('../pages/AuthPage.vue')
	},
	{
		path: '/vacancy',
		name: 'vacancy-list',
		component: () => import('../pages/VacancyListPage.vue')
	}
];

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes
});

export default router;