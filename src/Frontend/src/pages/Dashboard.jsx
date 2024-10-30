import React, {useContext} from 'react';
import { Typography, Box, Paper } from '@mui/material';
import { useNavigate } from 'react-router-dom';

import AgentInfo from './pentest/AgentInfo';

import {UserContext} from '../core/user';

import ResultMap from './pentest/module/ResultMap';
import { fetchAgents } from '../services/AgentServices';
import { useState } from 'react';

const Dashboard = () => {
    const { userState } = useContext(UserContext);
    const navigate = useNavigate();
    const [agentCount, setAgentCount] = React.useState(0);
    const [connectedAgentCount, setConnectedAgentCount] = React.useState(0);
    const [linuxAgentCount, setLinuxAgentCount] = React.useState(0);
    const [windowsAgentCount, setWindowsAgentCount] = React.useState(0);

    useState(() => {
        fetchAgents(userState.uid)
            .then(response => response.json())
            .then(data => {
                setAgentCount(data.length);
                setConnectedAgentCount(data.filter(agent => agent.connected).length);
                setWindowsAgentCount(data.filter(agent => agent.os.includes('Windows')).length);
                setLinuxAgentCount(data.filter(agent => !agent.os.includes('Windows')).length);
            })
            .catch(error => {
                console.error('Error fetching agents:', error);
            });         
    }, []);

    return (
        <div style={{ padding: '20px', backgroundColor: '#f5f5f5' }}>
            {/* Overview Cards */}
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
                <Paper elevation={3} style={{ padding: '20px', flex: '1', minWidth: '250px' }}>
                    <Typography variant='h6' color='textSecondary'>전체 호스트 수</Typography>
                    <Typography variant='h4' color='primary' style={{ fontWeight: 'bold', cursor: 'pointer' }} onClick={() => navigate('/pentest/info-agent')}>
                        {agentCount}
                    </Typography>
                </Paper>
                <Paper elevation={3} style={{ padding: '20px', flex: '1', minWidth: '250px' }}>
                    <Typography variant='h6' color='textSecondary'>연결된 에이전트</Typography>
                    <Typography variant='h4' color='primary' style={{ fontWeight: 'bold', cursor: 'pointer' }} onClick={() => navigate('/pentest/info-agent')}>
                        {connectedAgentCount}
                    </Typography>
                </Paper>
                <Paper elevation={3} style={{ padding: '20px', flex: '1', minWidth: '250px' }}>
                    <Typography variant='h6' color='textSecondary'>리눅스/MAC host</Typography>
                    <Typography variant='h4' color='primary' style={{ fontWeight: 'bold', cursor: 'pointer' }} onClick={() => navigate('/pentest/info-agent')}>
                        {linuxAgentCount}
                    </Typography>
                </Paper>
                <Paper elevation={3} style={{ padding: '20px', flex: '1', minWidth: '250px' }}>
                    <Typography variant='h6' color='textSecondary'>윈도우 host</Typography>
                    <Typography variant='h4' color='primary' style={{ fontWeight: 'bold', cursor: 'pointer' }} onClick={() => navigate('/pentest/info-agent')}>
                        {windowsAgentCount}
                    </Typography>
                </Paper>
            </div>

            {/* Vulnerability Metrics */}
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px', marginTop: '20px' }}>
                <Paper elevation={3} style={{ padding: '20px', flex: '1', minWidth: '250px' }}>
                    <Typography variant='h6' color='textSecondary'>취약한 호스트</Typography>
                    <Typography variant='h4' color='error' style={{ fontWeight: 'bold', cursor: 'pointer' }} onClick={() => navigate('/pentest/result')}>
                        0
                    </Typography>
                </Paper>
                <Paper elevation={3} style={{ padding: '20px', flex: '1', minWidth: '250px' }}>
                    <Typography variant='h6' color='textSecondary'>발견된 취약점</Typography>
                    <Typography variant='h4' color='error' style={{ fontWeight: 'bold', cursor: 'pointer' }} onClick={() => navigate('/pentest/result')}>
                        0
                    </Typography>
                </Paper>
                <Paper elevation={3} style={{ padding: '20px', flex: '1', minWidth: '250px' }}>
                    <Typography variant='h6' color='textSecondary'>공격 성공</Typography>
                    <Typography variant='h4' color='error' style={{ fontWeight: 'bold', cursor: 'pointer' }} onClick={() => navigate('/pentest/result')}>
                        0
                    </Typography>
                </Paper>
            </div>

            {/* Additional Information */}
            <div style={{ marginTop: '20px' }}>
                <Paper elevation={3} style={{ padding: '20px' }}>
                    <Typography variant='h5' style={{ fontWeight: 'bold', marginBottom: '20px' }}>Agent Information</Typography>
                    <AgentInfo view={true} />
                </Paper>
            </div>
            <div style={{ marginTop: '20px' }}>
                <Paper elevation={3} style={{ padding: '20px' }}>
                    <Typography variant='h5' style={{ fontWeight: 'bold', marginBottom: '20px' }}>Result</Typography>
                    {/* Add ResultMap component here if needed */}
                </Paper>
            </div>
        </div>
    );
}

export default Dashboard;
