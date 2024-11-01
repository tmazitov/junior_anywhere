<template>
	<div class="range">
		<div class="range-slider">
			<span class="range-selected" ref="rangeSelected"></span>
		</div>
		<div class="range-input" v-if="fromValue != undefined && toValue != undefined">
			<input type="range" @input="calcRangeSize" ref="fromPoint" 
				class="min" 
				:min="min" 
				:max="max" 
				:value="fromValue" 
				:step="step">
			<input type="range" @input="calcRangeSize" ref="toPoint" 
				class="max" 
				:min="min" 
				:max="max" 
				:value="toValue"
				:step="step">
		</div>
		<div class="range-price">      
			<label for="min">Min</label>
			<input type="number" name="min" 
				:min="min" :max="max" :step="step" :value="fromValue">      
			<label for="max">Max</label>
			<input type="number" name="max" 
				:min="min" :max="max" :step="step" :value="toValue">      
		</div>
	</div> 
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';

const fromPoint = ref<HTMLInputElement | null>(null)
const toPoint = ref<HTMLInputElement | null>(null)
const rangeSelected = ref<HTMLSpanElement | null>(null)

const range = defineModel<number|number[]|undefined>()


const fromValue = computed({
	get: () => Array.isArray(range.value) ? range.value[0] : undefined,
	set: (val: number) => {
		if (Array.isArray(range.value)) {
			range.value[0] = val
		}
	},
})

const toValue = computed({
	get: () => Array.isArray(range.value) ? range.value[1] : undefined,
	set: (val:number) => {
		if (Array.isArray(range.value)) {
			range.value[1] = val
		}
	},
})

const singleValue = computed({
	get: () => Array.isArray(range.value) ? undefined : range.value,
	set: (val: number) => {
		range.value = val
	},
})


const props = defineProps({
	label: {
		type: String,
		default: "Select Range",
	},
	min: {
		type: Number,
		default: 0,
	},
	max: {
		type: Number,
		default: 100,
	},
	step: {
		type: Number,
		default: 1,
	},
})

const calcRangeSize = (e:any) => {
	if (!fromPoint.value || !toPoint.value || !rangeSelected.value) {
		return
	}
	let minRange = Number(fromPoint.value.value);
	let maxRange = Number(toPoint.value.value);
	console.log('values :>> ', range.value, minRange, maxRange);

	if (e && e.target.className == "min" && minRange > maxRange) {   
		fromValue.value = maxRange
		e.preventDefault();
		return
	} else if (e && e.target.className == "max" && maxRange < minRange) {
		toValue.value = minRange
		e.preventDefault();
		return      
	} else {
		fromValue.value = minRange
		toValue.value = maxRange
		if (rangeSelected.value && fromPoint.value && toPoint.value) {
			rangeSelected.value.style.left = (minRange / Number(fromPoint.value.max)) * 100 + "%"
			rangeSelected.value.style.right = 100 - (maxRange / Number(toPoint.value.max)) * 100 + "%"
		}
	}
}

onMounted(() => {
	calcRangeSize(null)
})

</script>

<style scoped>
.range-slider {
	height: 2.25px;
	position: relative;
	background-color: var(--border-color);
	border-radius: 2px;
}
.range-selected {
	height: 100%;
	position: absolute;
	border-radius: 3px;
	background-color: var(--primary-color);
}
.range-input {
	position: relative;
}
.range-input input {
	position: absolute;
	width: 100%;
	height: 5px;
	top: -4px;
	background: none;
	pointer-events: none;
	margin: 0;
	-webkit-appearance: none;
	-moz-appearance: none;
}
.range-input input::-webkit-slider-thumb {
	height: 14px;
	width: 14px;
	border-radius: 50%;
	border: 1.5px solid var(--primary-color);
	background-color: white;
	pointer-events: auto;
	-webkit-appearance: none;
}
.range-input input::-moz-range-thumb {
	height: 15px;
	width: 15px;
	border-radius: 50%;
	border: 2px solid var(--primary-color);
	background-color: white;
	pointer-events: auto;
	-moz-appearance: none;
}
.range-price {
	margin: 30px 0;
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
}
.range-price label {
  margin-right: 5px;
}
.range-price input {
	width: 40px;
	padding: 5px;
}
.range-price input:first-of-type {
	margin-right: 15px;
}
</style>
  