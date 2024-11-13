import validateEmail from "../../utils/emailValidation";


class RegisterCompany {
	name: string = "";
	email: string = "";
	documentId: string = "";
	password: string = "";
	companyType: {value:number, title: string}|null = null
	agree: boolean = false;

	validate() : boolean {

		if (!this.agree)
			return false;

		if (this.documentId.length == 0) {
			return false
		} 

		if (this.companyType == null) {
			return false
		}

		if (!validateEmail(this.email)) {
			return false;
		}

		if (this.password.length < 8) {
			return false;
		}

		if (this.name.length < 3) {
			return false;
		}

		return true
	}
}

export default RegisterCompany;