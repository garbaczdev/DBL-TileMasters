import React from 'react';


import { themeIcons } from './icons';


const themes = {
    dark: {
        main: '#493662',
        support: '#EEEEEE',
        outline: '#BB96FC',
        background: '#1F1B24'
    },
    light: {
        main: '#222831',
        support: '#393E46',
        outline: '#00ADB5',
        background: '#EEEEEE'
    }
}


export function ThemeChanger(props) {

    const root = document.querySelector(':root');

    function changeTheme(){
        const theme = props.darkTheme ? themes.light : themes.dark;

        root.style.setProperty('--main-color', theme.main);
        root.style.setProperty('--support-color', theme.support);
        root.style.setProperty('--outline-color', theme.outline);
        root.style.setProperty('--background-color', theme.background);

        props.setDarkTheme(!props.darkTheme);
        // setIsDarkTheme(!isDarkTheme);

        // ANIMATION TO BE DONE HERE!
    }

    return (
        <span className="change-theme-span" onClick={changeTheme}>
            {
                props.darkTheme ?
                <>
                    <themeIcons.SmallLogo.light className="change-theme-icon"/><span>Light Theme</span>
                </>
                :
                <>
                    <themeIcons.SmallLogo.dark className="change-theme-icon"/><span>Dark Theme</span>
                </>
            }
        </span>
    );
  }