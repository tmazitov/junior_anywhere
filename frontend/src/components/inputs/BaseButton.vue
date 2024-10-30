<template>
	<div class="base__button" v-bind:class="{
		primary: primary,
		centered: centered,
		outlined: outlined,
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
	centered: Boolean,
	outlined: Boolean,
})
</script>

<style scoped>
.base__button{
	background: var(--button-background);
	padding: 8px 18px;
	border-radius: 8px;
	cursor: pointer;
	user-select: none;
	transition: background .3s;
	font-weight: 500;

	display: flex;
	gap: 12px;
}



@media (max-width: 768px) {
	.base__button:hover{
		background: var(--button-background);
	}	

	.base__button.primary:hover{
		background: var(--primary-color);
	}

	.base__button.outlined:hover{
		background: transparent;
		transition: outline .3s;

		outline: 1.5px solid var(--button-background);
	}
	.base__button {
		justify-content: center;
	}
}

@media (min-width: 768px) {
	.base__button:hover{
		background: var(--button-background-hover);
	}
	
	.base__button:active {
		background: var(--primary-color-opacity);
	}

	.base__button.outlined:hover{
		outline: 1.5px solid var(--button-background-hover);
		background: var(--button-background-hover);
	}
	.base__button.primary:hover{
		background: var(--primary-color-hover);
	}
	
}

.base__button.primary{
	background: var(--primary-color);
}

.base__button.centered{
	text-align: center;
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