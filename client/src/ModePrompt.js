import React from 'react';

import {changeMode} from './apiUtils';

import './styles/ModePrompt.css';

function ModePrompt({dataFetcher}) {

    const [listenerRegistered, setListenerRegistered] = React.useState(false);
    const [mode, setMode] = React.useState("instruction");

    if (!listenerRegistered){

        dataFetcher.addModeListener(setMode);
        setListenerRegistered(true);
    }


    return (
        <div className={`mode-prompt ${mode === "manual" ? "" : "hidden"}`}>
            <h4>The robot is in the manual mode</h4>
            <button className="std-btn" onClick={() => changeMode("instruction", dataFetcher)}>Switch to Instructions Mode</button>
        </div>
    );
  }
  
  export default ModePrompt;