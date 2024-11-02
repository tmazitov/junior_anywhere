<template>
	<div class="page">
		<div class="page-frame">
			<div class="page-frame__content  grid-container">
				<div class="block-child nav">
					<NavigationBar/>
				</div>
				<div class="block">
					<ContentBlock class="add" outlined>
						<div class="add-cover">
							<h3>Hard to make the CV?</h3>
							<div>Let our specialists help you to find your strong sides</div>
						</div>
					</ContentBlock>
					<ContentBlock class="desktop more-filters">
						<h4>Filters</h4>
						<Filters v-model="filters"/>
					</ContentBlock>
				</div>
				<div class="block">
					<ContentBlock class="filters mobile">
						<BaseIconButton class="mobile" 
							:icon="mobileFiltersIsOpen ? 'tabler:x' : 'tabler:filter'" 
							@click="toggleMobileFilters"/>
						<span class="mobile">
							<transition name="open">
								<div class="mobile-menu" v-if="mobileFiltersIsOpen"></div>
							</transition>
						</span>
					</ContentBlock>
					<ContentBlock style="flex:1;">Vacancy List</ContentBlock>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import ContentBlock from '../components/ContentBlock.vue';
import NavigationBar from '../components/navigation-bar/NavigationBar.vue';
import BaseIconButton from '../components/inputs/BaseIconButton.vue';
import VacancyListFilters from '../types/vacancyListFilters';
import { useRoute } from 'vue-router';
import router from '../router';
import Filters from '../components/vacancy-list/Filters.vue';


const mobileFiltersIsOpen = ref(false)
const toggleMobileFilters = () => {
	mobileFiltersIsOpen.value = !mobileFiltersIsOpen.value;
}

const route = useRoute()
const filters = ref(new VacancyListFilters(route.query))

watch(() => filters.value, () => {
	const query = filters.value.toQuery()
	router.replace({name: 'vacancy-list', query})
}, {deep: true})

</script>

<style scoped>
.filters{
	display: flex;
	flex-direction: row;
	gap: 10px;
	background: none;
	padding: 0;
	position: relative;
}

.filters > .base-input {
	width: max(30%, 220px);
	max-width: 300px;
	border-radius: 16px;
}

.more-filters {
	display: flex;
	flex-direction: column;
	gap: 16px;
	background: transparent;
	border: 1px solid var(--border-color);
	transition: height .3s;
}

.add {
	border-color: var(--primary-color);
	background: linear-gradient(90deg, var(--primary-color-opacity) 0%, var(--primary-color) 100%);
	padding: 0;
	overflow: hidden;
	cursor: pointer;
}

.add-cover {
	padding: 16px;
	height: 100%;
	box-sizing: border-box;
	background: rgba( 255, 255, 255, 0.15 );
	box-shadow: 0 8px 32px 0 rgba(162, 165, 199, 0.37);
	backdrop-filter: blur( 13px );
	-webkit-backdrop-filter: blur( 13px );
	border-radius: 10px;

	display: flex;
	flex-direction: column;
	gap: 12px;
}


.block {
	display: flex;
	flex-direction: column;
	gap: 16px;
}

.grid-container {
	display: grid;
	grid-template-columns: 240px 1fr;
	grid-template-rows: auto 1fr;
	grid-column-gap: 16px;
	grid-row-gap: 32px;
}

@media (max-width: 868px) {
	.grid-container {
		display: flex;
		flex-direction: column;
		gap: 16px;
	}
}

@media (max-width: 868px) {
	.desktop {
		display: none;
	}
}

@media (min-width: 868px) {
	.mobile {
		display: none;
	}
}

.nav { grid-area: 1 / 1 / 2 / 3; }
</style>