

<template>
	<router-view></router-view>
</template>

<script setup lang="ts">
import { onBeforeMount } from 'vue';
import CompanyAuth from './utils/authCompany';
import UserAuth from './utils/authUser';
import CompanyAPI from './api/company/companyApi';
import CompanyInfo from './types/company';

onBeforeMount(() => {
	const companyId = CompanyAuth.getCompanyId();
	const userId = UserAuth.getUserId();
	if (companyId && !userId) {
		CompanyAPI.info.general(companyId).then((res) => {
			if (res.status >= 400) {
				throw new Error('Get company info failed')
			}
			const data = res.data
			CompanyAuth.info = new CompanyInfo(data)
		})
	}
	if (!companyId && userId) {

	}
})
</script>

<style scoped>

</style>
