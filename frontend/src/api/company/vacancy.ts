import vacancies from "../../info/vacancies";
import VacancyCreate from "../../types/forms/vacancyCreate";
import VacancyListFilters from "../../types/vacancyListFilters";
import { fakeRequest } from "../utils/fakeRequest";
import client from "./client";

class VacancyAPI {

    static mockVacancies = import.meta.env.DEV ? vacancies : null

    static async list(filters:VacancyListFilters) {
        return await fakeRequest({
            responseData: () => {
                return this.mockVacancies?.filter(vacancy => {
                    return filters.check(vacancy)
                })
            },
            delay: 1000,
        });
    }

    static async listByCompany(companyId:number, filters:VacancyListFilters) {
        return client.get(`${companyId}/vacancy_filter?${filters.toQueryStr()}`)
    }

    static async submit(companyId:number, form:VacancyCreate) {
        return client.post(`${companyId}/vacancy`, form.toRequestBody())
    }

    static async details(companyId:number, vacancyId:number) {
        return client.get(`${companyId}/vacancy/${vacancyId}/view`)
    }
}

export default VacancyAPI