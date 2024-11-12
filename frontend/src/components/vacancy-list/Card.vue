<template>
	<div class="vacancy-card">
		<div class="vacancy-card__subtitle" v-if="isCompanyView">
			<!-- <Icon icon="tabler:user" size="1.2em" color="var(--primary-color)" /> -->
			{{ vacancy.applies }} users
		</div>
		<div class="vacancy-card__subtitle" v-else>
			{{ vacancy.companyName }}
		</div>

		<div class="vacancy-card__title">
			{{ vacancy.name }}
		</div>
		<div class="vacancy-card__footer">

			<div class="vacancy-card__info">
				{{ vacancy.salary }} AED
			</div>

			<div class="vacancy-card__info">
				{{ getLocationName(vacancy.locationId)}}
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import Vacancy from '../../types/vacancy';
import { defineProps } from 'vue';
import { Icon } from '@iconify/vue/dist/iconify.js';
import locations from '../../info/locations';

defineProps({
	vacancy : {
		type: Vacancy,
		required: true,
	},
	isCompanyView:{
		type: Boolean,
		required: false,
	}
})


const getLocationName = (id:number) => {
    return locations.find(loc => loc.value == id)?.title
}


</script>

<style scoped>
.vacancy-card {
	width: 100%;
	padding: 16px;
	border-radius: 16px;
	box-sizing: border-box;

	position: relative;
	box-shadow: 0 0 14px -7px  var(--border-color);
	transition: box-shadow .3s;

	cursor: pointer;
}

@media (min-width: 868px) {
	.vacancy-card:hover {
		box-shadow: 0 0 14px -3px  var(--border-color);
	}
}

.vacancy-card + .vacancy-card {
	margin-top: 16px;
}

.vacancy-card__subtitle{
	display: flex;
	flex-direction: row;
	gap: 6px;
}

.vacancy-card__title {
	font-size: 20px;
	font-weight: 500;
	margin-bottom: 16px;
	margin-top: 12px;
}

.vacancy-card__footer{
	display: flex;
	flex-direction: row;
	gap: 16px;
}

.vacancy-card__info{
	border-radius: 4px;
	width: fit-content;
	display: flex;
	flex-direction: row;
	align-items: center;
	gap: 6px;
	user-select: none;
	color: #616161;
}

</style>