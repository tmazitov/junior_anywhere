<template>
	<div class="card">
		<div class="card-header" v-if="$slots['header']">
			<slot name="header"></slot>
		</div>
		<div class="card-content" v-if="$slots['default']">
			<slot></slot>
		</div>
		<div class="card-footer" v-if="$slots['footer']">
			<slot name="footer"></slot>
		</div>
	</div>
</template>

<script setup lang="ts">
  
</script>

<style scoped>
.card{
	width: 100%;
	border-radius: 16px;
	box-sizing: border-box;

	position: relative;
	box-shadow: 0 0 14px -7px  var(--border-color);
	transition: box-shadow .3s;

	display: flex;
	flex-direction: column;
	gap: 16px;
	padding: 20px;
	width: 300px;
}

@media (min-width: 868px) {
	.card {
		width: 300px;
	}
}

@media (max-width: 368px){
	.card {
		width: 100%;
	}
}


.card-header{
	display: flex;
	flex-direction: row;
	align-items: center;
	gap: 12px;
}

.card-content {
	display: flex;
	flex-direction: column;
	gap: 14px;
}




.card-footer{
	display: flex;
	flex-direction: column;
	gap: 16px;
}
</style>