import validateEmail from "../../utils/emailValidation";


class RegisterUser {
	fullName: string = "";
	email: string = "";
	password: string = "";
	agree: boolean = false;

	validate() : boolean {

		if (!this.agree)
			return false;

		if (!validateEmail(this.email)) {
			return false;
		}

		if (this.password.length < 8) {
			return false;
		}

		if (this.fullName.length < 3) {
			return false;
		}

		return true
	}
}

export default RegisterUser;