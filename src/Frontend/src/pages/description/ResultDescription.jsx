import React from 'react';
import { useNavigate, } from 'react-router-dom';

import { Typography, IconButton } from '@mui/material'
import KeyboardDoubleArrowRightIcon from '@mui/icons-material/KeyboardDoubleArrowRight';

import showResult from '../../static/images/descriptionImg/showResult.png';
import viewDetail from '../../static/images/descriptionImg/viewDetail.png';

const ResultDescription = () => {
    const navigate = useNavigate();

    const gotoResult = () => {
        navigate('/pentest/result');
    }

    const imgStyle = { margin: '10px 0 30px 0', width: '50%',  };

    return (
        <div style={{ padding: '20px', backgroundColor: '#ebeff7', borderRadius: '10px'  }}>
            <Typography variant='h6' sx={{ fontWeight: 'bold', color: '#3A74CD',  }}>  Result 페이지 </Typography>
            <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
                {`Agent는 공격 대상 시스템에 설치되는 프로그램으로, 공격 대상 시스템에 설치되어 공격을 시도합니다.
이 플랫폼에서는 Agent가 설치되지 않았다면 CVE ATTACK 메뉴만을 이용해 공격을 시도할 수 있으며 Agent가 설치되어 있다면 MITRE ATT&CK와 CVE ATTACK 메뉴 모두를 이용해 공격을 시도할 수 있습니다.`}
            </Typography>

            <Typography variant='h6' sx={{ fontWeight: 'bold', color: '#3A74CD',  mt: 5, mb: 1 }}> Show Result 페이지 설명 </Typography>
            <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
            <strong> 1. 공격 시나리오 출력 </strong>
{`
    - Show Result 페이지에서는 성공한 공격 시나리오를 출력합니다.
    - 아래 그림은 대상 시스템에 대해 WIFI DOS 공격이 성공했고 이는 대상 시스템이 해당 공격에 취약함을 나타냅니다.
    - VIEW DETAIL 버튼을 누르면 해당 시나리오에 대해 자세한 정보를 확인할 수 있습니다.`}
            <img src={showResult} style={imgStyle}/>

            
            <strong> 2. VIEW DETAIL </strong>

{`
    - VIEW DETAIL 버튼을 누르면 아래 그림과 같이 공격 순서, 사용된 Command, Mitigation 등을 확인할 수 있습니다.
    - 이를 통해 공격에 사용된 Command를 확인하고, 이에 대한 대응책을 마련할 수 있습니다.`}
            <img src={viewDetail} style={imgStyle}/>
            </Typography>

            <div style={{ display: 'flex', direction: 'row', alignItems: 'center', justifyContent: 'flex-end' }}>
                <Typography sx={{ color: '#757575', mr: 1}}> Show Result 페이지로 이동 </Typography>
                    <IconButton aria-label="clear" onClick={gotoResult} >
                        <KeyboardDoubleArrowRightIcon/>
                    </IconButton>
                </div>
        </div>
    )
}

export default ResultDescription;