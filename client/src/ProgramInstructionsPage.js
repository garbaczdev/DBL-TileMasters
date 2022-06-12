import React from 'react';

import {Link} from "react-router-dom";

import {getThemedIcon, getIcon} from './icons';
import StdItem from './StdItem';

import './styles/ProgramInstructions.css';


const instructionAttributes = [
    {
        name: "Type",
        attribute: "type"
    },
    {
        name: "Repetitions",
        attribute: "repetitions"
    },
]


function Instruction({instructionJson}){

    let Icon = null;
    let name = null;
    let additionalInfo = null;

    if (instructionJson.type === "requirements"){
        name = `Requirements b:${instructionJson.black} w:${instructionJson.black}`;
        Icon = getIcon("RequirementsInstruction");

        additionalInfo = [
            {
                name: "Black",
                attribute: "black"
            },
            {
                name: "White",
                attribute: "white"
            },
        ]

    }

    else if (instructionJson.type === "pattern"){
        name = `Pattern ${instructionJson.pattern}`;
        Icon = getIcon("PatternInstruction");

        additionalInfo = [
            {
                name: "Pattern",
                attribute: "pattern"
            },
        ]
    }

    else if (instructionJson.type === "bitmask"){
        name = `Bitmask ${instructionJson.bitmask}`;
        Icon = getIcon("BitmaskInstruction");

        additionalInfo = [
            {
                name: "Bitmask",
                attribute: "bitmask"
            },
        ]
    }

    return (
        <StdItem 
            mainContent={
                <>
                <Icon className="std-item-icon" size={30}/>
                <span className="outline-color">{instructionJson.repetitions}</span>
                <span className="std-item-description">{name}</span>
                </>
            }
            infoContent={
                <ul className={"std-item-info-list"}>
                    {
                        instructionAttributes.map(({name, attribute}) => <li key={attribute}><span className='attribute-name'>{name + ": "}</span>{instructionJson[attribute]}</li>)
                    }
                    {
                        additionalInfo.map(({name, attribute}) => <li key={attribute}><span className='attribute-name'>{name + ": "}</span>{instructionJson[attribute]}</li>)
                    }
                </ul>
            }
        />
    );
}


class InstructionList extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            instructionsJson: [{
                "type": "requirements",
                "black": 1,
                "white": 0,
                "repetitions": -1
            },
            {
                "type": "bitmask",
                "bitmask": "1",
                "repetitions": -1
            }]
        }
    }

    render(){
        return (
            <ul className='std-item-list'>
                {
                    this.state.instructionsJson.map((instructionJson, index, instructionsJson) => 
                        <Instruction key={index} instructionJson={instructionJson} moveCallback={this.moveCallback} index={index} length={instructionsJson.length}/>
                    )
                }
            </ul>
        );
    }

    moveCallback(index, up=true){

    }

    indexCallback(){

    }

}


function ProgramInstructionsPage({darkTheme}) {

    const Icon = getThemedIcon("ProgramInstructions", darkTheme);

    return (
        <div className="program-instructions-page subpage">
            <Icon className="subpage-illustration"/>
            <h1 className="subpage-title">Program Instructions</h1>
            <p className="subpage-description">Program the robot's behavior</p>
            
            <InstructionList />
            
            <label className='std-label'>Need an explaination?</label>
            <Link to="./tutorial">
                <div className="std-btn">Open Tutorial</div>
            </Link>
        </div>
    );
  }
  
export default ProgramInstructionsPage;