<template>
	<div class="page">
		<div class="page-frame centered">
			<div class="page-frame__content">

				<!-- Auth card -->

				<FormCard v-if="!isRegister">
					<template #header>
						<BaseIconButton icon="tabler:arrow-back-up"
							@click="navigateToBack"
							fill="clear"/>
						<div class="card-header__title">Sign In</div>	
					</template>
					<template #default>
						<SignInUserForm v-model="signInUser"/>
						<a href="">Forgot password</a>
					</template>
					<template #footer>
						<BaseButton title="Continue" primary/>
					</template>
				</FormCard>

				<!-- Registration card -->

				<FormCard v-else>
					<template #header>
						<BaseIconButton icon="tabler:arrow-back-up"
							@click="navigateToBack"
							fill="clear"/>
						<div class="card-header__title">Registration</div>	
					</template>
					<template #default>
						<RegisterUserForm v-model="registerUser"/>
					</template>
					<template #footer>
						<BaseButton title="Continue" primary :disabled="!registrationFormIsValid"/>
					</template>
				</FormCard>

				<!-- Redirect to register -->

				<FormCard v-if="!isRegister">
					<h5>Don't have an account? Create them <a @click="toggleRegister">here</a></h5>
				</FormCard>

				<!-- Redirect to sign in -->

				<FormCard v-else>
					<h5>Already have an account? Sign in <a @click="toggleRegister">here</a></h5>
				</FormCard>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">

import { computed, ref } from 'vue';
import BaseButton from '../components/inputs/BaseButton.vue';
import BaseIconButton from '../components/inputs/BaseIconButton.vue';
import { useRouter } from 'vue-router';
import RegisterUser from '../types/forms/registerUser';
import RegisterUserForm from '../components/forms/RegisterUserForm.vue';
import FormCard from '../components/forms/FormCard.vue';
import SignInUser from '../types/forms/signInUser';
import SignInUserForm from '../components/forms/SignInUserForm.vue';

const signInUser = ref(new SignInUser());
const registerUser = ref(new RegisterUser());

const isRegister = ref(false);
const toggleRegister = () => {
	isRegister.value = !isRegister.value;
}

const router = useRouter();
const navigateToBack = () => {
	if (isRegister.value) {
		isRegister.value = false;
		return;
	}
	router.back();
}

const registrationFormIsValid = computed(() => {
	return registerUser.value.validate()
})

const email = ref('');
const emailField = ref<HTMLElement|null>(null)
const password = ref('');
const passwordField = ref<HTMLElement|null>(null)

const icons = {
	'email' : {
		name: 'tabler:mail',
	},
	'pass' : {
		name: 'tabler:password',
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

@media (max-width: 368px){
	.centered{
		align-items: normal;
	}
}


.card-header__title{
	font-size: 18px;
	font-weight: 400;
}

</style>