import employments from "../info/employments";
import locations from "../info/locations";
import LocationArea from "./location";

class VacancyListFilters {
	search: string = ""
	locations: Array<LocationArea> = []
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

		return query
	}
}

export default VacancyListFilters