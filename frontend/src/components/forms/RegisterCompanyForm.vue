<template>
	<BaseInput v-model="form.name" :left-icon="icons['name']" placeholder="Company name"/>
	<BaseInput v-model="form.documentId" :left-icon="icons['doc']" placeholder="Company id"/>
	
	<BaseSelect v-model="form.companyType" icon="tabler:basket-question" :items="companyTypes"/>

	<BaseInput v-model="form.email" type="email" :left-icon="icons['email']" placeholder="Email"/>
	<BaseInput v-model="form.password" type="password" :left-icon="icons['pass']" placeholder="Password"/>


	<BaseCheckbox v-model="form.agree" label="I agree with terms and conditions"/>
</template>

<script setup lang="ts">
import { defineModel } from 'vue';
import RegisterCompany from '../../types/forms/registerCompany';
import BaseInput from '../inputs/BaseInput.vue';
import BaseCheckbox from '../inputs/BaseCheckbox.vue';
import BaseSelect from '../inputs/BaseSelect.vue';
import companyTypes from '../../info/companyType';

const form = defineModel<RegisterCompany>({required: true})
const icons = {
	name : {
		name: 'tabler:briefcase'
	},
	doc: {
		name: 'tabler:id'
	},
	email: {
		name: 'tabler:mail',
	},
	pass: {
		name: 'tabler:password',
	}
}

</script>