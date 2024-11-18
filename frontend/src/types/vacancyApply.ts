class VacancyApply {
    userId : number
    userName : string
    resumeName: string
    constructor(data:any) {
        this.userName = data["userName"]
        this.userId = data["userId"]
        this.resumeName = data["resumeName"]
    }
}

export default VacancyApply