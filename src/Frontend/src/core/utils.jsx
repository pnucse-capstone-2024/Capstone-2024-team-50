export const passwordValidator = (password) => {
    if (!password || password.length <= 0) return 'Please enter a password.';
    else if (password.length < 8)
        return 'Password must be at least 8 characters long.';
    return '';
};

export const confirmPasswordValidator = (newPassword, confirmPassword) => {
    if (!confirmPassword || confirmPassword.length <= 0)
        return 'Please enter a confirm password.';
    if (newPassword !== confirmPassword) return 'Mismatched password.';
    return '';
};