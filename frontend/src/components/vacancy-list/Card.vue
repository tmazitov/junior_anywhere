<template>
	<div class="vacancy-card">
		<div class="vacancy-card__company-name">
			{{ vacancy.companyName }}
		</div>

		<div class="vacancy-card__name">
			{{ vacancy.name }}
		</div>
		<div class="vacancy-card__footer">
			<div class="vacancy-card__info">
				<Icon icon="tabler:map-pin" height="16px"/>
				{{ vacancy.city }}
			</div>

			<div class="vacancy-card__info">
				{{ vacancy.salary }} AED
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import Vacancy from '../../types/vacancy';
import { defineProps } from 'vue';
import { Icon } from '@iconify/vue/dist/iconify.js';

defineProps({
	vacancy : {
		type: Vacancy,
		required: true
	}
})

</script>

<style scoped>
.vacancy-card {
	width: 100%;
	padding: 12px;
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

.vacancy-card__company-name{
	margin-bottom: 10px;
}

.vacancy-card__name {
	font-size: 20px;
	font-weight: 500;
	margin-bottom: 20px;
}

.vacancy-card__footer{
	display: flex;
	flex-direction: row;
	justify-content: space-between;
}

.vacancy-card__info{
	padding: 4px 10px 4px 6px;
	border-radius: 4px;
	background: var(--input-background);
	width: fit-content;
	display: flex;
	flex-direction: row;
	align-items: center;
	gap: 4px;
	user-select: none;
}

</style>