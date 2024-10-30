<template>
	<div class="page">
		<div class="page-frame">
			<div class="page-frame__content">
				<div class="info-card">
					<div class="header">
						<h4>Junior Sunflower</h4>
						<h1>Let's find your first Job!</h1>
					</div>

					<div class="buttons">
						<BaseInput :left-icon="icons['search']" placeholder="Field of interest" v-model="search"/>
						<BaseSelect icon="tabler:briefcase" placeholder="Employment" :items="options" v-model="selected"/>
						<BaseButton id="search-desktop" title="Search" primary/>
					</div>

					<div class="some-info">
						<Category title="Easy to Attend" color="#f09156"/>
						<Category title="For Beginners" color="#f09156"/>
						<Category title="Absolutely Free" color="#f09156"/>
					</div>

					<BaseButton class="search-mobile" title="Search" primary/>
					<BaseButton class="search-mobile" title="For Bysiness" primary outlined/>
				</div>
			</div>
		</div>
	</div>	
</template>

<script setup lang="ts">
import { ref } from 'vue';
import BaseButton from '../components/inputs/BaseButton.vue';
import BaseInput from '../components/inputs/BaseInput.vue';
import BaseSelect from '../components/inputs/BaseSelect.vue';
import Category from '../components/inputs/Category.vue';

const selected = ref(null)
const search = ref('');
const icons = {
	"search" : {
		name: "tabler:search",
	},
}

const options = [
	{
		value: "all",
		title: "All"
	},
	{
		value: "internship",
		title: "Internship"
	},
	{
		value: "full-time",
		title: "Full Time"
	},
	{
		value: "part-time",
		title: "Part Time"
	},
]

</script>

<style scoped>
.header{
	display: flex;
	flex-direction: column;
	margin-bottom: 10px;
}

.buttons{
	display: flex;
	flex-direction: row;
	gap: 10px;
}

@media (max-width: 768px){
	#search-desktop {
		display: none;
	}
}

@media (min-width: 768px) {
	.search-mobile {
		display: none;
	}
}

.some-info{
	display: flex;
	flex-direction: row;
	gap: 10px;
}

.buttons > * {
	width: fit-content;
}

.info-card{
	display: flex;
	flex-direction: column;
	justify-content: center;
	gap: 10px;
}


</style>