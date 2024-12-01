import UserResume from "../../types/forms/userResume";
import client from "./client";

class InfoAPI {
    static async general(userId:number) {
        return client.get(`${userId}`)
    }

    static async uploadResume(userId:number, form:UserResume) {
        return client.post(`${userId}/resume/create`, form.toRequestBody())
    }

    static async getResume(userId:number) {
        return client.get(`${userId}/resume/get`)
    }
}

export default InfoAPI;