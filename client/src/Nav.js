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


function Nav(props) {

    const [hidden, setHidden] = React.useState(true);

    function changeMenuShowing(){
        setHidden(!hidden);
    }

    return (
        <nav className="nav">
            <Link to="/">
                {<icons.MediumLogoWhite className="nav-logo"/>}
            </Link>
            <div className={`nav-ul-div ${hidden ? "hidden":""}`}>
                <ul className="nav-ul">
                    <li><ThemeChanger darkTheme={props.darkTheme} setDarkTheme={props.setDarkTheme}/></li>
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
                    hidden ? <icons.HideMenu size={40}/> : <icons.ShowMenu size={40}/>
                }
            </div>
        </nav>
    );
  }
  
  export default Nav;