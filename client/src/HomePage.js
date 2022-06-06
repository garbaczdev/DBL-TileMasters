import {Link} from "react-router-dom";


const homeCards = [
    {
        title: "Program Instructions",
        description: "Program your own instruction set for the robot.",
        url: "/program-instructions"
    },
    {
        title: "Robot Utilities",
        description: "Choose from the pre-made instructions.",
        url: "/robot-utils"
    },
    {
        title: "Manual Mode",
        description: "Stop the instructions and move the robot’s arm manually.",
        url: "/manual-mode"
    }
]


function HomePage() {
    return (
        <div className="home-page">
            {
                homeCards.map((cardData) => 
                <>
                    <div id="home-page-card">
                        <h2>{cardData.title}</h2>
                        <p>{cardData.description}</p>
                        <Link to={cardData.url} className="std-btn">Open</Link>
                    </div>
                </>
                )
            }
        </div>
    );
  }
  
  export default HomePage;