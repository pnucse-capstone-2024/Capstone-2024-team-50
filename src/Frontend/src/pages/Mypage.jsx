import React, { useContext, useState, useEffect } from 'react';
import { UserContext } from '../core/user';
import { useNavigate, } from 'react-router-dom';

import { fetchUpdateUserInfo, fetchTestRecord, fetchTestRecordbyId, fetchCVE } from '../services/UserServices';
import { fetchAgents } from '../services/AgentServices';

import { Box, Button, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, IconButton, Tooltip } from '@mui/material'
import KeyboardDoubleArrowRightIcon from '@mui/icons-material/KeyboardDoubleArrowRight';


const Mypage = () => {
    const { userState } = useContext(UserContext);
    const navigate = useNavigate();

    const [stateModi, setStateModi] = useState(0);
    const [name, setName] = useState(userState.username);
    const [email, setEmail] = useState(userState.email);
    const [agentInfo, setAgentInfo] = useState([]);
    const [testRecord, setTestRecord] = useState([]);
    const [cveRecord, setCVErecord] = useState([]);
    const [cveList, setCveList] = useState([]);
    
    const loadAgentInfo = () => {
        if (userState && userState.uid) {
            fetchAgents(userState.uid).then((response) => {
                if (response.ok) {
                    response.json().then((data) => {
                        // console.log('Fetched agents:', data);
                        setAgentInfo(data);
                    });
                } else {
                    console.error('agent load error!');
                }
            });        
        }
        else console.warn('User state or user UID is not available');
        
    }

    const loadTestRecord = () => {
        if (userState && userState.uid) {
            fetchTestRecord(userState.uid).then((response) => {
                if (response.ok) {
                    response.json().then((data) => {
                        console.log('Fetched test record:', data);
                        setTestRecord(data);
                    }
                );
                } else {
                    console.error('test record load error!');
                }
            });
        }
        else console.warn('User state or user UID is not available');
    }

    const loadCVERecordbyRid = (rid) => {
        if (userState && userState.uid) {
            fetchTestRecordbyId(rid).then((response) => {
                if (response.ok) {
                    response.json().then((data) => {
                        // console.log('id test record:', data);
                        setCVErecord(data);  // 상태 업데이트
                    });
                } else {
                    console.error('detailed test record load error!');
                }
            });
        } else {
            console.warn('User state or user UID is not available');
        }
    };
    
    useEffect(() => {
        if (cveRecord) {
            const tcveRecord = cveRecord.map((cve) => cve.cid);
            
            fetchCVE(tcveRecord).then((response) => {
                if (response.ok) {
                    response.json().then((data) => {
                        // console.log('cve:', data);
                        setCveList(data);
                    });
                } else {
                    console.error('cve load error!');
                }
            });
        }
    }, [cveRecord]); 

    const hadletoSubmit = (event) => {
        if (window.confirm('사용자 정보를 수정하시겠습니까?')){
            const userInfo = {
                uid: userState.uid,
                username: name,
                email: email,
            }
    
            fetchUpdateUserInfo(userInfo).then((response) => {
                if (response.ok) {
                    response.json().then((data) => {
                        console.log("updated user info data:", data);
                        window.location.reload();
                    });
                } else {
                    console.log('user info modi error!');
                }
            })
        }
        handleCancel();
    };

    const handleCancel = () => {
        setStateModi(0);
        setName(userState.username);
        setEmail(userState.email);
    }
    
    const handleUpdate = () => {
        setStateModi(1);
    }

    const handleNameChange = (event) => {
        setName(event.target.value);
    };

    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };

    const gotoAgentInfo = () => {
        navigate('/pentest/info-agent');
    }

    const showResult = (id) => {
        loadCVERecordbyRid(id);
    }

    const tableStyle = {
        padding: '10px 10px 10px 0',
    }

    useEffect(() => {
        loadAgentInfo();
        loadTestRecord();

    }, []);


    return (
        <div>
            <Typography variant='h4' sx={{ fontWeight: 'bold', mb: 5 }}> Mypage </Typography>
            <div  style={{ border: '2px solid #ddd', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding:'20px' }}>
                <Typography variant='h5' sx={{ fontWeight: 'bold', mb: 2 }}> User Info </Typography>
                <table>
                    <tbody>
                        <tr>
                            <td  style={tableStyle}><strong>Name</strong></td>
                            <td style={tableStyle}> {stateModi === 1 ? (
                                <input
                                    type="text"
                                    value={name}
                                    autoFocus
                                    onChange={handleNameChange}
                                />
                            ) : (
                                userState?.username
                            )} </td>
                        </tr>
                        <tr>
                            <td style={tableStyle}><strong>Email</strong></td>
                            <td style={tableStyle}> {stateModi === 1 ? (
                                <input
                                    type="text"
                                    value={email}
                                    onChange={handleEmailChange}
                                />
                            ) : (
                                userState?.email
                            )} </td>
                        </tr>
                    </tbody>
                </table>
                <div className='flex flex-row'>
                    <Button variant='contained' sx={{ mt: 2, }}onClick={handleUpdate}>
                        수정
                    </Button>
                    {stateModi === 1 && (
                        <div>
                            <Button variant='contained' sx={{ mt: 2, ml: 1 }} onClick={hadletoSubmit}>
                                저장
                            </Button>
                            <Button variant='contained' sx={{ mt: 2, ml: 1 }} onClick={handleCancel}>
                                취소
                            </Button>
                        </div>
                    )}                
                </div>
            </div>
            
            <div style={{ border: '2px solid #ddd', marginTop: '20px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding:'20px' }}>
                <Box display="flex" sx={{ alignItems: 'center', mb: 2 }} >
                    <Typography variant='h5' sx={{ fontWeight: 'bold', }}> Current Connected Agent </Typography>
                    <Box display="flex" sx={{ alignItems: 'center', ml: 2 }} >
                        <Typography variant='body1' sx={{ color: 'gray' }}> More Information </Typography>
                        <IconButton aria-label="clear" onClick={gotoAgentInfo} >
                            <KeyboardDoubleArrowRightIcon/>
                        </IconButton>
                    </Box>
                </Box>

                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650, }} aria-label="simple table">
                        <TableHead>
                        <TableRow>
                            <TableCell>Host Name</TableCell>
                            <TableCell>IP</TableCell>
                            <TableCell>OS</TableCell>
                        </TableRow>
                        </TableHead>
                        <TableBody>
                        {agentInfo.map((agent) => (
                            <TableRow
                                key={agent.hostname}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                <TableCell component="th" scope="row">
                                    {agent.hostname}
                                </TableCell>
                                <TableCell sx={{ width: '25%'}}>{agent?.ip}</TableCell>
                                <TableCell sx={{ width: '25%'}}>
                                    {agent.os}
                                </TableCell>
                            </TableRow>
                        ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
            <div style={{ border: '2px solid #ddd', marginTop: '20px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding:'20px' }}>
                <Typography variant='h5' sx={{ fontWeight: 'bold', mb: 2 }}> Test Record </Typography>
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }} aria-label="simple table">
                        <TableHead>
                        <TableRow>
                            <TableCell>Test Name</TableCell>
                            <TableCell>Test Date</TableCell>
                            <TableCell>Result</TableCell>
                        </TableRow>
                        </TableHead>
                        <TableBody>
                        {testRecord.sort((b, a) => new Date(b.date) - new Date(a.date)).map((record) => (
                            <TableRow
                                key={record.name}
                                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                <TableCell component="th" scope="row">
                                    {record.name}
                                </TableCell>
                                <TableCell sx={{ width: '25%'}}>{record.date.split('T')[0]}</TableCell>
                                <TableCell
                                    onClick={()=>showResult(record.id)} 
                                    style={{cursor: 'pointer', width: '25%'}} 
                                    onMouseEnter={(e) => { e.target.style.color = 'blue'; e.target.style.textDecoration = 'underline'; }} 
                                    onMouseLeave={(e) => { e.target.style.color = 'inherit'; e.target.style.textDecoration = 'none'; }}>
                                    확인 

                                </TableCell>

                            </TableRow>
                        ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                <div style={{ border: '2px solid #ddd', marginTop: '20px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', padding:'20px' }}>
                    <Typography variant='h5' sx={{ fontWeight: 'bold', mb: 2 }}> CVE List </Typography>
                    <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 650 }} aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell> CVE ID </TableCell>
                                    <TableCell> Used Technique </TableCell>
                                    <TableCell> Mitigation </TableCell>

                                </TableRow>
                            </TableHead>
                            {cveList.length > 0 ? (
                                <TableBody>    
                                    {cveList.map((cve) => (
                                        <TableRow
                                            key={cve.cve_id}
                                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                        >   
                                            <TableCell>
                                                <Tooltip title={
                                                    <Box sx={{ p: 1 }}>
                                                        <Typography variant='subtitle1' sx={{ fontWeight: 'bold' }}>
                                                            {cve.cve_title}
                                                        </Typography>
                                                        <Typography variant='body1'>
                                                            {cve.cve_description}
                                                        </Typography>
        
                                                    </Box>
                                                    } 
                                                arrow placement='right'>
                                                    {cve.cve_id}
                                                </Tooltip>
                                            </TableCell>
                                            <TableCell sx={{ width: '25%', }}>
                                                <TableRow>
                                                    {cve.cve_tid.map((tid) => (
                                                        <TableRow>{tid}</TableRow>
                                                    ))}
                                                </TableRow>
                                            </TableCell>
                                            <TableCell sx={{ width: '25%', }}>{cve.cve_mitigation}</TableCell>

                                        </TableRow>
                                        
                                    ))}
                                </TableBody>
                            ): (
                                <TableBody>
                                    <TableRow>
                                        <TableCell variant='h6' colSpan={3} sx={{ textAlign: 'center', fontWeight: 'bold' }}> No detected CVE List </TableCell>
                                    </TableRow>
                                </TableBody>
                            )}
                        </Table>
                    </TableContainer>
                </div>
            </div>   
        </div>
    )
}

export default Mypage;
