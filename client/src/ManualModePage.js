import React from 'react';
import { changeMode, pushArm } from './apiUtils';

import {getThemedIcon} from './icons';

import './styles/ManualMode.css';


function ManualModePage({darkTheme, dataFetcher}) {

    const [listenerRegistered, setListenerRegistered] = React.useState(false);
    const [mode, setMode] = React.useState("instruction");

    if (!listenerRegistered){

        dataFetcher.addModeListener(setMode);
        setListenerRegistered(true);
    }

    const Icon = getThemedIcon("ManualMode", darkTheme);

    return (
        <div className="manual-mode-page subpage">
            <Icon className="illustration"/>
            <h1 className="title">Manual Mode</h1>
            <p className="description">Stop the instructions and move the robot’s arm manually. When you hit the button push, the arm of the robot will move and make the tile fall into place. This allows you to take direct control of the robot pushing mechanism.</p>
            {
                mode === "manual"
                ?
                <button className="main-btn std-btn" onClick={pushArm}>
                    Push The Arm
                </button>
                :
                <button className="main-btn std-btn" onClick={() => changeMode("manual", dataFetcher)}>
                    Switch To Manual Mode
                </button>
            }
        </div>
    );
  }
  
  export default ManualModePage;