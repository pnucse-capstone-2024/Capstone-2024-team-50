import AppConfig from '../core/config';

const fetchTest = async () => {
    const url = `${AppConfig.api_base_url}/kali/test`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchPentestToolsByCategory = async (category) => {
    const url = `${AppConfig.api_base_url}/kali/category/${category}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchBasicScanByIP = async (ip) => {
    const url = `${AppConfig.api_base_url}/kali/basic_scan/${ip}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchServiceScanByIP = async (ip) => {
    const url = `${AppConfig.api_base_url}/kali/service_scan/${ip}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchGetServicesByIP = async (ip) => {
    const url = `${AppConfig.api_base_url}/kali/get_services/${ip}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchAttackWithIPAndToolID = async (ip, toolID) => {
    const url = `${AppConfig.api_base_url}/kali/attack/${ip}/${toolID}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

export {
    fetchTest,
    fetchPentestToolsByCategory,
    fetchBasicScanByIP,
    fetchServiceScanByIP,
    fetchGetServicesByIP,
    fetchAttackWithIPAndToolID
};