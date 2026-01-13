import axios from 'axios';

// Determine API base URL
const getApiBaseUrl = () => {
  // Check if running in codespace by looking for codespace in URL
  if (window.location.hostname.includes('app.github.dev')) {
    const codespaceName = window.location.hostname.split('-3000')[0];
    return `https://${codespaceName}-8000.app.github.dev`;
  }
  return 'http://localhost:8000';
};

const api = axios.create({
  baseURL: getApiBaseUrl(),
  // withCredentials: true,  // Removed for token-only authentication
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

export default api;