<template>
	<div class="base-input" v-bind:class="{
		focused: isFocused,
	}">
		<div class="label" v-if="label">
			{{label}}
		</div>
		<div class="left icon" 
		v-if="leftIcon && !leftIcon.isHidden" 
		v-bind:class="{
			'is-button' : leftIcon.onClick
		}">
			<Icon  
				:icon="leftIcon.name" 
				:width="leftIcon.width" 
				:height="leftIcon.height" 
				:color="leftIcon.color"
				@click="leftIcon.onClick ? 
					leftIcon.onClick() : null"
			/>
		</div>

		<input 
			type="text" 
			:placeholder="placeholder"
			:value="value" @input="updateValue"
			@focus="isFocused = true"
			@blur="isFocused = false">

		<div class="right icon" 
		v-if="rightIcon"

		v-bind:class="{
			'is-button' : rightIcon.onClick
		}">
			<Icon v-show="!rightIcon.isHidden"
				:icon="rightIcon.name" 
				:width="rightIcon.width" 
				:height="rightIcon.height" 
				:color="rightIcon.color"
				@click="rightIcon.onClick ?
					rightIcon.onClick() : null"
			/>
		</div>
	</div>
</template>

<script setup lang="ts">
import { defineModel, defineProps, ref } from 'vue';
import IconT from '../../types/icon';
import {Icon} from '@iconify/vue'

const value = defineModel<string>({required: true})
defineProps({
	placeholder: String,
	rightIcon: 	Object as () => IconT,
	leftIcon: 	Object as () => IconT,
	label: String,
})

const isFocused = ref(false)
const updateValue = (ev: any) => {
	value.value = ev.target["value"]
}
</script>

<style scoped>
.base-input{
	display: flex;
	flex-direction: row;
	gap: 8px;

	background: var(--input-background-color);
	border: 1px solid var(--border-color);
	border-radius: 6px;
	box-sizing: border-box;
	transition: box-shadow .15s;
	font-size: 15px;
	padding: 7px 11px;
	height: 36px;
}

.icon{
	height: 21px;
	width: 21px;
}
.icon.is-button{
	cursor: pointer;
	user-select: none;
}

.base-input {
	position: relative;
}

.base-input > * {
	display: flex;
	align-items: center;
}

.base-input.focused{
	border-color: var(--border-color-hover);
	box-shadow: 0 0 1px 1px var(--primary-color-hover);
}

.label {
	position: absolute;
	left: 0;
	top: -24px;
	font-size: 13px;
	font-weight: 300;
}

input{
	border: none;
	background: none;
	padding: 0;
	width: 100%;
	line-height: 21px;
	font-size: 14px;
	height: 21px;
}

input:focus{
	outline: none;
}
</style>