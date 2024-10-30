import AppConfig from '../core/config';

const fetchTest = async () => {
    const url = `${AppConfig.api_base_url}/test/me`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}
export { fetchTest };