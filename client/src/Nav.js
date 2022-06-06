import React from 'react';

import {Link} from "react-router-dom";
import { AiOutlineMenuFold,  AiOutlineMenuUnfold} from 'react-icons/ai';


import './styles/Nav.css';


const subpages = [
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
]


function Nav() {

    const [hidden, setHidden] = React.useState(false);

    function changeMenuShowing(){
        setHidden(!hidden);
    }

    return (
        <nav className="nav">
            <Link className="nav-logo" to="/">Home</Link>
            <div className={`nav-ul-div ${hidden ? "hidden":""}`}>
                <ul className="nav-ul">
                    <li>Dark Mode</li>
                    {
                        subpages.map((subpage) => {
                            return <li onClick={() => setHidden(true)}>
                                <Link key={subpage.url} to={subpage.url}>{subpage.title}</Link>
                            </li>
                        })
                    }
                </ul>
            </div>
            <div className="nav-menu-icon" onClick={changeMenuShowing}>
                {
                    hidden ? <AiOutlineMenuUnfold size={40}/> : <AiOutlineMenuFold size={40}/>
                }
            </div>
            {/* {
                hidden?
                <li onClick={() => setHidden(false)}>
                    <AiOutlineMenuUnfold/>
                </li>
                :
                <li onClick={() => setHidden(true)}>
                    <AiOutlineMenuFold/>
                </li>
            } */}
        </nav>
    );
  }
  
  export default Nav;