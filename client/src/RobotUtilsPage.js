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
                <label className='std-dropdown-label'>Tiles to be pushed:</label>
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
        description: 'This instruction will output the given number in binary, with 1 denoting white and 0 denoting black.',
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
                    <div key={utilCard.title} className={`utils-card ${index % 2 === 0 ? "illustration-left" : "illustration-right"}`}>
                        <utilCard.Illustration className="utils-card-illustration"/>
                        <div className="utils-card-contents">
                            <h1 className="utils-card-title">{utilCard.title}</h1>
                            <p className="utils-card-description">{utilCard.description}</p>
                            {<utilCard.component />}
                            <button className='std-btn utils-card-send-btn' onClick={utilCard.sendInstructions}>
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