import {Link} from "react-router-dom";

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
    return (
        <nav className="nav">
            <Link className="nav-logo" to="/">Home</Link>
            <div className="nav-ul-div">
                <ul className="nav-ul">
                    <li>Dark Mode</li>
                    {
                        subpages.map((subpage) => {
                            return <li><Link key={subpage.url} to={subpage.url}>{subpage.title}</Link></li>
                        })
                    }
                </ul>
            </div>
        </nav>
    );
  }
  
  export default Nav;