import axios from 'axios';

export default axios.create({
    baseURL: process.env.NODE_ENV === 'production' ? 'https://earcast.jkrclaro.com/' : 'http://earcast.localhost:8000/'
})