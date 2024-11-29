

<template>
	<router-view></router-view>
</template>

<script setup lang="ts">
import { onBeforeMount } from 'vue';
import CompanyAuth from './utils/authCompany';
import UserAuth from './utils/authUser';
import CompanyAPI from './api/company/api';
import CompanyInfo from './types/company';

onBeforeMount(() => {
	const companyId = CompanyAuth.getCompanyId();
	const userId = UserAuth.getUserId();
	if (companyId && !userId) {
		CompanyAuth.setupInfo(companyId)
	}
	if (!companyId && userId) {

	}
})
</script>

<style scoped>

</style>
