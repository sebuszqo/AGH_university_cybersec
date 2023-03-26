const counterInput = document.getElementById("counter");
const spans = document.querySelectorAll("span");



function updateCounter() {
    let counter = counterInput.value;
    if (counter > 0) {
        counter--;
        counterInput.value = counter;
    }

    for (let i = 0; i < spans.length; i++) {
        spans[i].innerHTML = counter;
    }
}

setInterval(updateCounter, 1000);
