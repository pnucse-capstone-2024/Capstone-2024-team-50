import React, { useContext } from 'react';
import { Outlet, Navigate } from 'react-router-dom';

import PropTypes from 'prop-types';

import { CircularProgress } from '@mui/material';

import { UserContext } from '../../core/user';

const ProtectedRoute = ({ children, require_admin }) => {
    const { userState } = useContext(UserContext);

    if (userState?.isLoading) {
        return <CircularProgress />;
    }

    if (!userState) {
        return <Navigate to="/signin" />;
    }

    if (require_admin && !userState.is_admin) {
        return <Navigate to="/pentest" />;
    }

    return children ? <React.Fragment>{children}</React.Fragment> : <Outlet />;
};

ProtectedRoute.propTypes = {
    children: PropTypes.node,
};

export default ProtectedRoute;
