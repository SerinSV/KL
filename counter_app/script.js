// Get the elements
const decrementButton = document.getElementById("decrement");
const incrementButton = document.getElementById("increment");
const resetButton = document.getElementById("reset");
const countElement = document.getElementById("count");

// Set initial count
let count = 0;
countElement.textContent = count;

// Event listeners for buttons
decrementButton.addEventListener("click", decrement);
incrementButton.addEventListener("click", increment);
countElement.addEventListener("click",reset)
resetButton.addEventListener("click", reset)

// Decrement function
function decrement() {
    if (count > 0) {
        count--;
        countElement.textContent = count;
    }
}

// Increment function
function increment() {
    count++;
    countElement.textContent = count;
}

function reset(){
    count=0;
    countElement.textContent = count;
}
