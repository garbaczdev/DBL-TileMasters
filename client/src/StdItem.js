
import React from 'react';

import {icons} from './icons';
import {sleep} from './apiUtils';


let changing = false;
const infoTransitionTime = 200;

async function changeHidden(hidden, setHidden, setInfoTransparent){
    if (changing) return;
    changing = true;

    if (hidden){
        setHidden(false);
        await sleep(infoTransitionTime);
        setInfoTransparent(false);
        await sleep(infoTransitionTime);
    }
    else{
        setInfoTransparent(true);
        await sleep(infoTransitionTime);
        setHidden(true);
        await sleep(infoTransitionTime);
    }

    changing = false;
}


// STYLE IS IN App.scss
function StdItem({mainContent, infoContent}){

    const [hidden, setHidden] = React.useState(true);
    const [infoTransparent, setInfoTransparent] = React.useState(true);

    const Icon = hidden ? icons.ShowMore : icons.Hide;

    return (
        <li className="std-item">
            <div className="std-item-contents">
                {mainContent}
                <Icon className="std-item-show-icon" size={30} onClick={() => changeHidden(hidden, setHidden, setInfoTransparent)}/>
            </div>
            <div className={`std-item-info ${hidden ? "hidden" : ""} ${infoTransparent ? "transparent" : ""}`}>
                {
                    infoContent
                }
            </div>
        </li>
    );
}
  
export default StdItem;