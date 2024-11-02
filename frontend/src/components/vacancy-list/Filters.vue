<template>

	<!-- Search -->

	<BaseInput :left-icon="icons['search']" placeholder="Search" 
	v-model="filters.search"/>

	<!-- Employment type -->
	
	<BaseSelect icon="tabler:briefcase" 
		placeholder="Employment" 
		:items="employments" 
		v-model="filters.employments"
		with-multiselect/>

	<!-- Locations -->

	<BaseSelect icon="tabler:map-pin" 
		placeholder="Locations" 
		:items="locations" 
		v-model="filters.locations"
		with-multiselect with-search/>

	<!-- With salary -->

	<BaseCheckbox v-model="filters.withSalary" label="With salary"/>

	<!-- Salary range -->
		
	<transition name="show">
		<BaseRange v-if="filters.withSalary" 
		v-model="filters.salaryRange" label="Salary range"
		:min="0" :max="10000" :step="100"/>
	</transition>

	<!-- Work Format -->
	<BaseSelect icon="tabler:calendar" 
		placeholder="Work format" 
		:items="workFormats" 
		v-model="filters.workFormats"
		with-multiselect/>
	
	<!-- With remote -->

	<BaseCheckbox v-model="filters.degreeIsRequired" label="Degree is required"/>

	
</template>

<script setup lang="ts">
import VacancyListFilters from '../../types/vacancyListFilters';
import locations from '../../info/locations';
import workFormats from '../../info/workFormats';
import employments from '../../info/employments';

import BaseInput from '../inputs/BaseInput.vue';
import BaseRange from '../../components/inputs/BaseRange.vue';	
import BaseSelect from '../../components/inputs/BaseSelect.vue';
import BaseCheckbox from '../inputs/BaseCheckbox.vue';

const icons = {
	"search" : {
		name: "tabler:search",
	},
}

const filters = defineModel<VacancyListFilters>({required:true})
</script>

<style scoped>
.show-enter-active{
	animation: open .35s ease-in-out;	
}
.show-leave-active{
	animation: open .35s ease-in-out reverse;	
}

@keyframes open {
	from {
		max-height: 0;
		opacity: 0;
	}

	to {
		max-height: 100%;
		opacity: 1;
	}
}
</style>