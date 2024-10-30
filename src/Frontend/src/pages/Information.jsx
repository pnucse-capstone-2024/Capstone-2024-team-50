import React, { useState } from 'react';
import { useNavigate, } from 'react-router-dom';

import AgentInfoDescription from './description/AgentInfoDescription';
import MITREDescription from './description/MITREDescription';
import CVEDescription from './description/CVEDescription';
import ResultDescription from './description/ResultDescription';

import { Typography, IconButton, Button } from '@mui/material'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import Collapse from '@mui/material/Collapse';

const Information = () => {
    const [agentInfoOpen, setAgentInfoOpen] = useState(true);
    const [MITREOpen, setMITREOpen] = useState(false);
    const [CVEOpen, setCVEOpen] = useState(false);
    const [resultOpen, setResultOpen] = useState(false);

    const handleAgentInfoClick = () => {
        setAgentInfoOpen(!agentInfoOpen);
    };

    const handleMITREClick = () => {
        setMITREOpen(!MITREOpen);
    };
    
    const handleCVEClick = () => {
        setCVEOpen(!CVEOpen);
    };

    const handleResultClick = () => {
        setResultOpen(!resultOpen);
    };




    return (
        <div>
            <Typography variant='h4' sx={{ fontWeight: 'bold', mb: 5 }}> 이용 방법 </Typography>
            <div  style={{ border: '2px solid #ddd', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding:'20px' }}>
                <div style={{ display: 'flex', direction: 'row', alignItems: 'center', marginBottom: '20px' }}>
                    <Typography variant='h5' sx={{ fontWeight: 'bold', }}> Agent Information </Typography>
                    <IconButton aria-label="clear" onClick={handleAgentInfoClick} sx={{ marginLeft: '10px' }}>
                        {agentInfoOpen ? <ExpandLessIcon/> : <ExpandMoreIcon/>}
                    </IconButton>
                </div>
                <Collapse in={agentInfoOpen}>
                    <AgentInfoDescription/>
                </Collapse>
            </div>

            <div  style={{ border: '2px solid #ddd',  marginTop: '20px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding:'20px' }}>
                <div style={{ display: 'flex', direction: 'row', alignItems: 'center',  marginBottom: '20px'  }}>
                    <Typography variant='h5' sx={{ fontWeight: 'bold', }}> MITRE ATT&CK </Typography>
                    <IconButton aria-label="clear" onClick={handleMITREClick} sx={{ marginLeft: '10px' }}>
                        {MITREOpen ? <ExpandLessIcon/> : <ExpandMoreIcon/>}
                    </IconButton>
                </div>
                <Collapse in={MITREOpen}>
                    <MITREDescription/>
                </Collapse>

            </div>

            <div  style={{ border: '2px solid #ddd',  marginTop: '20px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding:'20px' }}>
                <div style={{ display: 'flex', direction: 'row', alignItems: 'center',  marginBottom: '20px'  }}>
                    <Typography variant='h5' sx={{ fontWeight: 'bold', }}> CVE ATTACK </Typography>
                    <IconButton aria-label="clear" onClick={handleCVEClick} sx={{ marginLeft: '10px' }}>
                        {CVEOpen ? <ExpandLessIcon/> : <ExpandMoreIcon/>}
                    </IconButton>
                </div>
                <Collapse in={CVEOpen}>
                    <CVEDescription/>
                </Collapse>

            </div>

            <div  style={{ border: '2px solid #ddd',  marginTop: '20px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding:'20px' }}>
                <div style={{ display: 'flex', direction: 'row', alignItems: 'center',  marginBottom: '20px'  }}>
                <   Typography variant='h5' sx={{ fontWeight: 'bold', }}> Show Result </Typography>
                    <IconButton aria-label="clear" onClick={handleResultClick} sx={{ marginLeft: '10px' }}>
                        {resultOpen ? <ExpandLessIcon/> : <ExpandMoreIcon/>}
                    </IconButton>
                </div>
                <Collapse in={resultOpen}>
                    <ResultDescription/>                
                </Collapse>

            </div>
        </div>
    )
}

export default Information;