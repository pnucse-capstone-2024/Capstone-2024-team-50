// this file is used to proxy the request to the backend server
// so that we can avoid CORS issue in development
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
    app.use(
        '/api',
        createProxyMiddleware({
            target: 'http://localhost:8000/api',
            changeOrigin: true,
        }),
    );
};
