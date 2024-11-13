<template>
    <ModalWindowLayout v-model="isOpen">
        <FormCard background="white" width="400px">
            <template v-slot:header>
                <BaseIconButton icon="tabler:arrow-back-up"
                    @click="closeHandler"
                    fill="clear"/>
                <h3>New Vacancy</h3>
            </template>
            <template v-slot:default>
                <VacancyCreateForm v-model="form"/>
            </template>
            <template v-slot:footer>
                <BaseButton title="Upload" primary :disabled="!formIsValid"/>
            </template>
        </FormCard>
    </ModalWindowLayout>
</template>

<script lang="ts" setup>
import FormCard from '../forms/FormCard.vue';
import BaseIconButton from '../inputs/BaseIconButton.vue';
import BaseButton from '../inputs/BaseButton.vue';
import ModalWindowLayout from './ModalWindowLayout.vue';
import VacancyCreate from '../../types/forms/vacancyCreate';
import { computed, ref } from 'vue';
import VacancyCreateForm from '../forms/VacancyCreateForm.vue';

const isOpen = defineModel<boolean>({required:true})
const form = ref(new VacancyCreate())

const closeHandler = () => {
    isOpen.value = false
    form.value.clear()
}

const formIsValid = computed(() => form.value.validate())

</script>

<style scoped>

</style>