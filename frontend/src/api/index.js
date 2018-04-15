import axios from 'axios';
const API_URL = 'http://127.0.0.1:8888';
export default {
  translate(text, suite) {
    return axios.get(`${API_URL}/translate/${encodeURIComponent(text)}/${encodeURIComponent(suite)}`);
  },
  imageCaption(data,action) {
    return axios.post(`${API_URL}/image-caption/${action}`, data);
  },
};
