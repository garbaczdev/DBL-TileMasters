import {Link} from "react-router-dom";

import {getThemedIcon} from './icons';

import './styles/ProgramInstructions.css';

function ProgramInstructionsPage({darkTheme}) {

    const Icon = getThemedIcon("ProgramInstructions", darkTheme);

    return (
        <div className="program-instructions-page subpage">
            <Icon className="subpage-illustration"/>
            <h1 className="subpage-title">Program Instructions</h1>
            <p className="subpage-description">Program the robot's behavior</p>
            

            
            <label className='std-label'>Need an explaination?</label>
            <Link to="./tutorial">
                <div className="std-btn">Open Tutorial</div>
            </Link>
        </div>
    );
  }
  
export default ProgramInstructionsPage;