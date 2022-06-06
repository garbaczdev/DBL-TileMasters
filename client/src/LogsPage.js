function LogsPage() {

    function log() {
        console.log("WORKS");
        setTimeout(log, 1000);
    }

    log();

    return (
        <div id="logs-page">
            Logs Page
        </div>
    );
  }
  
  export default LogsPage;