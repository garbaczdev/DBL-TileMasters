import React from 'react';
import Popup from 'reactjs-popup';

import {getIcon, getThemedIcon, icons} from './icons';
import { sendInstructions as apiSendInstructions} from './apiUtils';

import './styles/RobotUtils.css';



function dec2bin(dec) {
    return (dec >>> 0).toString(2);
}


const MORSE_CHR_TO_BIN = {"A": "01", "B": "1000", "C": "1010", "D": "100", "E": "0", "F": "0010", "G": "110", "H": "0000", "I": "00", "J": "0111", "K": "101", "L": "0100", "M": "11", "N": "10", "O": "111", "P": "0110", "Q": "1101", "R": "010", "S": "000", "T": "1", "U": "001", "V": "0001", "W": "011", "X": "1001", "Y": "1011", "Z": "1100", "1": "01111", "2": "00111", "3": "00011", "4": "00001", "5": "00000", "6": "10000", "7": "11000", "8": "11100", "9": "11110", "0": "11111"};



class SortingCard extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            tileColor: "white"
        }
    }

    render(){
        return (
            <>
                <label className='std-label'>Tiles to be pushed:</label>
                <select className='std-dropdown' value={this.state.tileColor} 
                    onChange={e => this.setState({...this.state, tileColor: e.target.value})}
                >
                    <option value="white">White</option>
                    <option value="black">Black</option>
                    <option value="all">All</option>
                </select>

                <button className='std-btn std-big-card-send-btn stick-down' onClick={() => this.sendInstructions()}>
                    Send Instructions
                </button>
            </>
        );
    }

    sendInstructions(){

        let instruction = null;

        if (this.state.tileColor === "white") instruction = {
            "type": "requirements",
            "black": 0,
            "white": 1,
            "repetitions": -1
        }
        else if (this.state.tileColor === "black") instruction = {
            "type": "requirements",
            "black": 1,
            "white": 0,
            "repetitions": -1
        }
        else if (this.state.tileColor === "all") instruction = {
            "type": "bitmask",
            "bitmask": "1",
            "repetitions": -1
        }

        apiSendInstructions([instruction]);
    }
}





class BinaryCard extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            popupOpen: false,
            firstBit: "left",
            number: '0'
        }

        this.popupMessage = "The input is not a non-negative integer";
    }

    render(){
        return (
            <>
                <label className='std-label'>Positive Integer to output:</label>
                <input className="std-text-input number-input" title="A positive integer" value={this.state.number} 
                    onChange={e => this.setState({...this.state, number: e.target.value})}
                />

                <label className='std-label'>What should come out first:</label>
                <select className='std-dropdown' value={this.state.value} 
                    onChange={e => this.setState({...this.state, firstBit: e.target.value})}
                >
                    <option value="left">Left-Most Bit</option>
                    <option value="right">Right-Most Bit</option>
                </select>
                <label className='std-label'>Expected output:</label>
                <span className="predicted-output">{this.getExpectedOutput()}</span>

                <button className='std-btn std-big-card-send-btn stick-down' onClick={() => this.sendInstructions()}>
                    Send Instructions
                </button>

                <Popup 
                    open={this.state.popupOpen}
                    onClose={() => this.setState({...this.state, popupOpen: false})}
                    position="right center"
                    closeOnDocumentClick
                >
                    {this.popupMessage}
                </Popup>
            </>
        );
    }

    areInformationsValid(){
        if (isNaN(this.state.number) || parseInt(this.state.number) < 0) return false;
        return true;
    }

    sendInstructions(){
        if (!this.areInformationsValid()){
            this.setState({...this.state, popupOpen: true});
            return;
        }

        const binNumber = this.getSequence();
        const instruction = this.generateInstructions(binNumber);
        apiSendInstructions([instruction]);
    }

    getSequence(){
        const binNumber = dec2bin(this.state.number);
        if (this.state.firstBit === "right") return binNumber.split("").reverse().join("");
        return binNumber;
    }

    getExpectedOutput(){
        if (!this.areInformationsValid()) {
            return "Given number is not valid";
        };
        const binNumber = this.getSequence();
        
        return binNumber.split("").map((bit, index) => {

            const iconName = bit === '1' ? "WhiteTile": "BlackTile";
            const Icon = getIcon(iconName, this.props.darkTheme);

            return <Icon key={index} />

        })
    }

    generateInstructions(binNumber){
        return {
            "type": "pattern",
            "pattern": binNumber,
            "repetitions": 1
        }
    }

}


class PatternCard extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            text: "",
            popupOpen: false
        }
        this.popupMessage = "The given text is not a pattern";
    }

    render(){
        return (
            <>
                <label className='std-label'>Enter text to be outputted with the tiles</label>
                <textarea className="std-text-input morse-code-input" value={this.state.text}
                    onChange={(e) => this.setState({...this.state, text: e.target.value})}
                />
                <label className='std-label'>Expected output:</label>
                <span className="predicted-output">{this.getExpectedOutput()}</span>

                <button className='std-btn std-big-card-send-btn stick-down' onClick={() => this.sendInstructions()}>
                    Send Instructions
                </button>
                <Popup 
                    open={this.state.popupOpen}
                    onClose={() => this.setState({...this.state, popupOpen: false})}
                    position="right center"
                    closeOnDocumentClick
                >
                    {this.popupMessage}
                </Popup>
            </>
        );
    }

    areInformationsValid(){
        const text = this.state.text;

        for (const chr of text) if (chr !== "0"  && chr !== "1") return false;
        
        return true;
    }

    sendInstructions(){
        if (!this.areInformationsValid()){
            this.setState({...this.state, popupOpen: true});
            return;
        }

        const sequence = this.getSequence();
        const instruction = this.generateInstructions(sequence);
        apiSendInstructions([instruction]);
    }

    getSequence(){
        
        return this.state.text;
    }

    getExpectedOutput(){
        if (!this.areInformationsValid()) {
            return "Given text is not valid.";
        };
        const sequence = this.getSequence();
        
        return sequence.split("").map((bit, index) => {

            const iconName = bit === '1' ? "WhiteTile": "BlackTile";
            const Icon = getIcon(iconName, this.props.darkTheme);

            return <Icon key={index} />

        })
    }

    generateInstructions(sequence){
        return {
            "type": "pattern",
            "pattern": sequence,
            "repetitions": 1
        }
    }
}



class MorseCodeCard extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            text: "",
            popupOpen: false
        }
        this.popupMessage = "It is not possible to encode the given text into morse code";
    }

    render(){
        return (
            <>
                <label className='std-label'>Enter text to be outputted in morse-code</label>
                <textarea className="std-text-input morse-code-input" value={this.state.text}
                    onChange={(e) => this.setState({...this.state, text: e.target.value.toUpperCase()})}
                />
                <label className='std-label'>Expected output:</label>
                <span className="predicted-output">{this.getExpectedOutput()}</span>

                <button className='std-btn std-big-card-send-btn stick-down' onClick={() => this.sendInstructions()}>
                    Send Instructions
                </button>
                <Popup 
                    open={this.state.popupOpen}
                    onClose={() => this.setState({...this.state, popupOpen: false})}
                    position="right center"
                    closeOnDocumentClick
                >
                    {this.popupMessage}
                </Popup>
            </>
        );
    }

    areInformationsValid(){
        const text = this.state.text;

        for (let i = 0; i < text.length; i++){
            const asciiCode = text.charCodeAt(i);

            // Normal character
            if (asciiCode >= 65 && asciiCode <= 90) continue;

            // Number
            else if (asciiCode >= 48 && asciiCode <= 57) continue;

            return false
        }
        
        return true;
    }

    sendInstructions(){
        if (!this.areInformationsValid()){
            this.setState({...this.state, popupOpen: true});
            return;
        }

        const sequence = this.getSequence();
        const instruction = this.generateInstructions(sequence);
        apiSendInstructions([instruction]);
    }

    getSequence(){
        let sequence = "";
        
        for (const chr of this.state.text) sequence += MORSE_CHR_TO_BIN[chr];
        
        return sequence;
    }

    getExpectedOutput(){
        if (!this.areInformationsValid()) {
            return "Given text is not valid.";
        };
        const sequence = this.getSequence();
        
        return sequence.split("").map((bit, index) => {

            const iconName = bit === '1' ? "WhiteTile": "BlackTile";
            const Icon = getIcon(iconName, this.props.darkTheme);

            return <Icon key={index} />

        })
    }

    generateInstructions(sequence){
        return {
            "type": "pattern",
            "pattern": sequence,
            "repetitions": 1
        }
    }
}


const utilsCards = [
    {
        title: 'Sort the tiles',
        description: 'This instruction will sort the incoming tiles.',
        component: SortingCard,
        Illustration: (darkTheme) => icons.Sorting
    },
    {
        title: 'Output the given pattern',
        description: 'This instruction will output the given pattern using the tiles with 0 being a black tile and 1 being a white tile.',
        component: PatternCard,
        Illustration: (darkTheme) => darkTheme ? icons.PatternDark : icons.PatternLight
    },
    {
        title: 'Output number in binary',
        description: 'This instruction will output the given positive integer in binary, using as many bits as needed, with 1 denoting white tile and 0 denoting black tile.',
        component: BinaryCard,
        Illustration: (darkTheme) => darkTheme ? icons.BinaryDark : icons.BinaryLight
    },
    {
        title: 'Output Morse Code',
        description: 'This instruction will output the given text in a Morse Code, with black denoting short and white denoting long.',
        component: MorseCodeCard,
        Illustration: (darkTheme) => icons.MorseCode
    }
]


function RobotUtilsPage({darkTheme}) {

    const Icon = getThemedIcon("RobotUtils", darkTheme);

    return (
        <div className="robot-utils-page subpage">
            <Icon className="subpage-illustration"/>
            <h1 className="subpage-title">Robot Utilities</h1>
            <p className="subpage-description">Choose from the following pre-programed robot utilities:</p>
            {
                utilsCards.map((utilCard, index) => {
                    const Illustration = utilCard.Illustration(darkTheme);
                    return (
                        <div key={utilCard.title} className={`std-big-card ${index % 2 === 0 ? "illustration-left" : "illustration-right"}`}>
                            <Illustration className="std-big-card-illustration"/>
                            <div className="std-big-card-contents">
                                <h1 className="std-big-card-title">{utilCard.title}</h1>
                                <p className="std-big-card-description">{utilCard.description}</p>
                                {<utilCard.component darkTheme={darkTheme}/>}
                            </div>
                        </div>
                    );
                })
            }
        </div>
    );
  }
  
  export default RobotUtilsPage;