import AppConfig from '../core/config';
// technique.tid가 tid
// attack에 tid가 있음
// command에 attack_id와 platform가 있음
// 그러면 사용자느 tid랑 uid를 보내주면 돼
// 백엔드에서는 tid로 attack_id를 찾아서 platform을 찾아서 command를 실행시키면 됨
// 해보자
const fetchRealAttackWithUIDTIDAID = async (uid, tid, aid) => {
    const url = `${AppConfig.api_base_url}/attack/${uid}/${tid}/${aid}`;

    const response = await fetch(url, {
        method: 'POST',
        credentials: 'include',
    });

    return response;
}

export {
    fetchRealAttackWithUIDTIDAID,
};