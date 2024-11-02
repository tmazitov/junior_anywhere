<template>
	<ContentBlock class="nav-bar">
		<div class="nav-bar__links">
			<div class="nav-bar__logo" @click="navigateTo('home')">
				<Icon icon="tabler:brightness-up-filled" color="var(--primary-color)" height="26px"/>
			</div>
			<div class="nav-bar__link desktop"
			v-for="item in navbarItems"
			:key="`nav-bar-item-${item.id}`"
			@click="item.action">
				{{ item.title}}
			</div>
		</div>
		<div class="nav-bar__profile">
			<span class="mobile">
				<transition name="open">
					<div class="mobile-menu" v-if="isOpen"></div>
				</transition>
			</span>
			<span class="mobile">
				<BaseIconButton 
					:icon="isOpen ? 'tabler:x' : 'tabler:menu-2'"
					@click="toggleMenu"/>
			</span>
			<span class="mobile">
				<BaseIconButton icon="tabler:arrow-bar-to-right" primary/>
			</span>
			<span class="desktop">
				<BaseButton style="width:78px" title="Sign In" icon="tabler:arrow-bar-to-right" primary />
			</span>

		</div>

	</ContentBlock>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue/dist/iconify.js';
import ContentBlock from '../ContentBlock.vue';
import BaseButton from '../inputs/BaseButton.vue';
import BaseIconButton from '../inputs/BaseIconButton.vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const isOpen = ref(false);
const toggleMenu = () => {
	isOpen.value = !isOpen.value;
}

const router = useRouter();

const navigateTo = (routeName:string) => {
	router.push({name: routeName})
}

type NavbarItem = {
	id: number;
	icon: string;
	title: string;
	action: (payload: MouseEvent) => void;
}

const navbarItems:Array<NavbarItem> = [
	{id: 0, title: "Events", icon: "tabler:search", action: () => navigateTo('vacancy-list') },
	{id: 0, title: "Vacancies", icon: "tabler:search", action: () => console.log("Vacancies") },
	{id: 1, title: "Companies", icon: "tabler:building", action: () => console.log("Companies") },
	{id: 2, title: "About", icon: "tabler:info-circle", action: () => console.log("About") },
]
</script>

<style scoped>
.nav-bar {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 8px;
	border-radius: 12px;
	height: 54px;
	box-sizing: border-box;
	position: sticky;
	top: 16px;
	z-index: 4;

	background: rgba( 255, 255, 255, 0.15 );
	box-shadow: 0 8px 32px 0 rgba(162, 165, 199, 0.37);
	backdrop-filter: blur( 13px );
	-webkit-backdrop-filter: blur( 13px );
}

.nav-bar__links {
	display: flex;
	gap: 16px;
	height: 100%;
	align-items: center;

}


.nav-bar__link {
	display: flex;
	align-items: center;
	border-radius: 8px;
	cursor: pointer;
	transition: background .3s;
	flex: 1;
}

.nav-bar__profile {
	display: flex;
	gap: 16px;
}

.nav-bar__logo {
	height: 36px;
	aspect-ratio: 1 / 1;
	border: 1.5px solid var(--border-color);
	border-radius: 8px;

	display: flex;
	box-sizing: border-box;
	justify-content: center;
	align-items: center;
}

.nav-bar__logo > svg {
	transition: transform 0.3s ease;
}

@media (min-width: 868px) {
	.nav-bar__logo:hover > svg  {
		animation: rotate 3.5s linear infinite;
	}
}

@keyframes rotate {
	from {
		transform: rotate(0deg);
	}
	to {
		transform: rotate(360deg);
	}
}

.mobile-menu {
	position: absolute;
	top: 66px;
	right: 0;
	left: 0;
	z-index: 100;
	height: 200px;
	background: var(--card-background-color);
	border-radius: 8px;
	box-shadow: 0 0 8px 1px var(--border-color);
}

.open-enter-active {
	animation: open .3s ease;
}

.open-leave-active {
	animation: open .3s ease reverse;
}

@keyframes open {
	from {
		opacity: 0;
		transform: translateY(-10px);
	}
	to {
		opacity: 1;
		transform: translateY(0);
	}
}

@media (max-width: 868px) {
	.desktop {
		display: none;
	}
}

@media (min-width: 868px) {
	.mobile {
		display: none;
	}
}
</style>