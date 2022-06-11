// Logo
import {ReactComponent as SmallLogo} from './assets/logo/small-logo.svg';
import {ReactComponent as MediumLogo} from './assets/logo/medium-logo.svg';
import {ReactComponent as MediumLogoWhite} from './assets/logo/medium-logo-white.svg';
import {ReactComponent as BigLogo} from './assets/logo/big-logo.svg';

// Themed Logo
import {ReactComponent as SmallLogoLight} from './assets/logo/small-logo-light-theme.svg';
import {ReactComponent as SmallLogoDark} from './assets/logo/small-logo-dark-theme.svg';
import {ReactComponent as MediumLogoLight} from './assets/logo/medium-logo-light-theme.svg';
import {ReactComponent as MediumLogoDark} from './assets/logo/medium-logo-dark-theme.svg';
import {ReactComponent as BigLogoLight} from './assets/logo/big-logo-light-theme.svg';
import {ReactComponent as BigLogoDark} from './assets/logo/big-logo-dark-theme.svg';

// Themed Illustrations
import {ReactComponent as ProgramInstructionsLight} from './assets/illustrations/program-instructions-light.svg';
import {ReactComponent as ProgramInstructionsDark} from './assets/illustrations/program-instructions-dark.svg';
import {ReactComponent as RobotUtilsLight} from './assets/illustrations/robot-utils-light.svg';
import {ReactComponent as RobotUtilsDark} from './assets/illustrations/robot-utils-dark.svg';
import {ReactComponent as ManualModeLight} from './assets/illustrations/manual-mode-light.svg';
import {ReactComponent as ManualModeDark} from './assets/illustrations/manual-mode-dark.svg';
// Icons
import {AiOutlineMenuFold,  AiOutlineMenuUnfold} from 'react-icons/ai';
import {BiErrorAlt} from 'react-icons/bi';
import {FaCircle, FaRegCircle, FaRegQuestionCircle} from 'react-icons/fa';


export const themeIcons = {
    SmallLogo : {
        light: SmallLogoLight,
        dark: SmallLogoDark
    },
    MediumLogo : {
        light: MediumLogoLight,
        dark: MediumLogoDark
    },
    BigLogo : {
        light: BigLogoLight,
        dark: BigLogoDark
    },
    ProgramInstructions: {
        light: ProgramInstructionsLight,
        dark: ProgramInstructionsDark
    },
    RobotUtils: {
        light: RobotUtilsLight,
        dark: RobotUtilsDark
    },
    ManualMode: {
        light: ManualModeLight,
        dark: ManualModeDark
    }
}

export function getThemedIcon(iconName, darkTheme){
    if (darkTheme) return themeIcons[iconName].dark;
    return themeIcons[iconName].light;
}


export const icons = {
    SmallLogo : SmallLogo,
    MediumLogo : MediumLogo,
    MediumLogoWhite: MediumLogoWhite,
    BigLogo : BigLogo,

    HideMenu: AiOutlineMenuFold,
    ShowMenu: AiOutlineMenuUnfold,

    Error: BiErrorAlt,

    BlackTile: FaCircle,
    WhiteTile: FaRegCircle,
    UndefinedTile: FaRegQuestionCircle,
}
