import React from 'react';

import {getColor} from './ThemeChanger';
import {icons} from './icons';

import './styles/TileCounter.css';

const counterElements = [
    {
        attribute: "b",
        iconName: "BlackTile"
    },
    {
        attribute: "w",
        iconName: "WhiteTile"
    },
    {
        attribute: "u",
        iconName: "UndefinedTile"
    }
]

function TileCounter({darkTheme, dataFetcher}) {

    const [listenerRegistered, setListenerRegistered] = React.useState(false);
    const [count, setCount] = React.useState({
        "b": 0,
        "w": 0,
        "u": 0
    });

    if (!listenerRegistered){

        dataFetcher.addCountListener(setCount);
        setListenerRegistered(true);
    }


    return (
        <div className="tile-counter">
            <ul className="tile-counter-list">
                {
                    counterElements.map((counterElement) => {
                        const Icon = icons[counterElement.iconName];
                        const color = getColor(darkTheme, "outline")

                        return (
                            <li key={counterElement.attribute} className="tile-counter-element">
                                <span className="tile-counter-element-counter">{count[counterElement.attribute]}</span>
                                <Icon className="tile-counter-element-icon" color={color}/>
                            </li>
                        );
                    })
                }
            </ul>
        </div>
    );
  }
  
export default TileCounter;