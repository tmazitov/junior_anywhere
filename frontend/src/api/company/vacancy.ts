import vacancies from "../../info/vacancies";
import VacancyCreate from "../../types/forms/vacancyCreate";
import VacancyListFilters from "../../types/vacancyListFilters";
import { fakeRequest } from "../utils/fakeRequest";

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

    static async listByCompany(filters:VacancyListFilters, companyId:number) {
        console.log(companyId)
        return await fakeRequest({
            responseData: () => {
                return this.mockVacancies?.filter(vacancy => {
                    return filters.check(vacancy)
                })
            },
            delay: 1000,
        });
    }

    static async submit(companyId:number, form:VacancyCreate) {
        console.log(companyId,form)
        return await fakeRequest({
            responseData: () => {
                return null
            },
            delay: 1000,
        });
    }
}

export default VacancyAPI