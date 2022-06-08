
const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
}

export async function fetchPaginatedData(){
    // THIS SHOULD BE CHANGED ON DEPLOYMENT.
    const response = await fetch('./api/logs',{
        method: "GET"
    })

    try{
        const responseJson = await response.json();
        return responseJson;
    }
    catch(e){
        return response;
    }
}

export function PaginatedDataFetcher(){

    this.logs_listener = null;
    this.last_log_id = -1;

    this.mode_listener = null;
    
    this.add_logs_listener = (logs_listener) => {
        this.logs_listener = logs_listener
    }

    this.add_mode_listener = (mode_listener) => {
        this.mode_listener = mode_listener
    }


    async function fetchAndUpdateData(){
        while(true){
            const response = await fetchPaginatedData();
            // if (this.logs_listener != null && this.mode_listener != null){
            //     console.log("FETCHING");
            // }
            console.log(response);
            await sleep(2000);
        }
    }

    fetchAndUpdateData();
}
