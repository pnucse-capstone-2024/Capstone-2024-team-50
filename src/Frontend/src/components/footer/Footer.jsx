import React, { useState, useEffect } from 'react';

import Fab from '@mui/material/Fab';
import ArrowUpwardOutlinedIcon from '@mui/icons-material/ArrowUpwardOutlined';

const Footer = () => {
    const [BtnStatus, setBtnStatus] = useState(false); // 버튼 상태

    const handleFollow = () => {
        if ((window.scrollY || window.pageYOffset) > 300) {
            setBtnStatus(true);
        } else {
            setBtnStatus(false);
        }
    };
    const handleTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth',
        });
    };
    useEffect(() => {
        const watch = () => {
            window.addEventListener('scroll', handleFollow);
        };
        watch();
        return () => {
            window.removeEventListener('scroll', handleFollow);
        };
    });
    return (
        <div
            className="flex justify-center w-full items-center space-y-2 pt-2 border border-gray-400 bg-white"
            style={{boxShadow: '0px -2px 2px -2px #333'}}
        >
            <div className="flex 2xl:w-10/12 mb-5 w-full items-center">
                <div className="flex flex-col text-xs">
                    <p>
                        Copyright ⓒ 부산대학교 2024 전기 졸업과제 팀 417호. All
                        Rights Reserved.
                    </p>
                </div>

                {BtnStatus && (
                    <Fab
                        className="!fixed bottom-5 right-5 2xl:right-[13.5%] !bg-primary !hover:bg-secondary !text-white"
                        onClick={handleTop}
                    >
                        <ArrowUpwardOutlinedIcon />
                    </Fab>
                )}
            </div>
        </div>
    );
};

export default Footer;
