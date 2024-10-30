import React from "react";
import { createBrowserRouter } from "react-router-dom";

import RedirectionRoute from '../components/route/RedirectionRoute';
import ProtectedRoute from '../components/route/ProtectedRoute';

// layouts
import MainLayout from "../layouts/MainLayout";
import ErrorLayout from "../layouts/ErrorLayout";
import PentestLayout from "../layouts/PentestLayout";

// pages
import Main from "../pages/Main";
import SignIn from "../pages/SignIn";
import Agent from "../pages/pentest/Agent";
import Agentless from "../pages/pentest/Agentless";
import Dashboard from "../pages/Dashboard";
import Information from "../pages/Information";
import Mypage from "../pages/Mypage";
import AgentInfo from "../pages/pentest/AgentInfo";
import Result from "../pages/pentest/Result";

const Router = createBrowserRouter([{
    path: '/',
    element: <MainLayout />,
    errorElement: <ErrorLayout />,
    children: [
        {
            index: true,
            element: <RedirectionRoute />,
        },
        {
            path: 'signin',
            element: <SignIn />,
        },
        {
            path: 'dashboard',
            element: <Dashboard />,
        },
        {
            path: 'information',
            element: <Information />,
        },
        {
            path: 'mypage',
            element: <Mypage />,
        },
        {
            path: 'pentest',
            element: (
                <PentestLayout />
            ),
            children: [
                {
                    path: 'agent',
                    element: <Agent />,
                },
                {
                    path: 'agentless',
                    element: <Agentless />,
                },
                {
                    path: 'info-agent',
                    element: <AgentInfo />,
                },
                {
                    path: 'result',
                    element: <Result />,
                }
            ],
        }
    ]
}]);

export default Router;
