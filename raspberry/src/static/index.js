

async function sendInstructions(instructions){

    const instruction_object = {
        instructions: instructions
    }

    const json_instructions = JSON.stringify(instruction_object);

    const response = await fetch("./api/instructions", {
        method: "PUT",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: json_instructions
    });
    
    const content = await response.json();

    console.log("INSTRUCTIONS: ", instructions, "SEND INSTRUCTIONS RESPONSE:", content);
}

async function push(){
    const response = await fetch("./api/push", {method: "POST"});
    
    const content = await response.json();

    console.log("PUSH RESPONSE:", content);
}

function addPushButtonEvents(){
    const pushButtons = document.getElementsByClassName('push-btn');

    for (let pushBtn of pushButtons){
        pushBtn.addEventListener('click', push)
    }
}

function addSendInstructionEvents(){
    
    const sortingBtn = document.getElementById("sorting-instructions-btn");
    const resetBtn = document.getElementById("reset-instructions-btn");

    const sortingInstruction = {
        type: "requirements",
        black: 1,
        white: 0,
        repetitions: -1
    }

    sortingBtn.addEventListener("click", (event) => sendInstructions([sortingInstruction]))
    resetBtn.addEventListener("click", (event) => sendInstructions([]))

}

addPushButtonEvents();
addSendInstructionEvents();