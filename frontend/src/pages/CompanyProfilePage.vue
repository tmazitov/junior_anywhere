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

				<FormCard width="240px">
					<h4>
						<Icon icon="tabler:filter" height="1.2em" color="var(--primary-color)"/>
						Filters
					</h4>
					<Filters v-model="filters" :fields="{
						search: true,
						employment: true,
						locations: true,
						salary: false,
						workFormat: true,
						degree: false,
						status: true,
					}"/>
				</FormCard>

				<BaseButton title="Log Out" @click="logOut"/>
			</div>
			<div class="main-content">
				<FormCard width="100%">
					<template v-slot:header>
						<div class="header-container">
							<h3>Active Vacancies</h3>
							<BaseButton title="Create" width="fit-content" primary
								@click="isCreateVacancy = true"/>
						</div>
					</template>
				</FormCard>
				<CompanyPersonalVacancyList v-if="vacancyList" 
				:vacancies="vacancyList"/>
			</div>
		</div>
	</div>
	<CreateVacancyModal v-model="isCreateVacancy" />
</div>
</template>

<script lang="ts" setup>
import NavigationBar from '../components/navigation-bar/NavigationBar.vue';
import FormCard from '../components/forms/FormCard.vue';
import BaseButton from '../components/inputs/BaseButton.vue';
import Vacancy from '../types/vacancy';
import CompanyPersonalVacancyList from '../components/vacancy-list/CompanyPersonalVacancyList.vue';
import { Icon } from '@iconify/vue/dist/iconify.js';
import { onMounted, ref, watch } from 'vue';
import Filters from '../components/vacancy-list/Filters.vue';
import VacancyListFilters from '../types/vacancyListFilters';
import { useRoute, useRouter } from 'vue-router';
import CreateVacancyModal from '../components/modals/CreateVacancyModal.vue';
import CompanyAuth from '../utils/authCompany';
import CompanyAPI from '../api/company/companyApi';

const companyId = CompanyAuth.getCompanyId()

const route = useRoute()

const isCreateVacancy = ref(false)

const filters = ref(new VacancyListFilters(route.query))
let timeout:number|null = null
const router = useRouter()

const vacancyList = ref<Vacancy[]|undefined>()
if (companyId) {
	CompanyAPI.vacancy.listByCompany(filters.value, companyId).then((res) => {
		vacancyList.value = res.data
	})
}


onMounted(() => {
	if (!CompanyAuth.getCompanyId()) {
		router.replace({name: "auth"})
		return
	}
})

watch(() => filters.value, () => {
	
	if (timeout) {
		clearTimeout(timeout)
	} 
	
	timeout = setTimeout(() => {
		const query = filters.value.toQuery()
		if (companyId) {
			CompanyAPI.vacancy.listByCompany(filters.value, companyId).then((res) => {
				vacancyList.value = res.data
			})
		}
		router.replace({name: 'company-profile', query})
	}, 200)
}, {deep: true})
                                       
const logOut = () => {
	CompanyAuth.delCompanyId()
	router.replace({name: "auth"})
}

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

.header-container{
	display: flex;
	flex-direction: row;
	gap: 16px;
	width: 100%;
	justify-content: space-between;
	align-items: center;
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

h4 {
	display: flex;
	flex-direction: row;
	gap:10px;
	align-items:center;
}
</style>