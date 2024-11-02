import employments from "../info/employments";
import locations from "../info/locations";
import workFormats from "../info/workFormats";
import LocationArea from "./location";

class VacancyListFilters {
	search: string = ""
	locations: Array<LocationArea> = []
	salaryRange: Array<number> = [0, 0]
	withSalary: boolean = false
	degreeIsRequired: boolean = false
	workFormats: Array<{value:number, title:string}> = []
	employments: Array<{value:number, title:string}> = []
	constructor(data:any) {
		if (data["s"]) {
			this.search = data["s"]
		}
		if (data["e"]) {
			if (Array.isArray(data["e"])) {
				data["e"] = data["e"].map((e) => Number(e))
				this.employments = employments.filter((employment) => {
					return data["e"].includes(employment.value)
				})
			} else {
				data["e"] = Number(data["e"])
				this.employments = employments.filter((employment) => {
					return employment.value === data["e"] 
				})
			}
		}
		if (data["l"]) {
			if (Array.isArray(data["l"])){
				data["l"] = data["l"].map((l) => Number(l))
				this.locations = locations.filter((loc) => {
					return data["l"].includes(loc.value)
				})
			} else {
				data["l"] = Number(data["l"])
				this.locations = locations.filter((loc) => {
					return loc.value === data["l"] 
				})
			}
		}

		if (data["wf"]) {
			if (Array.isArray(data["wf"])){
				data["wf"] = data["wf"].map((f) => Number(f))
				this.workFormats = workFormats.filter((f) => {
					return data["wf"].includes(f.value)
				})
			} else {
				data["wf"] = Number(data["wf"])
				this.locations = locations.filter((f) => {
					return f.value === data["wf"] 
				})
			}
		}

		if (data["s_min"]) {
			this.salaryRange[0] = Number(data["s_min"]) ?? 0
		}
		if (data["s_max"]) {
			this.salaryRange[1] = Number(data["s_max"]) ?? 0
		}
		if (data["s_max"] || data["s_min"]) {
			this.withSalary = true
		}
		if (data["d"]) {
			this.degreeIsRequired = true
		}
	}

	toQuery(){
		const query: any = {}

		if (this.search) {
			query["s"] = this.search
		}

		if (this.employments.length) {
			query["e"] = this.employments.map((employment) => {
				return employment.value
			})
		}

		if (this.locations.length) {
			query["l"] = this.locations.map((loc) => {
				return loc.value
			})
		}

		if (this.workFormats.length) {
			query["wf"] = this.workFormats.map((loc) => {
				return loc.value
			})
		}

		if (this.withSalary) {
			query["s_min"] = this.salaryRange[0]
			query["s_max"] = this.salaryRange[1]
		}

		if (this.degreeIsRequired) {
			query["d"] = true
		}

		return query
	}
}

export default VacancyListFilters