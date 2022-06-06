import { darkTheme } from './ThemeChanger';

// Logo
import {ReactComponent as smallLogoLight} from './assets/logo/small-logo-light-theme.svg';
import {ReactComponent as smallLogoDark} from './assets/logo/small-logo-dark-theme.svg';
import {ReactComponent as mediumLogoLight} from './assets/logo/medium-logo-light-theme.svg';
import {ReactComponent as mediumLogoDark} from './assets/logo/medium-logo-dark-theme.svg';
import {ReactComponent as bigLogoLight} from './assets/logo/big-logo-light-theme.svg';
import {ReactComponent as bigLogoDark} from './assets/logo/big-logo-dark-theme.svg';


// Icons
import { AiOutlineMenuFold,  AiOutlineMenuUnfold} from 'react-icons/ai';
import {ReactComponent as smallLogo} from './assets/logo/small-logo.svg';
import {ReactComponent as mediumLogo} from './assets/logo/medium-logo.svg';
import {ReactComponent as mediumLogoWhite} from './assets/logo/medium-logo-white.svg';
import {ReactComponent as bigLogo} from './assets/logo/big-logo.svg';

export const themeIcons = {
    smallLogo : {
        light: smallLogoLight,
        dark: smallLogoDark
    },
    mediumLogo : {
        light: mediumLogoLight,
        dark: mediumLogoDark
    },
    bigLogo : {
        light: bigLogoLight,
        dark: bigLogoDark
    }
}

export function getThemedIcon(iconName){
    if (darkTheme) return themeIcons[iconName].dark;
    return themeIcons[iconName].light;
}


export const icons = {
    smallLogo : smallLogo,
    mediumLogo : mediumLogo,
    mediumLogoWhite: mediumLogoWhite,
    bigLogo : bigLogo,
    hideMenu: AiOutlineMenuFold,
    showMenu: AiOutlineMenuUnfold
}
