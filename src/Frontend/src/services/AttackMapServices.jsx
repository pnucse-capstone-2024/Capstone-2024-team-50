import AppConfig from '../core/config';

const fetchGetAttackTactics = async () => {
    const url = `${AppConfig.api_base_url}/attack-map/tactics`;

    const response = await fetch(url, {
        method: 'GET',
        credentials: 'include',
    });

    return response;
}

const fetchGetAttackTechniques = async () => {
    const url = `${AppConfig.api_base_url}/attack-map/techniques`;

    const response = await fetch(url, {
        method: 'GET',
        credentials: 'include',
    });

    return response;
}

const fetchGetAttackCommands = async () => {
    const url = `${AppConfig.api_base_url}/attack-map/commands`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchGetAttackCommand = async (platform, attack_id) => {
    const url = `${AppConfig.api_base_url}/attack-map/command/${platform}/${attack_id}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchGetAttacks = async () => {
    const url = `${AppConfig.api_base_url}/attack-map/attacks`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

const fetchTestWifiDoS = async (uid) => {
    const url = `${AppConfig.api_base_url}/attack-map/tmp-set-attack/${uid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}
 

export { fetchGetAttackTactics, fetchGetAttackTechniques, fetchGetAttackCommands, fetchGetAttacks, fetchTestWifiDoS };