import React from 'react';
import { useRouteError } from 'react-router-dom';

import { Typography } from '@mui/material';

const ErrorPage = () => {
    const error = useRouteError();

    return (
        <div id="error-page" className="flex h-full justify-center">
            <div className="flex h-3/4 w-3/12 flex-col items-center justify-center space-y8 p-4">
                <div className="flex flex-col w-full h-3/5 items-center space-y-4 bg-white bg-opacity-90">
                    <Typography class="text-7xl text-slate-600 font-bold tracking-wider p-10 italic">
                        Oops!
                    </Typography>
                    <p>Sorry, an unexpected error has occured.</p>
                    <p>
                        <i>{error.status + ' ' + error.statusText}</i>
                        <i>{error.data?.message}</i>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default ErrorPage;
