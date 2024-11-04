<template>
	<div class="page">
		<div class="page-frame centered">
			<div class="page-frame__content">

				<!-- Auth card -->

				<FormCard v-if="!isRegister && !isSubmitted">
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
						<BaseButton title="Continue" 	
							@click="submitHandler"
							primary/>
					</template>
				</FormCard>

				<!-- Registration card -->

				<FormCard v-if="isRegister && !isSubmitted">
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
						<BaseButton title="Continue" 
							:disabled="!registrationFormIsValid"
							@click="submitHandler"
							primary />
					</template>
				</FormCard>

				<!-- Verification code -->

				<FormCard v-if="isSubmitted">
					<template #header>
						<BaseIconButton icon="tabler:arrow-back-up"
							@click="navigateToBack"
							fill="clear"/>
						<div class="card-header__title">Verification code</div>	
					</template>
					<template #default>
						<div class="verification-code" ref="codeField">
							<BaseInput v-for="i in 6" v-model="code[i-1]"
							type="number"
							:min="0" :max="9"
							@on-input="goNext"
							number-is-without-arrows/>
						</div>
					</template>
					<template #footer>
						<BaseButton title="Continue" 
							@click="submitHandler"
							:disabled="!codeIsValid"
							primary/>
					</template>
				</FormCard>
 
				<!-- Redirect to register -->

				<FormCard v-if="!isRegister">
					<h5>Don't have an account? Create them <a @click="toggleRegister">here</a></h5>
				</FormCard>

				<!-- Redirect to sign in -->

				<FormCard v-if="isRegister">
					<h5>Already have an account? Sign in <a @click="toggleRegister">here</a></h5>
				</FormCard>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">

import { computed, nextTick, ref } from 'vue';
import BaseButton from '../components/inputs/BaseButton.vue';
import BaseIconButton from '../components/inputs/BaseIconButton.vue';
import { useRouter } from 'vue-router';
import RegisterUser from '../types/forms/registerUser';
import RegisterUserForm from '../components/forms/RegisterUserForm.vue';
import FormCard from '../components/forms/FormCard.vue';
import SignInUser from '../types/forms/signInUser';
import BaseInput from '../components/inputs/BaseInput.vue';
import SignInUserForm from '../components/forms/SignInUserForm.vue';

const signInUser = ref(new SignInUser());
const registerUser = ref(new RegisterUser());

const codeField = ref<HTMLElement|null>(null);
const isSubmitted = ref(false)
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

	if (isSubmitted.value) {
		isSubmitted.value = false;
		return;
	}

	router.back();
}

const code = ref(['', '', '', '', '', '']);
const codeInputs = ref<HTMLInputElement[]>([]);
const codeIsValid = ref(false)
const goNext = (ev:any) => {

	const target = ev.target;
	const targetValue = target.value != '' ? Number(target.value) : NaN
	const index = codeInputs.value.findIndex((elem:HTMLElement) => elem === target);
	if (targetValue > 9) {	
		target.value = '9'
		code.value[index] = '9'
	}
	if (targetValue < 0) {	
		target.value = '0'
		code.value[index] = '0'
	}
	const next = codeInputs.value[index + 1];
	if (next && !Number.isNaN(targetValue)) {
		next.value = ''
		next.focus();
	}
	codeIsValid.value = code.value.join('').length === 6;
}

const submitSignInForm = () => {
	// if (!signInUser.value.validate()) {
	// 	return
	// }
	submitChange()
}

const submitRegistrationForm = () => {
	if (!registerUser.value.validate()) {
		return
	}
	submitChange()
}

const submitChange = () => {
	if (isSubmitted.value) {
		return
	}
	isSubmitted.value = true
	nextTick(() => {
		if (!codeField.value)
			return
		codeInputs.value = Array.from(codeField.value.querySelectorAll('input')) ?? [];
		if (!codeInputs.value.length)
			return
		codeInputs.value[0].focus();
	})
}

const submitVerificationCode = () => {
	if (codeIsValid.value) {
		return
	}

}

const submitHandler = () => {

	const submitLevels = [
		{level: !isRegister.value && !isSubmitted.value, submit: submitSignInForm},
		{level: isRegister.value && !isSubmitted.value, submit: submitRegistrationForm},
		{level: isSubmitted.value, submit: submitVerificationCode},
	]
	const currentLevel = submitLevels.find(submit => submit.level);
	if (!currentLevel)
		return

	currentLevel.submit();
}

const registrationFormIsValid = computed(() => {
	return registerUser.value.validate()
})
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

.verification-code{
	display: flex;
	gap: 10px;
}

.verification-code > * {
	flex: 1;
}
</style>