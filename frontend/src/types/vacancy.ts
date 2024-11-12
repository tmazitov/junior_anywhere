enum VacancyStatus {
	Uploaded = 1,
	Canceled,
	Hired,
}

class Vacancy {
	id: number
	name: string
	companyName: string
	salary: number
	locationId: number
	applies: number|undefined
	status: VacancyStatus = 1
	/**
	 *
	 */
	constructor(data:any) {
		this.id = data["id"]
		this.name = data["name"]
		this.companyName = data["companyName"]
		this.salary = data["salary"]
		this.locationId = data["locationId"]
		this.applies = data["applies"]

		if (data["status"]) {
			this.status = data["status"]
		}
	}
}

export default Vacancy