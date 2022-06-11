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
import {AiOutlineMenuFold,  AiOutlineMenuUnfold, AiOutlineEllipsis, AiFillRobot} from 'react-icons/ai';
import {BiErrorAlt, BiHide} from 'react-icons/bi';
import {FaCircle, FaRegCircle, FaRegQuestionCircle} from 'react-icons/fa';
import {BsCloudArrowUp, BsFillCloudCheckFill, BsCloudy, BsQuestion} from 'react-icons/bs';
import {GiRobotGrab} from 'react-icons/gi';
import {GrManual} from 'react-icons/gr';


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

    ShowMore: AiOutlineEllipsis,
    Hide: BiHide,
    Unknown: BsQuestion
}


export const logIcons = {
    "new-instructions": BsCloudArrowUp,
    "instructions-finished": BsFillCloudCheckFill,
    "turned-on": BsCloudy,
    "white-detected": FaRegCircle,
    "black-detected": FaCircle,
    "undefined-detected": FaRegQuestionCircle,
    "pushed": GiRobotGrab,
    "error": BiErrorAlt,
    "switched-to-instruction-mode": AiFillRobot,
    "switched-to-manual-mode": GrManual,

}

export function getLogIcon(iconName){
    if (logIcons.hasOwnProperty(iconName)) return logIcons[iconName];
    return icons.Unknown;
}
