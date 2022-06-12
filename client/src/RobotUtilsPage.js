import React from 'react';

import {getThemedIcon, icons} from './icons';

import './styles/RobotUtils.css';


class SortingCard extends React.Component{

    constructor(props){
        super(props);

        this.state = {
        }
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
        }
    }

    render(){
        return (
            <>
                <label className='std-label'>Positive Integer to output:</label>
                <input className="std-text-input number-input" pattern="[A-Za-z]{3}" title="A positive integer" />

                <label className='std-label'>What should come out first:</label>
                <select className='std-dropdown'>
                    <option value="left">Left-Most Bit</option>
                    <option value="right">Right-Most Bit</option>
                </select>
                <label className='std-label'>Expected output:</label>
            </>
        );
    }

    canBeSent(){

    }

    sendInstructions(){
        
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
                            <button className='std-btn std-big-card-send-btn stick-down' onClick={utilCard.sendInstructions}>
                                Send Instructions
                            </button>
                        </div>
                    </div>
                )
            }
        </div>
    );
  }
  
  export default RobotUtilsPage;