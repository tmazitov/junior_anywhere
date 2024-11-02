class Vacancy {
	id: number
	name: string
	companyName: string
	salary: number
	city: string
	/**
	 *
	 */
	constructor(data:any) {
		this.id = data["id"]
		this.name = data["name"]
		this.city = data["city"]
		this.companyName = data["companyName"]
		this.salary = data["salary"]
	}
}

export default Vacancy