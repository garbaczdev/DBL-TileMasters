
import React from 'react';

import TileCounter from './TileCounter';
import {getLogIcon} from './icons';
import StdItem from './StdItem';

import './styles/LogsPage.css';

const testLogs = [
    {
        "additionalData": {},
        "componentName": "Robot",
        "date": "11-06-2022",
        "description": "Starting to run",
        "id": 1,
        "time": "14:01:49",
        "type": "turned-on"
    },
    {
        "additionalData": {},
        "componentName": "Robot",
        "date": "11-06-2022",
        "description": "Instructions updated to [\"PatternInstruction(pattern:['0', '1'], r:-1)\"]",
        "id": 2,
        "time": "14:01:49",
        "type": "new-instructions"
    },
    {
        "additionalData": {},
        "componentName": "TestingTileScanner",
        "date": "11-06-2022",
        "description": "Tile events have been finished",
        "id": 3,
        "time": "14:01:49",
        "type": "testing-events-finished"
    }
]

const logInfoAttributes = [
    {
        name: "Id",
        attribute: "id"
    },
    {
        name: "Date",
        attribute: "date"
    },
    {
        name: "Time",
        attribute: "time"
    },
    {
        name: "Type",
        attribute: "type"
    },
    {
        name: "Component",
        attribute: "componentName"
    },
    {
        name: "Description",
        attribute: "description"
    },
]

const maxLogDescriptionLength = 45;

function Log({log, darkTheme}){

    const LogIcon = getLogIcon(log.type, darkTheme);

    let description = log.description;
    if (description.length > maxLogDescriptionLength) description = description.slice(0, maxLogDescriptionLength - 3) + "...";


    const mainContent = <>
        <LogIcon className="std-item-icon" size={30}/>
        <span className="log-time">{log.time}</span>
        <span className="std-item-description log-description">{description}</span>
    </>

    const infoContent = <>
        <ul className={"std-item-info-list"}>
            {
                logInfoAttributes.map(({name, attribute}) => <li key={attribute}><span className='attribute-name'>{name + ": "}</span>{log[attribute]}</li>)
            }
        </ul>
    </>

    return (
        <StdItem mainContent={mainContent} infoContent={infoContent} />
    );
}


class LogsPage extends React.Component{
    constructor(props){
        super(props);

        this.state = {
            logs: [],
            lastLogId: 0,
        }

        this.maxLogsLength = 100;

        this.props.dataFetcher.addLogsListener(this);

        // TESTING
        // setTimeout(() => {
        //     this.addLogs(testLogs);
        // }, 200)
    }
    render(){
        return (
            <div className="logs-page subpage">
                <h2 className="tile-counter-title">Tile Counter</h2>
                <TileCounter darkTheme={this.props.darkTheme} dataFetcher={this.props.dataFetcher} />
                <h2 className="logs-title">Logs</h2>
                <ul className="log-list std-item-list">
                    {
                        this.state.logs.length > 0
                        ?
                        this.state.logs
                        :
                        <h1 className="log-loading">Loading...</h1>
                    }
                </ul>
            </div>
        );
    }

    lastLogId(){
        return this.state.lastLogId;
    }

    addLogs(logs){

        if (logs.length === 0) return;

        const newLogs = logs.filter(log => log.id > this.state.lastLogId);

        if (newLogs.length > 0){

            const lastLogId = newLogs[newLogs.length - 1].id;

            const newLogElements = newLogs.map(log => <Log key={log.id} log={log} darkTheme={this.props.darkTheme}/>).reverse();

            let updatedLogs = [...newLogElements, ...this.state.logs];
            updatedLogs = updatedLogs.slice(-this.maxLogsLength, updatedLogs.length);
    
            this.setState({
                logs: updatedLogs,
                lastLogId: lastLogId
            })
        }
    }
};
  
  export default LogsPage;