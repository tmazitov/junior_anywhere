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
					
					<FormCard>
						<template v-slot:header>
							<h3>Resume</h3>
						</template>

						<template v-slot:default>
							<div class="support-message">
								Go ahead and create a summary about your skills and strong sides
							</div>							 
						</template>

						<template v-slot:footer>
							<BaseButton title="Create Resume" width="100%" primary/>
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
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import NavigationBar from '../components/navigation-bar/NavigationBar.vue';
import FormCard from '../components/forms/FormCard.vue';
import BaseButton from '../components/inputs/BaseButton.vue';

// const currentPage = ref<number>(0)
// const profilePages = [
// 	{icon: "tabler:user", title: "Main Info", value: 0},
// 	{icon: "tabler:address-book", title: "Resume", value: 1},
// 	{icon: "tabler:archive", title: "Applies", value: 2},
// ]

</script>

<style scoped>
.centered {
	padding-top: 16px;
	align-items: center;
	max-width: 100%;
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
</style>