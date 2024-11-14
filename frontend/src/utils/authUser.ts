class UserAuth {
	static keyName:string="user-key"

	static getUserId() : number|undefined{
		const rawValue = localStorage.getItem(this.keyName)
		if (!rawValue || Number.isNaN(Number(rawValue)))
			return undefined
		return Number(rawValue)
	}

	static setUserId(value:number){
		localStorage.setItem(this.keyName, value.toString())
	}
	
	static delUserId(){
		localStorage.removeItem(this.keyName)
	}
}

export default UserAuth