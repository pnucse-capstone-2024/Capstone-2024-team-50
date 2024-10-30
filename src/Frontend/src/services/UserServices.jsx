import AppConfig from '../core/config';

import { fetchRefresh } from './AuthServices';

const fetchMe = async () => {
    const url = `${AppConfig.api_base_url}/user/me`;

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
        credentials: 'include',
    });

    if (response.status === 401 || response.status === 422) {
        const refreshResponse = await fetchRefresh();

        if (refreshResponse.status === 200) {
            const retryResponse = await fetch(url, {
                method: 'GET',
                headers: {
                    Accept: 'application/json',
                },
                credentials: 'include',
            });

            return retryResponse;
        }
    }

    return response;
};

const fetchUpdateMe = async (userInfo) => {
    const url = `${AppConfig.api_base_url}/user/me`;

    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(userInfo),
    });

    if (response.status === 401 || response.status === 422) {
        const refreshResponse = await fetchRefresh();

        if (refreshResponse.status === 200) {
            const retryResponse = await fetch(url, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify(userInfo),
            });

            return retryResponse;
        }
    }
    return response;
};

const fetchUpdatePasswordMe = async (password) => {
    const url = `${AppConfig.api_base_url}/user/me/password`;

    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(password),
    });

    if (response.status === 401 || response.status === 422) {
        const refreshResponse = await fetchRefresh();

        if (refreshResponse.status === 200) {
            const retryResponse = await fetch(url, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify(password),
            });

            return retryResponse;
        }
    }
    return response;
};

const fetchUpdateUserInfo = async (userInfo) => {
    const url = `${AppConfig.api_base_url}/user/update`;

    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(userInfo),
    });

    return response;
};

const fetchTestRecord = async (uid) => {
    const url = `${AppConfig.api_base_url}/record/get/${uid}`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
        credentials: 'include',
    });

    return response;
};

const fetchTestRecordbyId = async (id) => {
    const url = `${AppConfig.api_base_url}/record/get/id/${id}`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
        credentials: 'include',
    });

    return response;
};

/* const fetchCVE = async (id) => {
    const url = `${AppConfig.api_base_url}/cve/cve`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
        credentials: 'include',
    });

    return response;
};
 */
const fetchCVE = async (id) => {
    const url = `${AppConfig.api_base_url}/cve/cve`;

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(id),
    });

    return response;
};

const fetchCVEResult = async (rid) => {
    const url = `${AppConfig.api_base_url}/cve_result/get/${rid}`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
        credentials: 'include',
    });

    return response;
}

const fetchCVERecord = async (rid) => {
    const url = `${AppConfig.api_base_url}/cve_result/record/${rid}`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
        credentials: 'include',
    });

    return response;
}

const fetchCVEResultbyRid = async (rid) => {
    const url = `${AppConfig.api_base_url}/cve_result/cve_attacks/${rid}`;
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
        credentials: 'include',
    });

    return response;
}

export { fetchMe, fetchUpdateMe, fetchUpdatePasswordMe, fetchUpdateUserInfo, fetchTestRecord, fetchCVEResult, fetchCVERecord, fetchCVEResultbyRid, fetchTestRecordbyId, fetchCVE };
