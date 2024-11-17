<template>
    <ModalWindowLayout v-model="isOpen">
        <FormCard background="white" width="500px" height="600px" v-if="vacancy">
            <template v-slot:header>
                <BaseIconButton icon="tabler:arrow-back-up"
                    @click="closeHandler"
                    fill="clear"/>
                <h3>{{vacancy.name}}</h3>
            </template>
            <template v-slot:default>
                <div class="modal-content">
                    <BaseSwitch v-model="currentTab" :items="tabOptions"/>

                    <div class="modal-content__container" v-show="currentTab == 1">

                        <div class="general__main-details" v-if="vacancy.salary">
                            <div class="general-salary">{{vacancy.salary}} AED</div>
                            <div class="general-location">{{ getLocationName(vacancy.locationId) }}</div>
                        </div>

                        <div class="general__secondary-details">
                            <div class="genera-experience" v-if="vacancy.experience">
                                from {{vacancy.experience}} years
                            </div>
                            <div class="general-employment" v-if="vacancy.employmentId">
                                <Icon icon="tabler:briefcase" height="1.2em"/>
                                {{getEmploymentName(vacancy.employmentId)}}
                            </div>
                            <div class="general-employment" v-if="vacancy.withDegree">
                                <Icon icon="tabler:school" height="1.2em"/>
                                Degree required
                            </div>
                        </div>
                        
                        <div class="general-skills">

                            <Category v-for="skill, index in vacancy.skills"
                                :key="`skill-${index}`" 
                                :title="skill" color="var(--primary-color)"/>
                        </div>
                        
                        <div class="general-description">

                            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                            Nulla nec purus feugiat, molestie ipsum et, eleifend nunc.
                                                        
                        </div>
                    </div>
                    <div class="modal-content__container" v-show="currentTab == 2">
                    </div>
                </div>
            </template>
            <!-- <template v-slot:footer> -->
                <!-- <BaseButton title="Upload" primary :disabled="!formIsValid"/> -->
            <!-- </template> -->
        </FormCard>
    </ModalWindowLayout>
</template>

<script lang="ts" setup>
import ModalWindowLayout from './ModalWindowLayout.vue';
import FormCard from '../forms/FormCard.vue';
import BaseIconButton from '../inputs/BaseIconButton.vue';
import BaseButton from '../inputs/BaseButton.vue';
import { ref , defineProps, defineModel } from 'vue';
import Vacancy from '../../types/vacancy';
import BaseSwitch from '../inputs/BaseSwitch.vue';
import locations from '../../info/locations';
import Category from '../inputs/Category.vue';
import { Icon } from '@iconify/vue/dist/iconify.js';
import employments from '../../info/employments';
const isOpen = defineModel<boolean>({required:true})


const closeHandler = () => {
    isOpen.value = false
}

defineProps({
    vacancy: Vacancy,
    isCompanyView: Boolean,
})

const getLocationName = (id:number) => {
    return locations.find(loc => loc.value == id)?.title
}

// TABS
const tabOptions = [
    {value : 1, title: 'General'},
    {value : 2, title: 'Applies'},
]
const currentTab = ref(1)

const getEmploymentName = (id:number) => {
    return employments.find(emp => emp.value == id)?.title
}
</script>

<style scoped>
.modal-content__container{
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-top: 16px
}

.general__main-details{
    display: flex;
    flex-direction: row;
    gap: 16px;
    justify-content: space-between;
    align-items: center;
}

.general__secondary-details {
    display: flex;
    flex-direction: row;
    gap: 16px;
    color: #616161;
}

.general-salary{
    font-size: 1.5em;
}

.general-skills{
    display: flex;
    flex-direction: row;
    gap: 10px;
}

.general-description{
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 10px;
    border-radius: 8px;
    background: var(--input-background);
    max-height: 300px;
    overflow-y: auto;
}

.general-employment{
    display: flex;
    flex-direction: row;
    gap: 8px;
    align-items: center;
}
</style>