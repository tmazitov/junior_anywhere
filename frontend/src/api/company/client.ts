import axios from "axios";

const client = axios.create({
    baseURL: '/company',
    timeout: 1000,
});
  
export default client;