import axios from "axios";

const client = axios.create({
    baseURL: '/user',
    timeout: 1000,
});
  
export default client;