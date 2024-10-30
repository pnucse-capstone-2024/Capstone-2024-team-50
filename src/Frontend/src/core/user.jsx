import React, { createContext, useContext, useEffect, useState } from 'react';

import PropTypes from 'prop-types';

import { AuthContext } from './auth';
import { fetchMe } from '../services/UserServices';

const UserContext = createContext();

const UserProvider = ({ children }) => {
    const { authState, setAuthState } = useContext(AuthContext);

    const [userState, setUserState] = useState({ isLoading: true });

    useEffect(() => {
        if (authState.isAuthenticated && !authState.isLoading) {
            fetchMe().then(async (response) => {
                const data = await response.json();

                if (response.ok) {
                    setUserState({
                        ...data,
                    });
                } else if (response.status === 401) {
                    setAuthState({
                        isAuthenticated: false,
                        isLoading: false,
                    });
                }
            });
        } else if (!authState.isAuthenticated && !authState.isLoading) {
            if (authState.isAuthenticated) {
                setAuthState({
                    isAuthenticated: false,
                    isLoading: false,
                });
            }
            setUserState(null);
        }

        console.log('authState - UserProvider', authState);
    }, [authState, setAuthState]);

    return (
        <UserContext.Provider value={{ userState, setUserState }}>
            {children}
        </UserContext.Provider>
    );
};

UserProvider.propTypes = {
    children: PropTypes.node.isRequired,
};

export { UserContext, UserProvider };
