import AppConfig from '../core/config';

const fetchAgents = async (uid) => {
    const url = `${AppConfig.api_base_url}/agent/all/${uid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchConnectedAgents = async (uid) => {
    const url = `${AppConfig.api_base_url}/agent/connected/all/${uid}`;
    
    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchDeleteAgent = async (agentId) => {
    const url = `${AppConfig.api_base_url}/agent/delete/${agentId}`;

    const response = await fetch(url, {
        method: 'DELETE',
        credentials: 'include',
    });

    return response;
}

const fetchGetConnectAgentCommand = async (uid) => {
    const url = `${AppConfig.api_base_url}/agent/command/${uid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });
    
    return response;
}

const fetchGetAgentCount = async (uid) => {
    const url = `${AppConfig.api_base_url}/agent/count/${uid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchGetVulerableHostCount = async (uid) => {
    const url = `${AppConfig.api_base_url}/agent/vulnerable/${uid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchTestLinux = async (uid) => {
    const url = `${AppConfig.api_base_url}/attack/test/linux/${uid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchgetTest = async (uid) => {
    const url = `${AppConfig.api_base_url}/attack/test/${uid}`;

    const response = await fetch(url, {
        method: 'get',
        credentials: 'include',
    });

    return response;
}

const fetchGetAgentPrepareStatus = async (aid) => {
    const url = `${AppConfig.api_base_url}/agent/prepare/status/${aid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

export { fetchConnectedAgents, fetchGetAgentPrepareStatus, fetchgetTest, fetchTestLinux, fetchAgents, fetchDeleteAgent, fetchGetConnectAgentCommand, fetchGetAgentCount, fetchGetVulerableHostCount };