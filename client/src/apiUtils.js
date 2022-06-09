
// const NotificationContainer = window.ReactNotifications.NotificationContainer;
// const NotificationManager = window.ReactNotifications.NotificationManager;
import {NotificationManager} from 'react-notifications';


const localDevelopment = false;


export const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
}

async function fetchPaginatedData(lastLogId = 0){
    // THIS SHOULD BE CHANGED ON DEPLOYMENT.


    const response = await fetch(`/api/info-pagination/${lastLogId}`,{
        method: "GET"
    })

    const responseJson = await response.json();

    return responseJson;
}


async function PaginatedDataFetcherLoop(fetcher){

    const missedRequestsThreshold = 10;

    let missedRequests = 0;
    let lostConnection = false;

    while(true){

        try{
            const response = await fetchPaginatedData(fetcher.lastLogId);
            fetcher.updateCallback(response);
            
            missedRequests = 0;
            if (lostConnection){
                // console.log("Connection Retrieved!");
                if (!localDevelopment) NotificationManager.success("", "Connection Regained");
                lostConnection = false;
            }

        }
        catch (e){
            if (missedRequests === missedRequestsThreshold){
                
                // console.log("No response from the server");
                if (!localDevelopment) NotificationManager.warning("", "No response from the server");

                lostConnection = true;
                missedRequests = 0;
            }
            else{
                missedRequests++;
            }
        }
        await sleep(fetcher.loopTimeout);
    }

}

export async function changeMode(mode, dataFetcher=null){

    if (dataFetcher !== null) {
        // Pre-Request change mode
        dataFetcher.updateCallback({
            logs: [],
            mode: mode
        }, true);
    }
    const response = await fetch(`/api/mode/${mode}`,{
        method: "POST"
    });

    const responseJson = await response.json();

    return responseJson;
}


export async function pushArm(){

    const response = await fetch(`/api/push`,{
        method: "POST"
    });

    const responseJson = await response.json();

    return responseJson;
}


export class PaginatedDataFetcher{
	constructor(){

        this.lastLogId = 0;
        this.logs = [];
        this.mode = "instruction";

        this.logsListeners = [];
        this.modeListeners = [];

        this.loopRunning = false;
        this.callbackTimeout = false;

        this.loopTimeout = 500;
        this.maxLogsLength = 100;
    }

    addLogsListener(logsListener){
    	this.logsListeners.push(logsListener);
        logsListener(this.logs);
    }

    addModeListener(modeListener){
        this.modeListeners.push(modeListener);
        modeListener(this.mode);
    }

    runLoop(){
        if (!this.loopRunning){
            PaginatedDataFetcherLoop(this);
            this.loopRunning = true;
        }
    }

    updateCallback(response, setCallbackTimeout=false){

        if (this.callbackTimeout) {
            // Blocked in case of local mode change!
            return;
        };
        if (setCallbackTimeout){
            this.callbackTimeout = true;
            setTimeout(() => this.callbackTimeout = false, this.loopTimeout);
        }

        const logs = response.logs;
        const mode = response.mode;

        const newLogs = logs.filter(log => log.id > this.lastLogId);

        if (newLogs.length > 0){
            
            this.logs = [...this.logs, ...newLogs];
            this.logs = this.logs.slice(-this.maxLogsLength, this.logs.length);

            this.lastLogId = this.logs[this.logs.length - 1].id;

            for (const logListener of this.logsListeners) logListener(this.logs);
        }

        if (mode !== this.mode){
            this.mode = mode;
            for (const modeListener of this.modeListeners) modeListener(this.mode);
        }

    }
}
