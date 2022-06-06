import {Link} from "react-router-dom";


function Nav() {
    return (
        <div className="Nav">
            <Link to="/">Home</Link>
            <Link to="/program-instructions">Program Instructions</Link>
            <Link to="/robot-utils">Robot Utils</Link>
            <Link to="/manual-mode">Manual Mode</Link>
        </div>
    );
  }
  
  export default Nav;