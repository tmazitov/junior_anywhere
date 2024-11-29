import RegisterUser from "../../types/forms/registerUser";
import SignInUser from "../../types/forms/signInUser";
import client from "./client";

class AuthAPI {
    static login(form: SignInUser) {
        return client.post('auth', {
            email: form.email,
            password: form.password
        });
    }
    static register(form:RegisterUser) {
        return client.post('register', form.toRequestBody());
    }
}

export default AuthAPI