import AppConfig from '../core/config';

const fetchAllResultCommands = async (uid) => {
    const url = `${AppConfig.api_base_url}/result/all_commands/${uid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchCheckSuccess = async (uid, tid) => {
    const url = `${AppConfig.api_base_url}/result/check_success/${uid}/${tid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchGetSuccessScenarios = async (aid) => {
    const url = `${AppConfig.api_base_url}/result/get_success_scenarios/${aid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

export {
    fetchAllResultCommands,
    fetchCheckSuccess,
    fetchGetSuccessScenarios,
};