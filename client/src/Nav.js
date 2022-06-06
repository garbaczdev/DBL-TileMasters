import React from 'react';

import {Link} from "react-router-dom";

import {ThemeChanger} from './ThemeChanger'
import {icons, getThemedIcon} from './icons'

import './styles/Nav.css';


const subpages = [
    {
        url: '/',
        title: "Home"
    },
    {
        url: '/program-instructions',
        title: "Program Instructions"
    },
    {
        url: '/robot-utils',
        title: "Robot Utils"
    },
    {
        url: '/manual-mode',
        title: "Manual Mode"
    },
    {
        url: '/logs',
        title: "Logs"
    },
]


function Nav() {

    const [hidden, setHidden] = React.useState(false);

    function changeMenuShowing(){
        setHidden(!hidden);
    }

    const MediumLogo = icons.mediumLogoWhite

    return (
        <nav className="nav">
            <Link to="/">
                <MediumLogo className="nav-logo"/>
            </Link>
            <div className={`nav-ul-div ${hidden ? "hidden":""}`}>
                <ul className="nav-ul">
                    <li><ThemeChanger/></li>
                    {
                        subpages.map((subpage) => {
                            return <li key={subpage.url} onClick={() => setHidden(true)}>
                                <Link to={subpage.url}>{subpage.title}</Link>
                            </li>
                        })
                    }
                </ul>
            </div>
            <div className="nav-menu-icon" onClick={changeMenuShowing}>
                {
                    hidden ? <icons.hideMenu size={40}/> : <icons.showMenu size={40}/>
                }
            </div>
        </nav>
    );
  }
  
  export default Nav;