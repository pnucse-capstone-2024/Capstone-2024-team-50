import AppConfig from '../core/config';

const fetchGetKaliHosts = async () => {
    const url = `${AppConfig.api_base_url}/kali_result/kali_hosts`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchGetKaliHostServices = async () => {
    const url = `${AppConfig.api_base_url}/kali_result/kali_host_services`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

export {
    fetchGetKaliHosts,
    fetchGetKaliHostServices
};