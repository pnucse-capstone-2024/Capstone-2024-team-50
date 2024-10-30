import React from 'react';
import { useNavigate, } from 'react-router-dom';

import { Typography, IconButton } from '@mui/material'
import KeyboardDoubleArrowRightIcon from '@mui/icons-material/KeyboardDoubleArrowRight';

import  AgentInfoPage from '../../static/images/descriptionImg/Agent info.png';
import  initialPage from '../../static/images/descriptionImg/initial page.png';
import  shell from '../../static/images/descriptionImg/shell.png';

const AgentInfoDescription = () => {
    const navigate = useNavigate();

    const gotoAgentInfo = () => {
        navigate('/pentest/info-agent');
    }

    const imgStyle = { margin: '10px 0 30px 0', width: '75%',/*  border:'1px solid black'  */};


    return (
        <div style={{ padding: '20px', backgroundColor: '#ebeff7', borderRadius: '10px' }}>
            <Typography variant='h6' sx={{ fontWeight: 'bold', color: '#3A74CD', }}> Agent란? </Typography>
            <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
                {`Agent는 공격 대상 시스템에 설치되는 프로그램으로, 공격 대상 시스템에 설치되어 공격을 시도합니다.
이 플랫폼에서는 Agent가 설치되지 않았다면 CVE ATTACK 메뉴만을 이용해 공격을 시도할 수 있으며 Agent가 설치되어 있다면 MITRE ATT&CK와 CVE ATTACK 메뉴 모두를 이용해 공격을 시도할 수 있습니다.`}
            </Typography>

            <Typography variant='h6' sx={{ fontWeight: 'bold', color: '#3A74CD', mt: 5, mb: 1 }}> Agent Info 페이지 설명 </Typography>
            <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
            <strong> 1. 초기 화면 </strong>
{`
    - 어떤 Agent도 연결되어 있지 않았을 때 보이는 테이블입니다. Agent를 연결하면 테이블에 Agent 정보가 추가됩니다. 상단의 연결 혹은 삭제 버튼을 눌러 Agent를 연결하거나 삭제할 수 있습니다.`}
            <img src={initialPage} style={imgStyle}/>
            <strong> 2. Agent 연결 </strong>

{`
    - 연결 버튼을 누르면 아래 그림과 같이 Agent를 설치할 수 있는 명령어가 OS 별로 나타납니다. 해당 명령어를 복사하여 Agent를 설치할 대상 시스템에 입력하면 Agent가 설치됩니다.
    - (1) 복사 버튼을 누르면 (2) 해당 명령어가 복사됩니다.`}
            <img src={shell} style={imgStyle}/>
            <strong> 3. Agent 설치 완료 </strong>
{`
    - Agent를 성공적으로 설치하면 아래 그림과 같이 Agent 정보가 테이블에 추가됩니다. 테이블에 존재하는 Agent들로 MITRE ATT&CK 메뉴의 기능을 수행할 수 있습니다.`}
            <img src={AgentInfoPage} style={imgStyle}/>
            </Typography>

            <div style={{ display: 'flex', direction: 'row', alignItems: 'center', justifyContent: 'flex-end' }}>
                <Typography sx={{ color: '#757575', mr: 1}}> Agent Info 페이지로 이동 </Typography>
                <IconButton aria-label="clear" onClick={gotoAgentInfo} >
                    <KeyboardDoubleArrowRightIcon/>
                </IconButton>
            </div> 
        </div>
    )
}

export default AgentInfoDescription;