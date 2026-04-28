function copyKey(button) {
    const key = document.getElementById("generated-key").innerText;
    navigator.clipboard.writeText(key).then(() => {
        if (!button.dataset.originalText) {
            button.dataset.originalText = button.innerText;
        }
        button.innerText = "Copied!";
        clearTimeout(button.dataset.timeoutId);
        const timeoutId = setTimeout(() => {
            button.innerText = button.dataset.originalText;
        }, 3000);
        button.dataset.timeoutId = timeoutId;
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