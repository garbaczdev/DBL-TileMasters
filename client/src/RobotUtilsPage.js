import React from 'react';
import Popup from 'reactjs-popup';

import {getThemedIcon, icons} from './icons';

import './styles/RobotUtils.css';



function dec2bin(dec) {
    return (dec >>> 0).toString(2);
}


class SortingCard extends React.Component{

    constructor(props){
        super(props);
    }

    render(){
        return (
            <>
                <label className='std-label'>Tiles to be pushed:</label>
                <select className='std-dropdown'>
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

    canBeSent(){

    }

    sendInstructions(){
        
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

        this.popupMessage = "The input is not a non-negative integer"
    }

    render(){
        console.log(this.state);
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

                <button className='std-btn std-big-card-send-btn stick-down' onClick={() => this.sendInstructions()}>
                    Send Instructions
                </button>

                <Popup 
                    open={this.state.popupOpen}
                    onClose={() => this.setState({...this.state, popupOpen: false})}
                    position="right center"
                    closeOnDocumentClick
                >
                    <div className="std-popup">
                    {this.popupMessage}
                    </div>
                </Popup>
            </>
        );
    }

    canBeSent(){
        if (!Number.isInteger(this.state.number) || parseInt(this.state.number) < 0) return false;
        return true;
    }

    sendInstructions(){
        if (!this.canBeSent()){
            this.setState({...this.state, popupOpen: true});
            return;
        }

        const binNumber = this.getBinNumber(parseInt(this.state.number));
    }

    getBinNumber(number){
        return dec2bin(number);
    }

}

class MorseCodeCard extends React.Component{

    constructor(props){
        super(props);

        this.state = {
        }
    }

    render(){
        return (
            <>
                <label className='std-label'>Enter text to be outputted in morse-code</label>
                <input className="std-text-input morse-code-input"/>
                <label className='std-label'>Expected output:</label>

                <button className='std-btn std-big-card-send-btn stick-down' onClick={() => this.sendInstructions()}>
                    Send Instructions
                </button>
            </>
        );
    }

    canBeSent(){

    }

    sendInstructions(){

    }
}


const utilsCards = [
    {
        title: 'Sort the tiles',
        description: 'This instruction will sort the incoming tiles.',
        component: SortingCard,
        Illustration: icons.Sorting
    },
    {
        title: 'Output number in binary',
        description: 'This instruction will output the given positive integer in binary, using as many bits as needed, with 1 denoting white tile and 0 denoting black tile.',
        component: BinaryCard,
        Illustration: icons.Binary
    },
    {
        title: 'Output Morse Code',
        description: 'This instruction will output the given text in a Morse Code, with black denoting short and white denoting long.',
        component: MorseCodeCard,
        Illustration: icons.MorseCode
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
                utilsCards.map((utilCard, index) => 
                    <div key={utilCard.title} className={`std-big-card ${index % 2 === 0 ? "illustration-left" : "illustration-right"}`}>
                        <utilCard.Illustration className="std-big-card-illustration"/>
                        <div className="std-big-card-contents">
                            <h1 className="std-big-card-title">{utilCard.title}</h1>
                            <p className="std-big-card-description">{utilCard.description}</p>
                            {<utilCard.component />}
                        </div>
                    </div>
                )
            }
        </div>
    );
  }
  
  export default RobotUtilsPage;