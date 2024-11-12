<template>
    <div class="company-vacancy-list">
        <div class="company-vacancy-list__item"
        v-for="vacancy in vacancies" 
        :key="`${vacancy.id}`">
            <div class="item-name">
                {{ vacancy.name }}
            </div>

            <div class="item-details">
                <div class="details-applies">
                    <Icon icon="tabler:user" height="1.2em" color="var(--primary-color)"/>
                    {{ vacancy.applies }}
                </div>
                <div class="details-location">
                    <Icon icon="tabler:map-pin" height="1.2em" color="var(--primary-color)"/>
                    {{ getLocationName(vacancy.locationId) }}
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { Icon } from '@iconify/vue/dist/iconify.js';
import locations from '../../info/locations';
import Vacancy from '../../types/vacancy';

defineProps({
    vacancies: {
        type: Array<Vacancy>,
        required: true,
    }
})


const getLocationName = (id:number) => {
    return locations.find(loc => loc.value == id)?.title
}

</script>

<style scoped>
.company-vacancy-list{
    display: flex;
    flex-direction: column;
    max-height: 400px;
    overflow-y: auto;
}
.company-vacancy-list__item{
    padding: 12px;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.company-vacancy-list__item:not(:first-child){
    border-top: 1px solid var(--timberwolf);
}

.item-name{
    font-size: 1.25em;
}

.item-details {
    display: flex;
    flex-direction: row;
    gap: 12px;
}

.details-applies{
    width: calc(16px + 4ch);
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.95em;
    color: #616161;

}

.details-location{
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.95em;
    color: #616161;
}

</style>
