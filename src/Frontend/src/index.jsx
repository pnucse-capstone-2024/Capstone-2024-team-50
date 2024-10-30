import React from 'react';
import ReactDOM from 'react-dom/client';
import { RouterProvider } from 'react-router-dom';
import './index.css';

import { ThemeProvider } from '@mui/material';
import { AuthProvider } from './core/auth';
import { UserProvider } from './core/user';

import theme from './theme';
import router from './routes/Router';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <ThemeProvider theme={theme}>
        <AuthProvider>
            <UserProvider>
                <RouterProvider router={router} />
            </UserProvider>
        </AuthProvider>
    </ThemeProvider>
);
