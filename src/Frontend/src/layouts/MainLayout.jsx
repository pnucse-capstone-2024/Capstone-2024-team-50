import React, { useContext } from 'react';
import { Outlet, useLocation } from 'react-router-dom';

import { UserContext } from '../core/user';

import Header from '../components/header/Header';
import Footer from '../components/footer/Footer';

const MainLayout = () => {
    const { userState } = useContext(UserContext);
    const location = useLocation();

    let padding = 'p-16';

    if (location.pathname.includes('pentest')) {
        padding = 'p-0';
    } else {
        padding = 'p-16';
    }

    if (!userState || userState.isLoading) {
        return (
            <div className="flex flex-col relative">
                <div className="flex w-full h-full min-h-screen p-2">
                    <Outlet />
                </div>
            </div>
        );
    } else {
        return (
            <>
                <div className="flex flex-col min-h-screen relative">
                    <Header />
                    <div className={`flex-grow w-full ${padding}`}>
                        <Outlet />
                    </div>
                </div>
            </>
        );
    }
};

export default MainLayout;
