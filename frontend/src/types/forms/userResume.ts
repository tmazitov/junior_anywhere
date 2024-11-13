

class UserResume {
	name:string = ""
	experienceInYears:number|null = null
	skills:string[] = []
	description:string = ""

	validate() : boolean{

		const checks:boolean[] = [
			this.name.length == 0,
			this.experienceInYears == null,
			Number.isNaN(this.experienceInYears),
			this.skills.length < 3,
			this.skills.find(skill => skill.length == 0) != undefined
		]

		return !checks.find(result =>result)
	}
}

export default UserResume