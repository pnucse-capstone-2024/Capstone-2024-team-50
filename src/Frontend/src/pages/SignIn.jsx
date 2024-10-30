import React, { useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { Divider, InputAdornment } from '@mui/material';
import PersonOutlineIcon from '@mui/icons-material/PersonOutline';
import PasswordIcon from '@mui/icons-material/Password';

import { AuthContext } from '../core/auth';

import { fetchSignIn } from '../services/AuthServices';
import { UserContext } from '../core/user';


const SignIn = () => {
    const navigate = useNavigate();

    const { setAuthState } = useContext(AuthContext);
    const { setUserState } = useContext(UserContext);

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const [usernameError, setUsernameError] = useState('');
    const [passwordError, setPasswordError] = useState('');

    const onClickSignIn = () => {
        if (validate()) {
            fetchSignIn(username, password)
                .then((response) => {
                    if (response.ok) {
                        setUserState({ isLoading: true });

                        setAuthState({
                            isAuthenticated: true,
                            isLoading: false,
                        });

                        setPassword('');
                        navigate('/');
                    } else if (response.status === 401) {
                        alert('Invalid username or password.');
                    } else {
                        alert('Unknown error. Please try again later.');
                    }
                })
                .catch((error) => {
                    alert('Network error. Please try again later.');
                    console.log(error);
                });
        }
    };

    const validate = () => {
        const isValidUsername = validateUsername();
        const isValidPassword = validatePassword();

        return isValidUsername && isValidPassword;
    };

    const validateUsername = () => {
        if (username.length === 0) {
            setUsernameError('Please enter your ID.');
            return false;
        }
        setUsernameError('');
        return true;
    };

    const validatePassword = () => {
        if (password.length === 0) {
            setPasswordError('Please enter your password.');
            return false;
        }
        setPasswordError('');
        return true;
    };

    return (
        <div className="flex flex-row justify-center items-center w-full space-x-32">
            <div className="flex flex-col items-center">
                <Container component="main" maxWidth="xs">
                    <CssBaseline />
                    <Box
                        sx={{
                            marginTop: 8,
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                        }}
                    >
                        <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                            <LockOutlinedIcon />
                        </Avatar>
                        <Typography component="h1" variant="h5">
                            Sign in
                        </Typography>
                        <Box sx={{ mt: 1 }}>
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                label="ID"
                                name="email"
                                autoComplete="email"
                                InputProps={{
                                    startAdornment: (
                                        <InputAdornment position="start">
                                            <PersonOutlineIcon />
                                        </InputAdornment>
                                    ),
                                }}
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                error={usernameError.length > 0}
                                helperText={usernameError}
                                autoFocus
                            />
                            <TextField
                                margin="normal"
                                required
                                fullWidth
                                label="Password"
                                type="password"
                                id="password"
                                InputProps={{
                                    startAdornment: (
                                        <InputAdornment position="start">
                                            <PasswordIcon />
                                        </InputAdornment>
                                    ),
                                }}
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                error={passwordError.length > 0}
                                helperText={passwordError}
                            />
                            <FormControlLabel
                                control={
                                    <Checkbox
                                        value="remember"
                                        color="primary"
                                    />
                                }
                                label="Remember me"
                            />
                            <Button
                                type="submit"
                                fullWidth
                                variant="contained"
                                sx={{ mt: 3, mb: 2 }}
                                onClick={onClickSignIn}
                            >
                                Sign In
                            </Button>
                            <Grid container>
                                <Grid item xs>
                                    <Button
                                        className="ml-10"
                                        onClick={() => navigate('/signup/')}
                                        sx={{textDecoration:'underline'}}
                                    >
                                        {"Sign Up"}
                                    </Button>
                                </Grid>
                                <Grid item>
                                <Button
                                        className="ml-10"
                                        sx={{textDecoration:'underline'}}
                                    >
                                        {"Forgot password?"}
                                    </Button>
                                </Grid>
                            </Grid>
                            
                        </Box>
                    </Box>
                </Container>
            </div>
        </div>
    );
};

export default SignIn;
