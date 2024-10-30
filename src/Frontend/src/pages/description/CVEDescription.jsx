import React from 'react';

import { useNavigate, } from 'react-router-dom';

import { Typography, IconButton } from '@mui/material'
import KeyboardDoubleArrowRightIcon from '@mui/icons-material/KeyboardDoubleArrowRight';

import cveInit from '../../static/images/descriptionImg/cveInit.png';
import cveIP from '../../static/images/descriptionImg/cveIP.png';
import cveAgent from '../../static/images/descriptionImg/cveAgent.png';
import cveEnd from '../../static/images/descriptionImg/cveEnd.png';

const CVEDescription = () => {
    const navigate = useNavigate();
    
    const gotoCVEattack = () => {
        navigate('/pentest/agentless');
    }

    const imgStyle = { margin: '10px 0 30px 0', width: '50%',  };
    const tmpImgStyle = { margin: '10px 0 30px 0', width:'40%',  };

    return (
        <div style={{ padding: '20px', backgroundColor: '#ebeff7', borderRadius: '10px'  }}>
            <Typography variant='h6' sx={{ fontWeight: 'bold', color: '#3A74CD',  }}>  CVE란? </Typography>
            <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
                {`CVE는 Common Vulnerabilities and Exposures의 약자로, 공개적으로 알려진 컴퓨터 보안 취약점 목록입니다.`}
            </Typography>

            <Typography variant='h6' sx={{ fontWeight: 'bold', color: '#3A74CD',  mt: 5, mb: 1 }}> CVE ATTACK 페이지 설명 </Typography>
            <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
            <strong> 1. 초기 화면 </strong>
{`
    - CVE ATTACK 페이지에 접속하면 아래 그림과 같이 초기 화면이 나타납니다.`}
            <img src={cveInit} style={imgStyle}/>

            
            <strong> 2. 공격 대상 선택 </strong>

{`
    -  CVE ATTACK 메뉴는 Agent 없이 IP만으로도 공격을 시도할 수 있습니다.
    - 아래 그림과 같이 IP를 입력하거나 Agent를 선택하여 공격 대상을 선택하고 ATTACK 버튼을 누르면 공격이 시작됩니다.`}

            <div style={{ display: 'flex', direction: 'row', alignItems: 'center' }}>
                <img src={cveIP} style={tmpImgStyle}/>            
                <img src={cveAgent} style={tmpImgStyle}/>
            </div>            
            <strong> 3. 공격 완료 </strong>
{`
    - 공격이 완료되면 아래 그림과 같이 공격 결과가 나타납니다. 공격 완료 후 활성화된 GO TO RESULT 버튼을 누르면 공격 결과 페이지로 이동합니다.
    - 공격 결과 페이지에서는 완성된 공격 시나리오 및 공격에 사용된 Command, Mitigation 등을 확인할 수 있습니다.`}
            <img src={cveEnd} style={imgStyle}/>
            </Typography>

            <div style={{ display: 'flex', direction: 'row', alignItems: 'center', justifyContent: 'flex-end' }}>
                <Typography sx={{ color: '#757575', mr: 1}}> CVE ATTACK 페이지로 이동 </Typography>
                <IconButton aria-label="clear" onClick={gotoCVEattack} >
                    <KeyboardDoubleArrowRightIcon/>
                </IconButton>
            </div>
        </div>
    )
}

export default CVEDescription;