<template>
<div class="page">
		<div class="page-frame">
			<NavigationBar/>
			<div class="page-frame__content grid-container">
				<div class="side-menu">
					<FormCard width="240px">
						<template v-slot:header>
							<h2>Yandex</h2>
						</template>
						<template v-slot:default>
							<div class="support-message">
								LLC: test-llc-number
							</div>		
						</template>
					</FormCard>
					<FormCard width="240px">
						<div class="menu-list">
							<div class="menu-list__item active">
								<Icon icon="tabler:user" height="1.2em" color="var(--primary-color)"/>
								Vacancies
							</div>
							<div class="menu-list__item disabled">
								<Icon icon="tabler:folder" height="1.2em"/>
								Documents
							</div>
							<div class="menu-list__item disabled">
								<Icon icon="tabler:archive" height="1.2em"/>
								Archive
							</div>
						</div>
					</FormCard>
				</div>
				<div class="main-content">
					<FormCard width="100%">
						<template v-slot:header>
							<h3>Vacancies</h3>
						</template>
						<template v-slot:default>
							<div class="support-message">
								Hire new workers electively
							</div>
							<CompanyPersonalVacancyList :vacancies="vacancyList"/>
						</template>
						<template v-slot:footer>
							<BaseButton title="Create Vacancy" width="200px"/>
						</template>
					</FormCard>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import NavigationBar from '../components/navigation-bar/NavigationBar.vue';
import FormCard from '../components/forms/FormCard.vue';
import BaseButton from '../components/inputs/BaseButton.vue';
import Vacancy from '../types/vacancy';
import CompanyPersonalVacancyList from '../components/vacancy-list/CompanyPersonalVacancyList.vue';
import { Icon } from '@iconify/vue/dist/iconify.js';

const vacancyList:Vacancy[] = [
	new Vacancy({id: 1, name: "Super Duper Frontend developer", locationId:1, companyName: "Yandex", salary: 10000, applies: 195,}),
	new Vacancy({id: 2, name: "Super Duper Frontend developer", locationId:2, companyName: "Yandex", salary: 10000, applies: 131,}),
	new Vacancy({id: 3, name: "Super Duper Frontend developer", locationId:3, companyName: "Yandex", salary: 10000, applies: 73}),
	new Vacancy({id: 4, name: "Super Duper Frontend developer", locationId:4, companyName: "Yandex", salary: 10000, applies: 106}),
	new Vacancy({id: 5, name: "Super Duper Frontend developer", locationId:4, companyName: "Yandex", salary: 10000, applies: 106}),
	new Vacancy({id: 6, name: "Super Duper Frontend developer", locationId:4, companyName: "Yandex", salary: 10000, applies: 106}),
	new Vacancy({id: 7, name: "Super Duper Frontend developer", locationId:4, companyName: "Yandex", salary: 10000, applies: 106}),
	new Vacancy({id: 8, name: "Super Duper Frontend developer", locationId:4, companyName: "Yandex", salary: 10000, applies: 106}),
]

</script>

<style scoped>
@media (min-width:868px) {
	.grid-container {
		padding-top: 16px;
		align-items: center;
		max-width: 100%;
	}
	
}

.grid-container{
	display: grid;
	grid-template-columns: 240px 1fr;
	column-gap: 16px;
}

.content{
	display: flex;
	flex-direction: column;
	gap: 16px;
	height: 100%
}

.support-message{
	width: 100%;
	display: flex;
	align-items: center;
	color: #616161;
	font-size: 0.95em;
}

.blur-enter-active{
	animation: blur .3s;
}

.blur-leave-active{
	animation: blur .3s reverse;
}

@keyframes blur {
	from {
		opacity: 1;

	}
	to {
		opacity: 0;
	}
}

.support-message.block {
	color: var(--silver);
	text-align: center;
	height: 150px;
}

.profile-card{
	display: flex;
	flex-direction: column;
	gap: 16px;
}

.buttons{
	display: flex;
	flex-direction: row;
	gap: 16px;
}

.side-menu {
	display: flex;
	flex-direction: column;
	gap: 16px;
	height: 100%;
	justify-content: flex-start;

}

.main-content{
	display: flex;
	flex-direction: column;
	gap: 16px;
	height: 100%;
	justify-content: flex-start;
}

.menu-list{
	display: flex;
	flex-direction: column;
	gap: 16px;
}

.menu-list__item{
	display: flex;
	flex-direction: row;
	gap: 10px;
	cursor: pointer;
}

.menu-list__item.active{
	font-weight: 500;
}

.menu-list__item.disabled{
	color: var(--silver);
}
</style>