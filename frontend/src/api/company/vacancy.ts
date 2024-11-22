import vacancies from "../../info/vacancies";
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
}

export default VacancyAPI