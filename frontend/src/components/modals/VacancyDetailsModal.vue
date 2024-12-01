<template>
    <ModalWindowLayout v-model="isOpen">
        <div class="window-container">
            <FormCard background="white" width="500px" height="600px" v-if="vacancy">
            <template v-slot:header>
                <BaseIconButton icon="tabler:arrow-back-up"
                    @click="closeHandler"
                    fill="clear"/>
                <h3>{{vacancy.name}}</h3>
            </template>
            <template v-slot:default>
                <div class="modal-content">
                    <BaseSwitch v-if="isCompanyView" v-model="currentTab" :items="tabOptions"/>

                    <div class="modal-content__container" v-show="currentTab == 1">

                        <div class="general__main-details" v-if="vacancy.salary">
                            <div class="general-salary">{{vacancy.salary}} AED</div>
                            <div class="general-location">{{ getLocationName(vacancy.locationId) }}</div>
                        </div>

                        <div class="general__secondary-details" v-if="vacancy.experience || vacancy.employmentId || vacancy.withDegree">
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
                            <div class="general-employment" v-if="vacancy.workFormatId">
                                {{ getWorkFormat(vacancy.workFormatId)}}
                            </div>
                        </div>
                        
                        <div class="general-skills" v-if="vacancy.skills.length">

                            <Category v-for="skill, index in vacancy.skills"
                                :key="`skill-${index}`"
                                :title="skill" color="var(--primary-color)"/>
                        </div>
                        
                        <div class="general-description">
                            {{ vacancy.comment }}
                        </div>
                    </div>
                    <div class="modal-content__container" v-show="currentTab == 2">
                        <VacancyApplyList :applies="applies"
                        @on-details="onDetailsHandler"/>
                    </div>
                </div>
            </template>
            <template v-slot:footer v-if="!isCompanyView">
                <BaseButton title="Apply" width="fit-content" primary @click="isNewApply = true"/>
            </template>
            <template v-slot:footer v-if="isCompanyView && currentTab == 1">
                <BaseButton title="Cancel" 
                    width="fit-content"
                    @click="isCancelAlertOpen = true"/>
            </template>
        </FormCard>
        <FormCard 
        :background="currentApply || isNewApply ? 
            'white' : 'rgba(215, 215, 215, 0.66)'" 
        width="500px" 
        height="600px">

            <!-- Company view -->

            <template  v-slot:header v-if="currentApply && isCompanyView">
                <div class="content-header">
                    <h3>{{currentApply.userName}} <span style="font-weight: 300; font-size: 0.9em;">({{currentApply.resumeName}})</span></h3>
                </div>
            </template>
            <template v-slot:default v-if="currentApply && isCompanyView">
                <div class="content">
                    There will be a resume details
                </div>
            </template>

            <template v-slot:footer v-if="currentApply && isCompanyView">
                <div class="content-footer" v-if="currentApply">
                    <BaseButton title="Hire" primary  />
                    <BaseButton title="Cancel" secondary />
                </div>
            </template>

            <!-- User view -->

            <template v-slot:header v-if="isNewApply && !isCompanyView">
                <div class="content-header">
                    <h3>Vacancy Apply</h3>
                </div>
            </template>
            <template v-slot:default v-if="isNewApply && !isCompanyView">
                <div class="content">
                    <h4>Resume</h4>
                    <div class="current-resume">
                        <Icon icon="tabler:user" height="1.5em"/>
                        <!-- <div>{{applyForm.resumeName}}</div> -->
                        <div style="flex:1">Resume name</div>
                        <div @click="navTo('user-profile')">
                            Edit
                        </div>
                    </div>
                    <h4>Message</h4>
                    <VacancyApplyForm v-model="applyForm"/>
                </div>
            </template>

            <template v-slot:footer v-if="isNewApply && !isCompanyView">
                <div class="content-footer">
                    <BaseButton title="Submit" primary
                        @click="applyFormSubmit"/>
                    <BaseButton title="Cancel" secondary 
                        @click="applyFormCancel"/>
                </div>
            </template>
        </FormCard>
    </div>
</ModalWindowLayout>
<BaseAlert v-model="isCancelAlertOpen"
    title="Cancel vacancy"
    message="Are you sure you want to cancel this vacancy?"
    confirmText="Yes"
    cancelText="No"
    @on-confirm="cancelVacancyHandler"/>
</template>

<script lang="ts" setup>
import ModalWindowLayout from './ModalWindowLayout.vue';
import FormCard from '../forms/FormCard.vue';
import BaseIconButton from '../inputs/BaseIconButton.vue';
import BaseButton from '../inputs/BaseButton.vue';
import { ref , defineProps, defineModel, computed, watch } from 'vue';
import Vacancy from '../../types/vacancy';
import BaseSwitch from '../inputs/BaseSwitch.vue';
import locations from '../../info/locations';
import Category from '../inputs/Category.vue';
import { Icon } from '@iconify/vue/dist/iconify.js';
import employments from '../../info/employments';
import VacancyApplyList from '../vacancy-list/VacancyApplyList.vue';
import VacancyApply from '../../types/vacancyApply';
import VacancyApplyFormInstance from '../../types/forms/vacancyApply';
import VacancyApplyForm from '../forms/VacancyApplyForm.vue';
import { useRouter } from 'vue-router';
import CompanyAuth from '../../utils/authCompany';
import workFormats from '../../info/workFormats';
import CompanyAPI from '../../api/company/api';
import BaseAlert from '../inputs/BaseAlert.vue';

const isOpen = defineModel<boolean>({required:true})

const closeHandler = () => {
    applyDetails.value = 0
    isOpen.value = false
}


const router = useRouter()
const navTo = (name:string) => {
    router.push({name})
} 

const props = defineProps({
    vacancy: Vacancy,
    isCompanyView: Boolean,
})
const emits = defineEmits([
    'on-cancel-vacancy',
])

watch(() => props.vacancy, async () => {
    if (!props.vacancy) {
        return
    }
    const companyId = CompanyAuth.getCompanyId()
    if (!companyId) {
        return
    }
    await props.vacancy.setupDetails(companyId)
})


// APPLY

const applyDetails = ref<number>(0)
const onDetailsHandler = (userId:number) => {
    applyDetails.value = userId
}
const applies = [
    new VacancyApply({userId: 1, 
        userName: "Timur Mazitov", 
        resumeName: "Supper duper frontend developer"}),
    new VacancyApply({userId: 2, userName: "Sofa Abdulkina", resumeName: "Supper duper backend developer"}),
    new VacancyApply({userId: 3, userName: "Lera Lomakina", resumeName: "Supper duper backend developer"}),
]

const currentApply = computed<VacancyApply | undefined>(() => {
    return applies.find(apply => apply.userId == applyDetails.value)
})

const getLocationName = (id:number) => {
    return locations.find(loc => loc.value == id)?.title
}

const isNewApply = ref<boolean>()
const applyForm = ref<VacancyApplyFormInstance>(new VacancyApplyFormInstance())
const closeApplyHandler = () => {
    applyForm.value.clear()    
    isNewApply.value = false
}
const applyFormSubmit = () => {
    closeApplyHandler()
}
const applyFormCancel = () => {
    closeApplyHandler()
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

const getWorkFormat = (id:number) => {
    return workFormats.find(wf => wf.value == id)?.title
}

// Cancel

const isCancelAlertOpen = ref<boolean>(false)
const cancelVacancyHandler = () => {
    const companyId = CompanyAuth.getCompanyId()
    if (!companyId || !props.vacancy) {
        return
    }
    CompanyAPI.vacancy.cancel(companyId, props.vacancy.id)
    .then(() => {
        emits('on-cancel-vacancy', props.vacancy)
    })
}

</script>

<style scoped>
.window-container{
    display: flex;
    flex-direction: row;
    gap: 16px;
}

.modal-content__container{
    display: flex;
    flex-direction: column;
    gap: 20px;
    flex: 1;
    overflow: hidden;
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

.modal-content{
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.content-header{
    height: 36px;
    width: 100%;
    display: flex;
    align-items: center;
}

.content-footer{
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 16px;
}
.content{
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.current-resume{
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 16px;
    
    padding: 11px;
    width: 100%;
    border-radius: 8px;
    background: var(--input-background);
    border: 1px solid var(--border-color);

    cursor: default;
    transition: background .3s;
    box-sizing: border-box;
}

@media (min-width: 868px){
    .current-resume:hover{
        background: var(--input-background-hover);
    }
}
</style>