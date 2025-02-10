import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export const login = async (username, password) => {
    const response = await axios.post(`${API_URL}token/`, { username, password });
    localStorage.setItem('access', response.data.access);
    localStorage.setItem('refresh', response.data.refresh);
    return response.data;
};

export const getProtectedData = async () => {
    const token = localStorage.getItem('access');
    const response = await axios.get(`${API_URL}protected/`, {
        headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
};
