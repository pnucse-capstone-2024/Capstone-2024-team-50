import React from 'react';
import { useNavigate, } from 'react-router-dom';

import { Typography, IconButton } from '@mui/material'
import KeyboardDoubleArrowRightIcon from '@mui/icons-material/KeyboardDoubleArrowRight';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';

import AgentSelect from '../../static/images/descriptionImg/agentSelect.png';
import AttackStart from '../../static/images/descriptionImg/startAttack.png';
import AttackIng from '../../static/images/descriptionImg/attacking.png';
import AttackResult from '../../static/images/descriptionImg/attackResult.png';

const MITREDescription = () => {
    const navigate = useNavigate();

    const gotoMITREattack = () => {
        navigate('/pentest/agent');
    }

    const imgStyle = { margin: '10px 0 30px 0', width: '50%',  };
    const tmpImgStyle = { margin: '10px 0 30px 0', width:'40%',  };

    return (
        <div style={{ padding: '20px', backgroundColor: '#ebeff7', borderRadius: '10px'  }}>
            <Typography variant='h6' sx={{ fontWeight: 'bold', color: '#3A74CD',  }}> MITRE ATT&CK이란? </Typography>
            <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
                {`MITRE ATT&CK는 사이버 공격의 기술과 전술을 체계적으로 정리한 지식 기반으로, 공격자가 공격을 수행하는 방식과 이를 방어하기 위한 방법을 정의합니다. 
공격방법(Tactic)과 기술(Technique)의 관점으로 분석하여 다양한 공격 그룹의 공격기법들에 대한 정보를 분류해 목록화한 표준적인 정보들을 제공합니다.`}
            </Typography>

            <Typography variant='h6' sx={{ fontWeight: 'bold', color: '#3A74CD',  mt: 5, mb: 1 }}> MITRE ATT&CK 페이지 설명 </Typography>
            <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
            <strong> 1. Agent 선택 </strong>
{`
    - 연결할 Agent를 선택합니다. Agent가 없다면 Agent를 설치해야 합니다. Agent를 설치하는 방법은 Agent Info 페이지를 참고하세요.
    - Agent를 선택하면 아래 그림과 같이 ATTACK 버튼이 활성화되고 해당 버튼을 누르면 공격이 시작됩니다.`}
            <div style={{ display: 'flex', direction: 'row', alignItems: 'center' }}>
                <img src={AgentSelect} style={tmpImgStyle}/>
                <ArrowForwardIcon sx={{ width: '10%', }}/>
                <img src={AttackStart} style={tmpImgStyle}/>
            </div>

            <strong> 2. 공격 시도 중 </strong>

{`
    - ATTACK 버튼을 누르면 아래 그림과 같이 공격이 시작됩니다.
    - 박스의 색깔은 Technique의 상태를 나타냅니다.
        * 파란색: 현재 실행 중인 Technique
        * 빨간색: 공격이 실패한 Technique
        * 초록색: 공격이 성공한 Technique`}
            <img src={AttackIng} style={imgStyle}/>
            <strong> 3. 공격 완료 </strong>
{`
    - 공격이 완료되면 아래 그림과 같이 공격 결과가 나타납니다. 공격 완료 후 활성화된 GO TO RESULT 버튼을 누르면 공격 결과 페이지로 이동합니다.
    - 공격 결과 페이지에서는 완성된 공격 시나리오 및 공격에 사용된 Command, Mitigation 등을 확인할 수 있습니다.`}
            <img src={AttackResult} style={imgStyle}/>
            </Typography>
            
            <div style={{ display: 'flex', direction: 'row', alignItems: 'center', justifyContent: 'flex-end' }}>
                <Typography sx={{ color: '#757575', mr: 1}}> MITRE ATT&CK 페이지로 이동 </Typography>
                <IconButton aria-label="clear" onClick={gotoMITREattack} >
                    <KeyboardDoubleArrowRightIcon/>
                </IconButton>
            </div> 
        </div>
    )
}

export default MITREDescription;