import RegisterCompany from "../../types/forms/registerCompany";
import client from "./client";

class AuthAPI {
    static login(email:string, password:string) {
        return client.post('auth', {
            email: email,
            password: password
        });
    }
    static register(form:RegisterCompany) {
        return client.post('register', form.toRequestBody());
    }
}

export default AuthAPI