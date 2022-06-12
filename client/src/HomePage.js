import {Link} from "react-router-dom";

import {getThemedIcon} from './icons';

import './styles/HomePage.css';


const homeCards = [
    {
        title: "Program Instructions",
        description: "Program your own instruction set for the robot.",
        url: "/program-instructions",
        iconName: "ProgramInstructions"
    },
    {
        title: "Robot Utilities",
        description: "Choose from the pre-made instructions.",
        url: "/robot-utils",
        iconName: "RobotUtils"
    },
    {
        title: "Manual Mode",
        description: "Stop the instructions and move the robot’s arm manually.",
        url: "/manual-mode",
        iconName: "ManualMode"
    }
]


function HomePage({darkTheme}) {

    return (
        <div className="home-page">
            {
                homeCards.map((cardData) => {

                    const Icon = getThemedIcon(cardData.iconName, darkTheme);

                    return (
                        <div className="std-card" key={cardData.url}>
                            {<Icon className="illustration"/>}
                            <h2>{cardData.title}</h2>
                            <p>{cardData.description}</p>
                            <Link to={cardData.url}>
                                <div className="std-btn">Open</div>

                            </Link>
                        </div>
                    );
                })
            }
        </div>
    );
  }
  
  export default HomePage;