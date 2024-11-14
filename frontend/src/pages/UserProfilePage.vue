<template>
	<div class="page">
		<div class="page-frame">
			<NavigationBar/>
			<div class="page-frame__content centered">
				<div class="profile-card">
					<FormCard>
						<template v-slot:header>
							<h2>Timur Mazitov</h2>
						</template>
						<template v-slot:default>
							<div class="support-message">
								No Data
							</div>		
						</template>
					</FormCard>
					
					<FormCard v-if="!isFillResumeForm">
						<template v-slot:header>
							<h3>Resume</h3>
						</template>

						<template v-slot:default>
							<div class="support-message">
								Go ahead and create a summary about your skills and strong sides
							</div>							 
						</template>

						<template v-slot:footer>
							<BaseButton title="Create Resume" width="100%" 
								@click="() => isFillResumeForm = true"
								primary/>
						</template>
					</FormCard>
				

					<FormCard v-if="isFillResumeForm">
						<template v-slot:header>
							<h3>New Resume Form</h3>
						</template>

						<template v-slot:default>
							<UserResumeForm v-model="resumeForm"/>
						</template>

						<template v-slot:footer>
							<div class="buttons">
								<BaseButton title="Cancel" width="100%" fill="outline"
									@click="() => isFillResumeForm = false"/>
								<BaseButton title="Upload" width="100%" primary :disabled="!resumeFormIsValid"/>
							</div>
						</template>
					</FormCard>
					<!-- <FormCard>
						<template v-slot:header>
							<h3>Applies</h3>
						</template>
						<template v-slot:default>
							<div class="support-message block">
								Empty list
							</div>
						</template>
					</FormCard> -->
					<BaseButton title="Log Out" @click="logOut"/>

				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import NavigationBar from '../components/navigation-bar/NavigationBar.vue';
import FormCard from '../components/forms/FormCard.vue';
import BaseButton from '../components/inputs/BaseButton.vue';
import UserResumeForm from '../components/forms/UserResumeForm.vue';
import { computed, onMounted, ref } from 'vue';
import UserResume from '../types/forms/userResume';
import UserAuth from '../utils/authUser';
import { useRouter } from 'vue-router';

const isFillResumeForm = ref(false)
const resumeForm = ref(new UserResume())
const resumeFormIsValid = computed(() => resumeForm.value.validate())

onMounted(() => {
	if (!UserAuth.getUserId()) {
		router.replace({name: "auth"})
		return
	}
})

const router = useRouter()

const logOut = () => {
	UserAuth.delUserId()
	router.replace({name: "auth"})
}

</script>

<style scoped>

@media (min-width:868px) {
	.centered {
		padding-top: 16px;
		align-items: center;
		max-width: 100%;
	}
	
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
	font-size: 0.85em;
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
</style>