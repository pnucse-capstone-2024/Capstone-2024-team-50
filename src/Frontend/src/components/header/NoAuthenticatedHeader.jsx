import React from 'react';
import { useNavigate } from 'react-router-dom';

import {
    AppBar,
    Toolbar,
    Button,
} from '@mui/material';

import { useTheme } from '@mui/material/styles';

import HeaderIcon from '../icon/HeaderIcon';

const NoAuthenticatedHeader = () => {
    const navigate = useNavigate();
    const theme = useTheme();

    const onClickSignIn = () => {
        navigate('/SignIn');
    };

    return (
    <AppBar
            position="static"
            elevation={1}
            style={{ background: '#ffffff' }}
        >
            <Toolbar>
                <HeaderIcon theme={theme} onClickLogo={() => navigate('/')} />
                {/* Spacer div */}
                <div style={{ flexGrow: 1 }}></div>

                <Button
                    type="submit"
                    variant="contained"
                    sx={{ mt: 1, mb: 1 }}
                    onClick={onClickSignIn}
                >
                    Sign In
                </Button>
            </Toolbar>
        </AppBar>
    );
};

export default NoAuthenticatedHeader;
