import InfoAPI from "./info"
import AuthAPI from "./auth"

class UserAPI {
    static auth = AuthAPI
    static info = InfoAPI
}

export default UserAPI