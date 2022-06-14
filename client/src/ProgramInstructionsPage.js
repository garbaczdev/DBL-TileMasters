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


const DeleteInstructionIcon = getIcon("Unknown");

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
                <DeleteInstructionIcon className="delete-instruction-icon" size={30} onClick={() => deleteCallback(index)}/>
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
            white: 1,
            black: 1,
            bitmask: "1",
            pattern: "1",
            repetitions: 1
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

                {
                    this.state.instructionType === "requirements"
                    ?
                    // Requirements
                    <>
                        <label className='std-label'>Number of required black tiles</label>
                        <input className="std-text-input number-input" title="Number of black tiles" value={this.state.black} 
                            onChange={e => {
                                    this.setState({...this.state, black: e.target.value}); 
                                }
                            }
                            onBlur={e => {

                                const newValue = e.target.value;
                                const black = parseInt(newValue);

                                if (isNaN(newValue) || (black === 0 && this.state.white === 0) || black < 0) {
                                    this.setState({...this.state, black: 1});
                                    return;
                                }

                                this.setState({...this.state, black: black});
                                }

                            }
                        />
                        <label className='std-label'>Number of required white tiles</label>
                        <input className="std-text-input number-input" title="Number of white tiles" value={this.state.white} 
                            onChange={e => {
                                    this.setState({...this.state, white: e.target.value}); 
                                }
                            }
                            onBlur={e => {

                                const newValue = e.target.value;
                                const white = parseInt(newValue);

                                if (isNaN(newValue) || (white === 0 && this.state.black === 0) || white < 0) {
                                    this.setState({...this.state, white: 1});
                                    return;
                                }

                                this.setState({...this.state, white: white});
                                }

                            }
                        />
                    </>
                    
                    :
                    this.state.instructionType === "pattern"
                    ?
                    <>
                        <label className='std-label'>Pattern to be displayed:</label>
                        <textarea className="std-text-input" value={this.state.pattern}
                            onChange={(e) => this.setState({...this.state, pattern: e.target.value})}
                            onBlur={e => {

                                const newValue = e.target.value;

                                if (!this.isPattern(newValue)) this.setState({...this.state, pattern: "1"});
                                }

                            }
                        />
                    </>
                    :
                    <>
                        <label className='std-label'>Bitmask:</label>
                        <textarea className="std-text-input" value={this.state.bitmask}
                            onChange={(e) => this.setState({...this.state, bitmask: e.target.value})}
                            onBlur={e => {

                                const newValue = e.target.value;

                                if (!this.isPattern(newValue)) this.setState({...this.state, bitmask: "1"});
                                }

                            }
                        />
                    </>
                }


                <label className='std-label'>Number of repetitions:</label>
                <input className="std-text-input number-input" title="Number of repetitions" value={this.state.repetitions} 
                    onChange={e => {

                        this.setState({...this.state, repetitions: e.target.value});
                        
                    }
                    }
                    onBlur={e => {

                        const newValue = e.target.value;
                        if (isNaN(newValue)) {
                            this.setState({...this.state, repetitions: 1});
                            return;
                        }

                        const repetitions = parseInt(newValue);

                        if (repetitions < -1) {
                            this.setState({...this.state, repetitions: -1});
                            return;
                        };

                        this.setState({...this.state, repetitions: repetitions});
                        }

                    }
                />

                <div className='btn-div'>

                    <button className='std-btn' onClick={() => this.close()}>Close</button>

                    {
                        <button className='std-btn' onClick={() => this.addInstruction()}>Add Instruction</button>
                    }

                </div>
            </Popup>
        );
    }

    close(){
        this.props.parent.closePopup();
    }

    isPattern(text){
        if (text.length === 0) return false;
        for (const chr of text) if (chr !== "0" && chr !== "1") return false;
        return true;
    }

    getInstruction(){
        let additionalInfo = {};
        if (this.state.instructionType === "requirements") additionalInfo = {
            black: this.state.black,
            white: this.state.white
        }
        else if (this.state.instructionType === "pattern") additionalInfo = {
            pattern: this.state.pattern,
        }
        else if (this.state.instructionType === "bitmask") additionalInfo = {
            bitmask: this.state.bitmask,
        }

        return {
            ...additionalInfo,
            type: this.state.instructionType,
            repetitions: this.state.repetitions
        }
    }

    addInstruction(){

        const instruction = this.getInstruction();

        this.props.parent.addInstruction(instruction);


        // this.close();
    }

}


class InstructionList extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            instructionsJson: [],
            popupOpen: false
        }
    }

    render(){

        return (
            <>
                <ul className='std-item-list'>
                    {
                        this.state.instructionsJson.map((instructionJson, index) => 
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
        const instructions = this.state.instructionsJson;
        const newInstructions =  instructions.slice(0, index);
        // ???
        // newInstructions.push(...instruction.slice(index + 1, instructions.length));
        // this.setState({...this.state, instructionsJson: newInstructions});
    }

    addInstruction(instruction){
        const newInstructions = [...this.state.instructionsJson, instruction];
        this.setState({...this.state, popupOpen: false, instructionsJson: newInstructions});
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