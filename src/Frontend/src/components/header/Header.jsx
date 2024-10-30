import React, { useContext } from 'react';

import { UserContext } from '../../core/user';

import NoAuthenticatedHeader from './NoAuthenticatedHeader';
import AuthenticatedHeader from './AuthenticatedHeader';

const Header = () => {
    const { userState } = useContext(UserContext);
  
    if (!userState || userState.isLoading) {
        return <NoAuthenticatedHeader />;
    }
    else {
        return <AuthenticatedHeader />;
    }
};

export default Header;
