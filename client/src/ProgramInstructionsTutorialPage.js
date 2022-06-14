
import {getIcon} from './icons';


const cards = [
    {
        title: "Instructions",
        description: "Tile Master operates on the instructions specified by the user. Below are the available instruction types. You can freely modify the instructions and make them repeat, with specifying the repetitions variable. -1 repetitions means repeat forever!",
        example: "Instruction1(repeat:2), Instruction2(repeat:-1) would make the robot complete the Instruction1 twice and then do the Instruction2 forever.",
        iconName: (darkTheme) => "SmallLogo"
    },
    {
        title: "Pattern Instruction",
        description: "This instruction indicates in what order the tiles should be outputed, with 1 denoting white and 0 denoting black.",
        example: "Pattern 1100 would cause the robot to output 2 black tiles and then 2 white tiles",
        iconName: (darkTheme) => "PatternInstruction"
    },
    {
        title: "Requirements Instruction",
        description: "This instruction takes the exact amount of tiles specified by user.",
        example: "Take 2 black tiles and 1 white tile and repeat 2 times.",
        iconName: (darkTheme) => "RequirementsInstruction"
    },
    {
        title: "Bitmask Instruction",
        description: "This instruction indicates the exact order in which the tiles are taken or skipped, with 1 denoting take and 0 denoting skip.",
        example: "1100 would make the robot take 2 tiles, then skip 2 tiles. ",
        iconName: (darkTheme) => "BitmaskInstruction"
    }
]


function ProgramInstructionsTutorialPage({darkTheme}) {
    return (
        <div className="program-instructions-tutorial-page subpage">
            {
                cards.map((card, index) => {
                    const Icon = getIcon(card.iconName(darkTheme));
                    return (
                        <div key={card.title} className={`std-big-card ${index % 2 === 0 ? "illustration-left" : "illustration-right"}`}>
                            <Icon className="std-big-card-illustration"/>
                            <div className="std-big-card-contents">
                                <h1 className="std-big-card-title">{card.title}</h1>
                                <p className="std-big-card-description">{card.description}</p>
                                <label className="std-label">Example:</label>
                                <p className="std-big-card-description">{card.example}</p>
                            </div>
                        </div>
                    );
                })
            }
        </div>
    );
  }
  
  export default ProgramInstructionsTutorialPage;