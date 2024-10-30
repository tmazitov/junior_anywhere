<template>
<div class="content-block" :class="class" v-bind:class="{
	outlined: outlined,
}">
	<slot></slot>
</div>
</template>

<script setup lang="ts">
defineProps({
	class: String,
	outlined: Boolean,
})
</script>

<style scoped>
.content-block {
	background-color: var(--card-background-color);
	border-radius: 16px;
	padding: 16px;
}
.outlined{
	border: 1px solid var(--border-color);
}
</style>