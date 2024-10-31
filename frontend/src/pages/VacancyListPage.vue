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
					<ContentBlock style="flex:1; max-height: 450px" class="desktop more-filters">
						<h4>Filters</h4>
						<BaseSelect icon="tabler:briefcase" 
							placeholder="Employment" 
							:items="employments" 
							v-model="filters.employments"
							with-multiselect/>
						<BaseSelect icon="tabler:map-pin" 
							placeholder="Locations" 
							:items="locations" 
							v-model="filters.locations"
							with-multiselect with-search/>
						Todo: add checkbox "salary is defined"<br/>
						Todo: add checkbox "degree is required" 
					</ContentBlock>
				</div>
				<div class="block">
					<ContentBlock class="filters">
						<BaseInput :left-icon="icons['search']" placeholder="Search" 
							v-model="filters.search"/>
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
import BaseSelect from '../components/inputs/BaseSelect.vue';
import BaseInput from '../components/inputs/BaseInput.vue';
import ContentBlock from '../components/ContentBlock.vue';
import NavigationBar from '../components/navigation-bar/NavigationBar.vue';
import locations from '../info/locations';
import BaseIconButton from '../components/inputs/BaseIconButton.vue';
import VacancyListFilters from '../types/vacancyListFilters';
import { useRoute } from 'vue-router';
import employments from '../info/employments';
import router from '../router';

const mobileFiltersIsOpen = ref(false)
const toggleMobileFilters = () => {
	mobileFiltersIsOpen.value = !mobileFiltersIsOpen.value;
}

const route = useRoute()
const filters = ref(new VacancyListFilters(route.query))

const icons = {
	"search" : {
		name: "tabler:search",
	},
}

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