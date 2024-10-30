import React, { useContext, useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import {
    AppBar,
    Toolbar,
    Divider,
    IconButton,
    Typography,
    Button,
    Menu,
    MenuItem,
    Box,
    Avatar,
    styled,
} from '@mui/material';
import PersonOutlineIcon from '@mui/icons-material/PersonOutline';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import { useTheme } from '@mui/material/styles';
import { AuthContext } from '../../core/auth';
import { UserContext } from '../../core/user';
import { fetchSignOut } from '../../services/AuthServices';

import csrc_logo from '../../static/images/csrc_logo_light.png';

// 스타일링된 AppBar 및 Toolbar
const StyledAppBar = styled(AppBar)(({ theme }) => ({
    backgroundColor: '#3A74CD',
    boxShadow: theme.shadows[4],
}));

const StyledToolbar = styled(Toolbar)(({ theme }) => ({
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: theme.spacing(1, 3),
}));

const NavButton = styled(Button)(({ theme }) => ({
    color: theme.palette.common.white,
    '&:hover': {
        backgroundColor: theme.palette.primary.dark,
    },
}));

const UserMenuAvatar = styled(Avatar)(({ theme }) => ({
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.common.white,
    cursor: 'pointer',
}));

const Header = () => {
    const navigate = useNavigate();
    const theme = useTheme();
    const { setAuthState } = useContext(AuthContext);
    const { userState } = useContext(UserContext);
    const [userMenuAnchorEl, setUserMenuAnchorEl] = useState(null);
    const userMenuOpen = Boolean(userMenuAnchorEl);
    const [isLogoClicked, setIsLogoClicked] = useState(false);
    const [isUserInfoClicked, setIsUserInfoClicked] = useState(false);
    const [isLogoutClicked, setIsLogoutClicked] = useState(false);

    const onClickSignOut = () => {
        fetchSignOut().finally(() => {
            setAuthState({
                isAuthenticated: false,
                isLoading: false,
            });
            onCloseUserMenu();
            setIsLogoutClicked(true);
        });
    };

    const onCloseUserMenu = () => {
        setUserMenuAnchorEl(null);
    };

    const onClickUserInfo = () => {
        setIsUserInfoClicked(true);
    };

    useEffect(() => {
        if (isLogoClicked) {
            navigate('/Project');
            setIsLogoClicked(false);
        }
    }, [isLogoClicked]);

    useEffect(() => {
        if (isUserInfoClicked) {
//            navigate('/myPages/MyInformation');
            navigate('/mypage');
            setIsUserInfoClicked(false);
        }
    }, [isUserInfoClicked]);

    useEffect(() => {
        if (isLogoutClicked) {
            navigate('/');
            setIsLogoutClicked(false);
        }
    }, [isLogoutClicked]);

    const renderUserMenu = () => (
        <Menu
            id="user-menu"
            anchorEl={userMenuAnchorEl}
            open={userMenuOpen}
            onClose={onCloseUserMenu}
            MenuListProps={{ 'aria-labelledby': 'user-button' }}
            transformOrigin={{
                horizontal: 'right',
                vertical: 'top',
            }}
            anchorOrigin={{
                horizontal: 'right',
                vertical: 'bottom',
            }}
        >
            <MenuItem onClick={onClickUserInfo}>
                <Box display="flex" flexDirection="column" alignItems="center" p={2}>
                    {userState.logo && (
                        <Box
                            component="img"
                            src={userState.logo}
                            alt="User Logo"
                            sx={{ width: 60, height: 60, borderRadius: '50%', mb: 1 }}
                        />
                    )}
                    <Box display="flex" alignItems="center">
                        <PersonOutlineIcon fontSize="large" sx={{ mr: 1 }} />
                        <Box textAlign="left">
                            <Typography variant="body1">{userState.username}</Typography>
                            <Typography variant="body2" color="textSecondary">
                                {userState.company_name}
                            </Typography>
                        </Box>
                        <ArrowForwardIosIcon fontSize="small" sx={{ ml: 'auto' }} />
                    </Box>
                </Box>
            </MenuItem>
            <MenuItem>
                <Button
                    fullWidth
                    variant="contained"
                    onClick={onClickSignOut}
                    color="error"
                >
                    Sign Out
                </Button>
            </MenuItem>
        </Menu>
    );

    return (
        <StyledAppBar position="static">
            <StyledToolbar>
                <Link to="/" style={{ textDecoration: 'none' }}>
                    <Box display="flex" sx={{alignItems:"center", }} >
                       {/* <img src={csrc_logo} style={{width: '250px', }}/> */}
                         <Typography
                            variant="h5"
                            sx={{ color: 'white', fontWeight: 'bold', }}
                        >
                            PNU-417
                        </Typography> 
                    </Box>
                </Link>

                <Box display="flex" alignItems="center">
                    <NavButton onClick={() => navigate('/')} >홈</NavButton>
                    <Divider orientation="vertical" variant="middle" flexItem sx={{ backgroundColor: 'white', mx: 1 }} />
                    <NavButton onClick={() => navigate('/pentest/info-agent')}>침투 테스트</NavButton>
                    <Divider orientation="vertical" variant="middle" flexItem sx={{ backgroundColor: 'white', mx: 1 }} />
                    <NavButton onClick={() => navigate('/information')}>이용 방법</NavButton>
                    <Divider orientation="vertical" variant="middle" flexItem sx={{ backgroundColor: 'white', mx: 1 }} />
                    <NavButton onClick={() => navigate('/mypage')}>마이페이지</NavButton>
                    <Divider orientation="vertical" variant="middle" flexItem sx={{ backgroundColor: 'white', mx: 1 }} />
                    <NavButton onClick={onClickSignOut}>로그아웃</NavButton>
                </Box>

                <UserMenuAvatar
                    onClick={(e) => setUserMenuAnchorEl(e.currentTarget)}
                >
                    {userState.username.charAt(0)}
                </UserMenuAvatar>
            </StyledToolbar>
            {renderUserMenu()}
        </StyledAppBar>
    );
};

export default Header;
