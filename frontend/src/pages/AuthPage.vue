<template>
	<div class="page">
		<div class="page-frame centered">
			<div class="page-frame__content">
				<div class="card">
					<div class="card-header">
						<BaseIconButton icon="tabler:arrow-back-up"
							@click="navigateToBack"
							fill="clear"/>
						<div class="card-header__title">Sign In</div>	
					</div>
					<div class="card-content">
						<BaseInput v-model="email" type="email" ref="emailField"
							:left-icon="icons['email']"
							placeholder="Email"/>
						<BaseInput v-model="password" type="password" ref="passwordField" 
							:left-icon="icons['pass']" 
							placeholder="Password"/>
						<a href="">Forget password</a>
						<a href="">Register account</a>
					</div>
					<div class="card-footer">
						<BaseButton title="Continue" primary/>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">

import { ref } from 'vue';
import BaseInput from '../components/inputs/BaseInput.vue';
import BaseButton from '../components/inputs/BaseButton.vue';
import BaseIconButton from '../components/inputs/BaseIconButton.vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const navigateToBack = () => {
	router.back();
}

const email = ref('');
const emailField = ref<HTMLElement|null>(null)
const password = ref('');
const passwordField = ref<HTMLElement|null>(null)

const icons = {
	'email' : {
		name: 'tabler:mail',
	},
	'pass' : {
		name: 'tabler:key',
	}
}

</script>

<style scoped>

.centered {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}

.card{
	width: 100%;
	border-radius: 16px;
	box-sizing: border-box;

	position: relative;
	box-shadow: 0 0 14px -7px  var(--border-color);
	transition: box-shadow .3s;

	display: flex;
	flex-direction: column;
	gap: 16px;
	padding: 20px;
}

@media (min-width: 868px) {
	.card {
		width: 100%;
	}
}

.card-header{
	display: flex;
	flex-direction: row;
	align-items: center;
	gap: 12px;
}

.card-content {
	display: flex;
	flex-direction: column;
	gap: 14px;
}

.card-header__title{
	font-size: 20px;
	font-weight: 500;
}


@media (max-width: 868px){

	.centered{
		align-items: normal;
	}
}

.card-footer{
	display: flex;
	flex-direction: column;
	gap: 16px;
}
</style>