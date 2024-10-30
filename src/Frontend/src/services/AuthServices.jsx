import AppConfig from '../core/config';

const fetchSignIn = async (username, password) => {
    const url = `${AppConfig.api_base_url}/auth/sign-in`;

    const data = {
        grant_type: 'password',
        username,
        password,
        scope: null,
        client_id: null,
    };

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: Object.keys(data)
            .map(
                (key) =>
                    encodeURIComponent(key) +
                    '=' +
                    encodeURIComponent(data[key]),
            )
            .join('&'),
        credentials: 'include',
    });
    
    return response;
};

const fetchRefresh = async () => {
    const url = `${AppConfig.api_base_url}/auth/refresh`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
};

const fetchSignOut = async () => {
    const url = `${AppConfig.api_base_url}/auth/sign-out`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
};

export { fetchSignIn, fetchRefresh, fetchSignOut };
