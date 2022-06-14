import React from 'react';

import {Link} from "react-router-dom";
import Popup from 'reactjs-popup';

import {getThemedIcon, getIcon} from './icons';
import StdItem from './StdItem';
import { sendInstructions as apiSendInstructions} from './apiUtils';

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


function Instruction({instructionJson, index, deleteCallback}){

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

class ProgramInstructionsPopup extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            instructionType: "requirements",
            instructionOptions: {
                white: 0,
                black: 0
            },
            repeat: 1
        }
    }

    render(){
        return (
            <Popup 
                open={this.props.parent.isPopupOpened()}
                onClose={() => this.props.parent.closePopup()}
                position="right center"
                className="program-instructions-popup"
            >
                <label className='std-label'>Instruction Type:</label>
                <select className='std-dropdown' value={this.state.instructionType}
                    onChange={e => this.setState({...this.state, instructionType: e.target.value})}
                >
                    <option value="requirements">Requirements</option>
                    <option value="pattern">Pattern</option>
                    <option value="bitmask">Bitmask</option>
                </select> 


                <label className='std-label'>Number of repetitions:</label>
                <input className="std-text-input number-input" title="Number of repetitions" value={this.state.repetitions} 
                    onChange={e => this.setState({...this.state, repetitions: e.target.value})}
                />

                <div className='btn-div'>

                    <button className='std-btn' onClick={() => this.props.parent.closePopup()}>Close</button>

                    {
                        this.canBeAdded() && <button className='std-btn' onClick={() => this.props.parent.closePopup()}>Add Instruction</button>
                    }

                </div>
            </Popup>
        );
    }

    canBeAdded(){
        return true;
    }

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
            }],
            popupOpen: false
        }
    }

    render(){
        return (
            <>
                <ul className='std-item-list'>
                    {
                        this.state.instructionsJson.map((instructionJson, index, instructionsJson) => 
                            <Instruction key={index} instructionJson={instructionJson} index={index} deleteCallback={this.deleteCallback}/>
                        )
                    }
                </ul>
                <div className="btn-div">
                    <button className='std-btn' onClick={() => this.openPopup()}>Add Instruction</button>
                    <button className='std-btn' onClick={() => this.sendInstructions()}>Send Instructions</button>
                </div>

                <ProgramInstructionsPopup parent={this}/>
            </>
        );
    }

    isPopupOpened(){
        return this.state.popupOpen;
    }


    openPopup(){
        this.setState({...this.state, popupOpen: true})
    }

    closePopup(){
        this.setState({...this.state, popupOpen: false})
    }

    deleteCallback(index){

    }

    sendInstructions(){
        apiSendInstructions(this.state.instructionsJson);
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