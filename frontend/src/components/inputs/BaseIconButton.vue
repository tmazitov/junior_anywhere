<template>
	<div class="base-icon-button" v-bind:class="{
		primary: primary,
		[fill]: true
	}">
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
	fill: {
		type: String,
		default: 'default',
		validation(value:string){
			return ['default', 'clear', 'outline'].includes(value)
		}
	},
	primary: Boolean,
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
	border-radius: var(--border-radius);

	cursor: pointer;
	box-sizing: border-box;
	transition: background .15s;
}

.clear {
	background: transparent;
	border-color: transparent;
}

@media (min-width: 868px){
	.base-icon-button:hover{
		background: var(--button-background-hover);
	}
	.primary:hover{
		background: var(--primary-color-hover);
	}
}

.primary{
	background: var(--primary-color);
	border-color: transparent;
}

</style>