<template>
	<div class="base-icon-button">
		<Icon :icon="icon" color="var(--text-color)" height="18px" width="18px"/> 
	</div>
</template>

<script lang="ts" setup>
import { Icon } from '@iconify/vue/dist/iconify.js';

defineProps({
	icon: {
		type: String,
		required: true,
	},
})
</script>

<style  scoped>
.base-icon-button{
	display: flex;
	justify-content: center;
	align-items: center;
	height: 36px;
	width: 36px;

	background: var(--button-background);
	border: 1px solid var(--border-color);
	border-radius: 6px;

	cursor: pointer;
	transition: background .15s;
}

.base-icon-button:hover{
	background: var(--button-background-hover);
}

.base-icon-button:hover{
	background: var(--button-background-hover);
}
</style>