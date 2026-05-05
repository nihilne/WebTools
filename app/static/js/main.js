function copyToClipboard(button, sourceId) {
    const text = document.getElementById(sourceId).innerText;
    navigator.clipboard.writeText(text).then(() => {
        if (!button.dataset.originalText) {
            button.dataset.originalText = button.innerText;
        }
        button.innerText = "Copied!";
        clearTimeout(button.dataset.timeoutId);
        button.dataset.timeoutId = setTimeout(() => {
            button.innerText = button.dataset.originalText;
        }, 3000);
    });
}

function setVAT(value) {
    document.getElementById("vat-input").value = value;
}

function randomNumber() {
    return Math.floor(Math.random() * 15);
}

function animateToolIcons() {
    if (randomNumber() != randomNumber()) {
        return;
    }
    const icons = document.querySelectorAll(".tool-icon");
    icons.forEach((icon, i) => {
        setTimeout(() => {
            icon.classList.add("spin-once");
        }, i * 60);
    });
}

window.addEventListener("load", () => {
    animateToolIcons();
});