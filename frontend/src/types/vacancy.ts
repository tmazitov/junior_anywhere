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
	description: string|undefined
	employmentId:number|undefined
	locationId: number
	experience: number|undefined
	applies: number|undefined
	skills: string[] = []
	workFormatId: number|undefined
	withDegree: boolean = false
	status: VacancyStatus = 1
	/**
	 *
	 */
	constructor(data:any) {
		this.id = data["id"]
		this.name = data["name"]
		this.description = data["description"]
		this.companyName = data["companyName"]
		this.salary = data["salary"]
		this.locationId = data["locationId"]
		this.applies = data["applies"]
		this.workFormatId = data["workFormatId"]
		this.employmentId = data["employmentId"]
		this.experience = data["experience"]
		this.withDegree = data["withDegree"]
		this.skills = data["skills"] ? data["skills"].split(" ") : []
		if (data["status"]) {
			this.status = data["status"]
		}
	}
}

export default Vacancy