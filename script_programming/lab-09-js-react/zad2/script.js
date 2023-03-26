function decrement(){
    let current = document.getElementById('counter').valueAsNumber;
    if (current <= 0) {return 0;}

    let spans = document.getElementsByTagName('span');
    for (let i = 0; i < spans.length; i++){
        spans[i].textContent = current - 1;
    }
    document.getElementById('counter').value = current - 1;
}

setInterval(decrement, 1000);