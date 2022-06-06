
const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
}

// export async function fetchPaginatedData(){
//     // THIS SHOULD BE CHANGED ON DEPLOYMENT.
//     while (true){
//         const response = await fetch('http://localhost:5000/api/logs',{
//             method: "GET",
//             headers: {
//                 "access-control-allow-origin" : "*",
//                 "Content-type": "application/json; charset=UTF-8"
//             }})
//         const responseJson = await response.json();
//         console.log(responseJson);
//         await sleep(1000);
//         break;
//     }
// }

export function PaginatedDataFetcher(){
    this.last_log_id = -1

}
