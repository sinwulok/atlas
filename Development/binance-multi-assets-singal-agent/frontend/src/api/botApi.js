import axios from 'axios';

const API_URL = 'http://localhost:8000/bot';

export const startBot = () => axios.post(`${API_URL}/start`);
export const stopBot = () => axios.post(`${API_URL}/stop`);
export const getBotStatus = () => axios.get(`${API_URL}/status`);