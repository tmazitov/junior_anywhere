<template>
	<div class="base__button" v-bind:class="{
		primary: primary,
		disabled: disabled,
		[fill]: true,
	}">
		<div class="base__button-icon" v-if="icon">
			<Icon :icon="icon" color="var(--text-color)" height="18px" width="18px"/> 
		</div>
		<div class="base__button-title">
			{{ title }}
		</div>
	</div>
</template>

<script lang="ts" setup>
import { Icon } from '@iconify/vue/dist/iconify.js';
import { defineProps } from 'vue'

defineProps({
	title: String,
	icon: String,
	primary: Boolean,
	disabled: Boolean,
	fill: {
		type: String,
		default: 'default',
		validation(value:string){
			return ['default', 'clear', 'outline'].includes(value)
		}
	},
})
</script>

<style scoped>
.base__button{
	background: var(--button-background);
	padding: 8px 18px;
	border-radius: var(--border-radius);
	cursor: pointer;
	user-select: none;
	transition: background .3s;
	font-weight: 500;
	outline: 1.5px solid transparent;

	display: flex;
	gap: 8px;
	transition: all .3s;
}

.base__button.clear {
	background: transparent;
	color: var(--primary-color);
}

.base__button-title{
	text-align: center;
	width: 100%;
}

.disabled{
	pointer-events: none;
	opacity: .5;
}

@media (max-width: 868px) {

	.base__button {
		justify-content: center;
	}
}

@media (min-width: 868px) {
	.base__button.default:hover{
		background: var(--button-background-hover);
	}
	.base__button.clear:hover{
		outline: 1.5px solid var(--primary-color-hover);
	}
	.base__button.primary:hover{
		background: linear-gradient(90deg, var(--primary-color-opacity) 0%, var(--primary-color) 50%);
	}
}

.base__button.primary{
	/* background: var(--primary-color); */
	background: linear-gradient(90deg, var(--primary-color-opacity) 0%, var(--primary-color) 100%);
}

.base__button.outlined{
	background: transparent;
	transition: outline .3s;

	outline: 1.5px solid var(--button-background);
}

.base__button-icon{
	display: flex;
	justify-content: center;
	align-items: center;
}

</style>