import React, { createContext, useEffect, useState } from 'react';

import PropTypes from 'prop-types';

import { fetchRefresh } from '../services/AuthServices';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
    const [authState, setAuthState] = useState({
        isAuthenticated: false,
        isLoading: true,
    });

    useEffect(() => {
        fetchRefresh()
            .then((response) => {
                if (response.ok) {
                    setAuthState({
                        isAuthenticated: true,
                        isLoading: false,
                    });
                } else {
                    setAuthState({
                        isAuthenticated: false,
                        isLoading: false,
                    });
                }
            })
            .catch((error) => {
                console.log(error);
            });
        console.log('authState - AuthProvider', authState);
    }, []);

    return (
        <AuthContext.Provider value={{ authState, setAuthState }}>
            {children}
        </AuthContext.Provider>
    );
};

AuthProvider.propTypes = {
    children: PropTypes.node.isRequired,
};

export { AuthContext, AuthProvider };
