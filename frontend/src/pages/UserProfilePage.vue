<template>
	<div class="page">
		<div class="page-frame">
			<NavigationBar/>
			<div class="page-frame__content grid-container">
				<ContentBlock outlined style="height: fit-content">
					<Menu v-model="currentPage" :options="profilePages"/>
				</ContentBlock>

				<ContentBlock outlined style="height: 300px">
					<span class="content" v-if="currentPage == 0">
						<h2>Main Info</h2>
						<div>Timur Mazitov</div>
					</span>
					<span class="content" v-else-if="currentPage == 1">
						<h2>Resume</h2>

						<BaseButton title="Add resume"/>
					</span>
					<span class="content" v-else-if="currentPage == 2">
						<h2>Applies</h2>
						<div class="support-message">
							No applies
						</div>
					</span>
				</ContentBlock>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import ContentBlock from '../components/ContentBlock.vue';
import NavigationBar from '../components/navigation-bar/NavigationBar.vue';
import Menu from '../components/profile/Menu.vue';
import BaseButton from '../components/inputs/BaseButton.vue';

const currentPage = ref<number>(0)
const profilePages = [
	{icon: "tabler:user", title: "Main Info", value: 0},
	{icon: "tabler:address-book", title: "Resume", value: 1},
	{icon: "tabler:archive", title: "Applies", value: 2},
]

</script>

<style scoped>
.grid-container {
	display: grid;
	padding-top: 16px;
	grid-template-columns: 240px 1fr;
}

.content{
	display: flex;
	flex-direction: column;
	gap: 16px;
	height: 100%
}

.support-message{
	width: 100%;
	flex: 1;
	color: var(--silver);
	display: flex;
	align-items: center;
	justify-content: center;
}
</style>