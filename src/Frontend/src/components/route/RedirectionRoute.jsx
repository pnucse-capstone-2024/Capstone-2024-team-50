import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';

import PropTypes from 'prop-types';

import { CircularProgress } from '@mui/material';

import { UserContext } from '../../core/user';

const RedirectionRoute = () => {
    const { userState } = useContext(UserContext);

    if (userState?.isLoading) {
        return <CircularProgress />;
    }

    if (!userState) {
        return <Navigate to="/signin" />;
    }
    else {
        return <Navigate to="/dashboard" />;
    }
};

RedirectionRoute.propTypes = {
    children: PropTypes.node,
};

export default RedirectionRoute;
