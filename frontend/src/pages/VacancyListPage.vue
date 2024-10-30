<template>
	<div class="page">
		<div class="page-frame grid-container">
			<div class="block">
				<div class="block-child" style="height:200px">
					Add One
				</div>
				<div class="block-child" style="flex:1;">
					Add Two
				</div>
			</div>
			<div class="block">
				<div class="block-child">Filters</div>
				<div class="block-child" style="flex:1;">
					Vacancy List
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">


</script>

<style scoped>

.block-child {
	background-color: #f0f0f0;
	border-radius: 8px;
	padding: 16px;
}

.block {
	display: flex;
	flex-direction: column;
	gap: 16px;
}

.grid-container {
	display: grid;
	grid-template-columns: 240px 1fr;
	grid-column-gap: 16px;
}
</style>