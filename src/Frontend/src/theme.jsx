import { createTheme } from '@mui/material/styles';

const colors = {
    blue: {
        100: '#cce7f4',
        200: '#99cfe9',
        300: '#66b8dd',
        400: '#33a0d2',
        500: '#0088c7',
        600: '#006d9f',
        700: '#005277',
        800: '#003650',
        900: '#001b28',
    },
    gery: {
        100: '#d0d1d5',
        200: '#a1a4ab',
        300: '#727681',
        400: '#434957',
        500: '#141b2d',
        600: '#101624',
        700: '#0c101b',
        800: '#080b12',
        900: '#040509',
    },
    green: {
        100: '#dbf5ee',
        200: '#b7ebde',
        300: '#94e2cd',
        400: '#70d8bd',
        500: '#16A34A',
        600: '#3da58a',
        700: '#2e7c67',
        800: '#1e5245',
        900: '#0f2922',
    },
    indigo: {
        100: '#e1e2fe',
        200: '#c3c6fd',
        300: '#a4a9fc',
        400: '#868dfb',
        500: '#6870fa',
        600: '#535ac8',
        700: '#3e4396',
        800: '#2a2d64',
        900: '#151632',
    },
    orange: {
        100: '#fdecce',
        200: '#fbd89d',
        300: '#f9c56d',
        400: '#f7b13c',
        500: '#f59e0b',
        600: '#c47e09',
        700: '#935f07',
        800: '#623f04',
        900: '#312002',
    },
    red: {
        100: '#fcdada',
        200: '#f9b4b4',
        300: '#f58f8f',
        400: '#f26969',
        500: '#ef4444',
        600: '#bf3636',
        700: '#8f2929',
        800: '#601b1b',
        900: '#300e0e',
    },
    white: {
        100: '#ffffff',
    },
    black: {
        100: '#000000',
    }
};


// A custom theme for this app
const theme = createTheme({
    palette: {
        primary: {
            // main: '#3eb489',
            main: '#3A74CD',
            light: '#f1f3fb',
        },
        secondary: {
            main: '#0d65a2',
            dark: '#083554',
            light: '#b4ddfa',
        },
        neutral: {
            dark: colors.gery[700],
            main: colors.gery[500],
            light: colors.gery[300],
        },
        error: {
            main: colors.red[500],
        },
        warning: {
            main: colors.orange[500],
        },
        info: {
            main: '#556cd6',
        },
        success: {
            main: colors.green[500],
        },
        background: {
            default: colors.white[100],
            paper: colors.white[100],
        },
        white: {
            default: colors.white[100],
        },
        black: {
            main: colors.black[100],
        }
    },
    typography: {
        fontFamily: ['Roboto', 'sans-serif'].join(','),
        fontWeightLight: 300,
        fontWeightRegular: 400,
        fontWeightMedium: 500,
        fontWeightBold: 700,
    },
});

export default theme;
