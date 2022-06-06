import React from 'react';


import { themeIcons } from './icons';


const themes = {
    dark: {
        main: '#493662',
        support: '#FFFFFF',
        outline: '#BB96FC',
        background: '#1F1B24'
    },
    light: {
        main: '#222831',
        support: '#393E46',
        outline: '#51AAFD',
        background: '#FFFFFF'
    }
}


export let darkTheme = true


export function ThemeChanger() {

    // true - dark theme; false - light theme
    const [isDarkTheme, setIsDarkTheme] = React.useState(true);

    const root = document.querySelector(':root');

    function changeTheme(){
        const theme = isDarkTheme ? themes.light : themes.dark;

        root.style.setProperty('--main-color', theme.main);
        root.style.setProperty('--support-color', theme.support);
        root.style.setProperty('--outline-color', theme.outline);
        root.style.setProperty('--background-color', theme.background);

        setIsDarkTheme(!isDarkTheme);

        // ANIMATION TO BE DONE HERE!
    }

    darkTheme = isDarkTheme;

    return (
        <span className="change-theme-span" onClick={changeTheme}>
            {
                isDarkTheme ?
                <>
                    <themeIcons.smallLogo.light className="change-theme-icon"/><span>Light Theme</span>
                </>
                :
                <>
                    <themeIcons.smallLogo.dark className="change-theme-icon"/><span>Dark Theme</span>
                </>
            }
        </span>
    );
  }