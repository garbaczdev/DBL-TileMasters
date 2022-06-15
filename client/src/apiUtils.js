
// const NotificationContainer = window.ReactNotifications.NotificationContainer;
// const NotificationManager = window.ReactNotifications.NotificationManager;
import {NotificationManager} from 'react-notifications';


const localDevelopment = false;


export const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
}

async function fetchPaginatedData(lastLogId = 0, fetchLogs=true){
    // THIS SHOULD BE CHANGED ON DEPLOYMENT.


    const url = fetchLogs ? `/api/info-pagination/${lastLogId}`: "/api/info-pagination/";

    const response = await fetch(url, {
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
            const response = await fetchPaginatedData(fetcher.lastLogId(), fetcher.shouldFetchLogs());

            missedRequests = 0;
            if (lostConnection){
                // console.log("Connection Retrieved!");
                if (!localDevelopment) NotificationManager.success("", "Connection Regained");
                lostConnection = false;
            }

            fetcher.updateCallback(response);

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

export async function sendInstructions(instructions){
    const response = await fetch(`/api/instructions`,{
        method: "PUT",
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "instructions": instructions
        })
    });

    const responseJson = await response.json();

    if (responseJson.ok) NotificationManager.success("", "Instructions sent!", 1000);

    return responseJson;
}

export async function changeMode(mode, dataFetcher=null){

    if (dataFetcher !== null) {
        // Pre-Request change mode
        dataFetcher.updateCallback({
            logs: [],
            mode: mode,
            count: null
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
        this.logsListener = null;
        this.modeListeners = [];
        this.countListeners = [];

        this.loopRunning = false;
        this.callbackTimeout = false;

        this.loopTimeout = 500;
    }

    lastLogId(){
        if (this.logsListener === null) return 0;
        return this.logsListener.lastLogId();
    }

    addLogsListener(logsListener){
    	this.logsListener = logsListener;
    }

    addModeListener(modeListener){
        this.modeListeners.push(modeListener);
    }

    addCountListener(countListener){
        this.countListeners.push(countListener);
    }

    runLoop(){
        if (!this.loopRunning){
            PaginatedDataFetcherLoop(this);
            this.loopRunning = true;
        }
    }

    shouldFetchLogs(){
        return this.logsListener !== null && this.logsListener.isMounted();
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
        const count = response.count;

        if (logs.length > 0 && this.logsListener !== null) this.logsListener.addLogs(logs);

        if (mode !== null) for (const modeListener of this.modeListeners) modeListener(mode);
        
        if (count !== null) for (const countListener of this.countListeners) countListener(count);

    }
}
