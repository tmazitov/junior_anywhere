<template>
    <div class="vacancy-apply-list">
        <VacancyApplyItem v-for="apply in applies" 
        :key="`apply-${apply.userId}`" :apply="apply"
        @on-hire="onHireHandler"
        @on-cancel="onCancelHandler"/>
    </div>
</template>

<script setup lang="ts">
import VacancyApply from '../../types/vacancyApply';
import VacancyApplyItem from './VacancyApplyItem.vue';

const emits = defineEmits([
    'on-hire',
    'on-cancel',
])

defineProps({
    applies: {
        type: Array<VacancyApply>,
        required: true,
    }
})

const onHireHandler = (userId:number) => {
    emits('on-hire', userId)
}

const onCancelHandler = (userId:number) => {
    emits('on-cancel', userId)
}

</script>

<style scoped>
.vacancy-apply-list{
    display: flex;
    flex-direction: column;
    gap: 16px;
    overflow-y: auto;
    height: 468px;
}
</style>    