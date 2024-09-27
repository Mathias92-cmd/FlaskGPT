function cloneAnswerBlock(){
    const output = document.querySelector("#gpt-output");
    const template = document.querySelector("#chat-template");
    const clone = template.cloneNode(true);
    clone.id = "";
    output.appendChild(clone);
    clone.classList.remove("hidden");
    return clone.querySelector(".message");
}

function addToLog(message) {
    const answerBlock = cloneAnswerBlock();
    answerBlock.innerText = message;
    return answerBlock;
}