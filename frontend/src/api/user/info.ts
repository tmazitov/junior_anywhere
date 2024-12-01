import client from "./client";

class InfoAPI {
    static async general(userId:number) {
        return client.get(`${userId}`)
    }
}

export default InfoAPI;