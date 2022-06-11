
import React from 'react';

import TileCounter from './TileCounter';

import './styles/LogsPage.css';

const testLogs = [
    {
        "additionalData": {},
        "componentName": "Robot",
        "description": "Starting to run",
        "id": 1,
        "type": "turned-on"
    },
    {
        "additionalData": {},
        "componentName": "Robot",
        "description": "Instructions updated to [\"PatternInstruction(pattern:['0', '1'], r:-1)\"]",
        "id": 2,
        "type": "new-instructions"
    },
    {
        "additionalData": {},
        "componentName": "TestingTileScanner",
        "description": "Tile events have been finished",
        "id": 3,
        "type": "testing-events-finished"
    }
]

function LogsPage({darkTheme, dataFetcher}) {

    const [listenerRegistered, setListenerRegistered] = React.useState(false);
    const [logs, setLogs] = React.useState([]);

    if (!listenerRegistered){

        dataFetcher.addLogsListener(setLogs);
        setListenerRegistered(true);
        setLogs(testLogs);
    }

    return (
        <div className="logs-page subpage">
            <h2 className="tile-counter-title">Tile Counter</h2>
            <TileCounter darkTheme={darkTheme} dataFetcher={dataFetcher} />
            <h2 className="logs-title">Logs</h2>
            <div className="log-list item-list">
                {
                    logs.map(log => {

                    })
                }
            </div>
        </div>
    );
  }
  
  export default LogsPage;