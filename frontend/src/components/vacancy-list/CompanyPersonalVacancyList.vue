<template>
    <div class="company-vacancy-list">
        <Card v-for="vacancy in vacancies" 
        :key="`card-${vacancy.id}`"
        :vacancy="vacancy"
        is-company-view/>
    </div>
</template>

<script lang="ts" setup>
import Vacancy from '../../types/vacancy';
import Card from './Card.vue';

defineProps({
    vacancies: {
        type: Array<Vacancy>,
        required: true,
    }
})

</script>

<style scoped>
.company-vacancy-list{
    display: flex;
    flex-direction: column;
    padding-bottom: 24px;
}
</style>
