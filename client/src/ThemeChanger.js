import React from 'react';


import { themeIcons } from './icons';
import {sleep} from './apiUtils'

import './styles/ThemeChangerBlinder.css';


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

let blinderSwitching = false;
const root = document.querySelector(':root');

async function changeTheme(darkTheme, setBlinderHidden, setDarkTheme){

    if (blinderSwitching) return;
    blinderSwitching = true;

    setBlinderHidden(false);
    await sleep(500);

    // Change theme
    const theme = darkTheme ? themes.light : themes.dark;

    root.style.setProperty('--main-color', theme.main);
    root.style.setProperty('--support-color', theme.support);
    root.style.setProperty('--outline-color', theme.outline);
    root.style.setProperty('--background-color', theme.background);

    setDarkTheme(!darkTheme);
    await sleep(500);

    setBlinderHidden(true);
    blinderSwitching = false;
    // setIsDarkTheme(!isDarkTheme);

    // ANIMATION TO BE DONE HERE!
}


export function ThemeChanger({darkTheme, setDarkTheme}) {

    const [blinderHidden, setBlinderHidden] = React.useState(true);

    return (
    <>
        <div className={`theme-changer-blinder ${blinderHidden ? "hidden": ""}`}>

            {
                darkTheme ?
                <>
                    <themeIcons.SmallLogo.dark className="blinder-icon"/>
                </>
                :
                <>
                    <themeIcons.SmallLogo.light className="blinder-icon"/>
                </>
            }
            <h1 className="title">Changing Theme...</h1>
            
        </div>
        <span className="change-theme-span" onClick={() => changeTheme(darkTheme, setBlinderHidden, setDarkTheme)}>
            {
                darkTheme ?
                <>
                    <themeIcons.SmallLogo.light className="change-theme-icon"/><span>Light Theme</span>
                </>
                :
                <>
                    <themeIcons.SmallLogo.dark className="change-theme-icon"/><span>Dark Theme</span>
                </>
            }
        </span>
    </>
    );
  }